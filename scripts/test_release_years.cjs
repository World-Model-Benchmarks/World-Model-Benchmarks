#!/usr/bin/env node
// Independent 102-year PDF transcription and browser-logic regression checks.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const root = path.resolve(__dirname, '..');
const assets = path.join(root, 'docs/assets');
const audit = JSON.parse(fs.readFileSync(path.join(__dirname, 'release_years_20260907.json'), 'utf8'));
const manifest = JSON.parse(fs.readFileSync(path.join(assets, 'benchmarks.json'), 'utf8'));
const shards = [1,2,3,4].flatMap(i => JSON.parse(fs.readFileSync(path.join(assets, `benchmarks-${i}.json`), 'utf8')));
class Element {
  constructor() { this.children=[]; this.attrs={}; this.style={setProperty(){}}; this.handlers={}; }
  set innerHTML(value) { this.html=value; this.children=[]; }
  get innerHTML() { return this.html || ''; }
  append(...items) { this.children.push(...items); }
  setAttribute(key, value) { this.attrs[key]=value; }
  addEventListener(key, value) { this.handlers[key]=value; }
  querySelectorAll() { return []; }
}
const nodes = new Map();
const document = {querySelector(key){if (!nodes.has(key)) nodes.set(key,new Element());return nodes.get(key);},querySelectorAll(){return [];},createElement(){return new Element();}};
const source = fs.readFileSync(path.join(assets,'app-v3-core.js'),'utf8');
const api = vm.runInNewContext(source.replace(/\ninit\(\);\s*$/, '\n') + '\n({state,normalizeCorpus,matchesPeriod,visibleItems,renderCards,buildTimeline})', {document,URLSearchParams,location:{search:'',pathname:'/',hash:''}});
api.state.metadata=manifest;
api.state.benchmarks=api.normalizeCorpus(shards,manifest);
assert.equal(api.state.benchmarks.length,102);
assert.deepEqual(Object.fromEntries(api.state.benchmarks.map(x=>[x.shortName,x.year])),audit.years);
assert.ok(api.state.benchmarks.every(x=>x.releaseYear===x.year));
for (const [period,count] of Object.entries(audit.releaseWindowCounts)) {
  api.state.period=period;
  assert.equal(api.visibleItems().length,count,period);
}
api.state.period=null;
api.buildTimeline();
const columns=nodes.get('#timeline-chart').children;
assert.equal(columns.length,5);
manifest.timelineBins.forEach((bin,i)=>{
  assert.equal(columns[i].children[0].children[0].attrs['aria-label'],`${bin.label}: ${audit.releaseWindowCounts[bin.label]} new benchmarks, ${audit.cumulativeCounts[i]} cumulative`);
});
api.renderCards(api.state.benchmarks);
const cards=nodes.get('#benchmark-grid').children;
for (const [name,data] of Object.entries(manifest.publicationMetadata)) {
  const item=api.state.benchmarks.find(x=>x.shortName===name);
  const card=cards[api.state.benchmarks.indexOf(item)];
  assert.ok(card.innerHTML.includes(`Release Year: ${audit.years[name]}`),name);
  assert.ok(card.innerHTML.includes(`${data.venue} ${data.publicationYear}`),name);
}
assert.equal(manifest.records.ComPhy[1],2022);
assert.equal(manifest.records.DrivingGen[1],2026);
console.log('PASS: all 102 PDF release years, all five period filters, timeline new/cumulative counts, and separate publication-year card labels.');
