#!/usr/bin/env node
// Validate joint target/protocol/metric/data filtering against all final task rows.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assets = path.resolve(__dirname, '../docs/assets');
const m = JSON.parse(fs.readFileSync(path.join(assets, 'benchmarks.json'), 'utf8'));
const shards = [1, 2, 3, 4].flatMap(i => JSON.parse(fs.readFileSync(path.join(assets, `benchmarks-${i}.json`), 'utf8')));

class Element {
  constructor() { this.children = []; this.attrs = {}; this.style = {setProperty() {}}; this.handlers = {}; }
  set innerHTML(value) { this.html = value; this.children = []; }
  get innerHTML() { return this.html || ''; }
  append(...values) { this.children.push(...values); }
  setAttribute(key, value) { this.attrs[key] = value; }
  addEventListener(key, value) { this.handlers[key] = value; }
  querySelectorAll() { return []; }
}
const nodes = new Map();
const document = {
  querySelector(key) { if (!nodes.has(key)) nodes.set(key, new Element()); return nodes.get(key); },
  querySelectorAll() { return []; },
  createElement() { return new Element(); },
};
const source = fs.readFileSync(path.join(assets, 'app-v3-core.js'), 'utf8');
const api = vm.runInNewContext(
  source.replace(/\ninit\(\);\s*$/, '\n') + '\n({state,normalizeCorpus,visibleItems,countForValue,renderCards,buildMatrix})',
  {document, location: {search: '', pathname: '/', hash: ''}, URLSearchParams},
);
const plain = value => JSON.parse(JSON.stringify(value));
const names = items => plain(items.map(item => item.shortName)).sort();
api.state.metadata = m;
api.state.benchmarks = api.normalizeCorpus(shards, m);

assert.equal(api.state.benchmarks.length, 102);
assert.equal(m.taskRecords.length, 403);
assert.equal(m.taskRecords.filter(row => !row.auxiliary).length, 401);
assert.equal(m.evaluationRecords.length, 372);
assert.equal(api.state.benchmarks.reduce((count, item) => count + item.evaluationTracks.length, 0), 307);
for (const item of api.state.benchmarks) {
  const exported = shards.find(row => row.shortName === item.shortName);
  assert.deepEqual(plain(item.evaluationTracks), exported.evaluationTracks, item.shortName);
}

const scopeTarget = scope => {
  if (scope.startsWith('T')) return m.targetLabels[scope];
  return m.targetLabels[['S5', 'S6'].includes(scope) ? 'T6' : 'T7'];
};
function wanted(selectedTargets, protocols, metrics, data) {
  return Object.keys(m.records).filter(name => m.evaluationRecords.some(record =>
    record.benchmark === name &&
    (!selectedTargets.length || selectedTargets.includes(scopeTarget(record.scope))) &&
    (!protocols.length || protocols.includes(record.protocol)) &&
    (!metrics.length || metrics.includes(record.metric)) &&
    (!data.length || data.includes(record.data))
  )).sort();
}
function reset() {
  Object.values(api.state.filters).forEach(values => values.clear());
  api.state.search = '';
  api.state.period = null;
}

const targets = Object.values(m.targetLabels);
const targetSelections = [[], ...targets.map(target => [target]), targets];
const protocolSelections = [[], ['OL'], ['CL'], ['OL', 'CL']];
const metricSelections = [[], ['P'], ['O'], ['P', 'O']];
const dataSelections = [[], ['RWD'], ['SBG'], ['SPTC'], ['HCP'], ['RWD', 'HCP']];
let checks = 0;
for (const selected of targetSelections) {
  for (const protocols of protocolSelections) {
    for (const metrics of metricSelections) {
      for (const data of dataSelections) {
        reset();
        selected.forEach(value => api.state.filters.targets.add(value));
        protocols.forEach(value => api.state.filters.protocols.add(value));
        metrics.forEach(value => api.state.filters.metrics.add(value));
        data.forEach(value => api.state.filters.evaluationData.add(value));
        assert.deepEqual(names(api.visibleItems()), wanted(selected, protocols, metrics, data), JSON.stringify({selected, protocols, metrics, data}));
        for (const value of ['P', 'O']) assert.equal(api.countForValue('metrics', value), wanted(selected, protocols, [value], data).length);
        for (const value of ['OL', 'CL']) assert.equal(api.countForValue('protocols', value), wanted(selected, [value], metrics, data).length);
        for (const value of ['RWD', 'SBG', 'SPTC', 'HCP']) assert.equal(api.countForValue('evaluationData', value), wanted(selected, protocols, metrics, [value]).length);
        for (const value of targets) assert.equal(api.countForValue('targets', value), wanted([value], protocols, metrics, data).length);
        checks++;
      }
    }
  }
}

reset();
api.state.filters.targets.add(m.targetLabels.T6);
assert.equal(api.countForValue('protocols', 'CL'), 4);
assert.equal(api.countForValue('metrics', 'O'), 4);

reset();
api.state.filters.targets.add(m.targetLabels.T1);
assert.equal(api.countForValue('metrics', 'O'), 0);

// Joint-filter counterexample from the final checklist: do not form a cross-product.
reset();
api.state.filters.targets.add(m.targetLabels.T4);
api.state.filters.protocols.add('CL');
api.state.filters.metrics.add('O');
api.state.filters.evaluationData.add('RWD');
assert.ok(!names(api.visibleItems()).includes('WorldSimBench'));
api.state.filters.evaluationData.clear();
api.state.filters.evaluationData.add('HCP');
assert.ok(names(api.visibleItems()).includes('WorldSimBench'));

reset();
api.state.filters.targets.add(m.targetLabels.T7);
api.state.filters.protocols.add('CL');
api.state.filters.metrics.add('O');
api.state.filters.evaluationData.add('RWD');
assert.ok(!names(api.visibleItems()).includes('WorldArena 2.0'));
api.state.filters.evaluationData.clear();
api.state.filters.evaluationData.add('HCP');
assert.ok(names(api.visibleItems()).includes('WorldArena 2.0'));

reset();
api.state.filters.targets.add(m.targetLabels.T1);
api.state.search = '4DWorldBench';
assert.equal(api.visibleItems().length, 1); // An unresolved branch is allowed without a Data filter.
api.renderCards(api.visibleItems());
assert.match(nodes.get('#benchmark-grid').children[0].innerHTML, /source unresolved/);
assert.match(nodes.get('#benchmark-grid').children[0].innerHTML, /Evaluation coding by target \/ role/);

reset();
api.buildMatrix();
for (const [id, group, labels] of [['#taxonomy-matrix', 'protocols', m.protocolLabels], ['#metrics-matrix', 'metrics', m.metricLabels]]) {
  const cells = nodes.get(id).children;
  assert.equal(cells.length, 24);
  targets.forEach((target, i) => Object.keys(labels).forEach((value, j) => {
    const count = wanted([target], group === 'protocols' ? [value] : [], group === 'metrics' ? [value] : [], []).length;
    assert.equal(cells[4 + i * 3 + j].attrs['aria-label'], `${target}, ${labels[value]}: ${count} benchmarks`);
  }));
}

console.log(`PASS: 401 task rows, 372 joint combinations, 307 target/role parents, and ${checks} combined-filter cases.`);
console.log('PASS: data filtering is task-aligned; unresolved rows and both anti-cross-product examples behave correctly.');
