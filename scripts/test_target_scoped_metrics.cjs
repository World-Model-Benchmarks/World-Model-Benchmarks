#!/usr/bin/env node
// Compare browser filtering against every target/role row, not global marginals.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assets = path.resolve(__dirname, '../docs/assets');
const m = JSON.parse(fs.readFileSync(path.join(assets,'benchmarks.json'),'utf8'));
const shards = [1,2,3,4].flatMap(i=>JSON.parse(fs.readFileSync(path.join(assets,`benchmarks-${i}.json`),'utf8')));
class Element {
  constructor(){this.children=[];this.attrs={};this.style={setProperty(){}};this.handlers={};}
  set innerHTML(v){this.html=v;this.children=[];}
  get innerHTML(){return this.html||'';}
  append(...v){this.children.push(...v);}
  setAttribute(k,v){this.attrs[k]=v;}
  addEventListener(k,v){this.handlers[k]=v;}
  querySelectorAll(){return [];}
}
const nodes=new Map();
const document={querySelector(k){if(!nodes.has(k))nodes.set(k,new Element());return nodes.get(k);},querySelectorAll(){return [];},createElement(){return new Element();}};
const source=fs.readFileSync(path.join(assets,'app-v3-core.js'),'utf8');
const api=vm.runInNewContext(source.replace(/\ninit\(\);\s*$/,'\n')+'\n({state,normalizeCorpus,visibleItems,countForValue,renderCards,buildMatrix})', {document,location:{search:'',pathname:'/',hash:''},URLSearchParams});
const plain=x=>JSON.parse(JSON.stringify(x));
const names=x=>plain(x.map(i=>i.shortName)).sort();
api.state.metadata=m;api.state.benchmarks=api.normalizeCorpus(shards,m);
assert.equal(api.state.benchmarks.length,102);
assert.equal(api.state.benchmarks.reduce((n,i)=>n+i.evaluationTracks.length,0),307);
for(const item of api.state.benchmarks){
  const exported=shards.find(x=>x.shortName===item.shortName);
  assert.deepEqual(plain(item.evaluationTracks),exported.evaluationTracks,item.shortName);
  for(const t of item.evaluationTracks){
    assert.deepEqual([t.protocols.join('+'),t.metrics.join('+')],m.categoryRecords[t.scope][item.shortName]);
  }
}
function reset(){Object.values(api.state.filters).forEach(s=>s.clear());api.state.search='';api.state.period=null;}
const targets=Object.values(m.targetLabels);
function wanted(selected,ps,ms){
  return Object.keys(m.records).filter(name=>Object.entries(m.categoryRecords).some(([scope,rows])=>{
    const codes=rows[name];if(!codes)return false;
    const tc=scope[0]==='T'?scope:(['S5','S6'].includes(scope)?'T6':'T7');
    return (!selected.length||selected.includes(m.targetLabels[tc]))&&(!ps.length||ps.some(p=>codes[0].split('+').includes(p)))&&(!ms.length||ms.some(v=>codes[1].split('+').includes(v)));
  })).sort();
}
const selections=[[],...targets.map(t=>[t]),...targets.flatMap((t,i)=>targets.slice(i+1).map(u=>[t,u])),targets];
let checks=0;
for(const selected of selections)for(const ps of [[],['OL'],['CL'],['OL','CL']])for(const ms of [[],['P'],['O'],['P','O']]){
  reset();selected.forEach(t=>api.state.filters.targets.add(t));ps.forEach(p=>api.state.filters.protocols.add(p));ms.forEach(x=>api.state.filters.metrics.add(x));
  assert.deepEqual(names(api.visibleItems()),wanted(selected,ps,ms),JSON.stringify({selected,ps,ms}));
  for(const metric of ['P','O'])assert.equal(api.countForValue('metrics',metric),wanted(selected,ps,[metric]).length);
  for(const protocol of ['OL','CL'])assert.equal(api.countForValue('protocols',protocol),wanted(selected,[protocol],ms).length);
  for(const target of targets)assert.equal(api.countForValue('targets',target),wanted([target],ps,ms).length);
  checks++;
}
reset();api.state.filters.targets.add(m.targetLabels.T6);
assert.equal(api.countForValue('protocols','CL'),5);
assert.equal(api.countForValue('metrics','O'),4);
api.state.filters.metrics.add('O');
assert.deepEqual(names(api.visibleItems()),['KineBench','RoboWM-Bench','WoW-World-Eval','WorldSimBench'].sort());
reset();api.state.filters.targets.add(m.targetLabels.T1);
assert.equal(api.countForValue('metrics','O'),0);
api.renderCards(api.visibleItems());
const cards=nodes.get('#benchmark-grid').children;
assert.equal(cards.length,46);
assert.ok(cards.every(c=>c.innerHTML.includes('Metrics P</span>')));
reset();api.state.filters.targets.add(m.targetLabels.T7);api.state.search='WMBench';
assert.equal(api.visibleItems().length,1);
api.renderCards(api.visibleItems());assert.ok(nodes.get('#benchmark-grid').children[0].innerHTML.includes('Metrics P · O'));
reset();api.buildMatrix();
for(const [id,group,labels] of [['#taxonomy-matrix','protocols',m.protocolLabels],['#metrics-matrix','metrics',m.metricLabels]]){
  const cells=nodes.get(id).children;
  assert.equal(cells.length,24);
  targets.forEach((target,i)=>Object.keys(labels).forEach((v,j)=>{
    const count=wanted([target],group==='protocols'?[v]:[],group==='metrics'?[v]:[]).length;
    assert.equal(cells[4+i*3+j].attrs['aria-label'],`${target}, ${labels[v]}: ${count} benchmarks`);
  }));
}
console.log(`PASS: all 307 target/role rows, ${checks} combined-filter cases and their facet counts, both matrices, and target-specific card labels.`);
console.log('PASS: Control Fidelity CL=5/O=4; Visual Quality O=0; WMBench utility P+O is not inherited by diagnostic targets.');
