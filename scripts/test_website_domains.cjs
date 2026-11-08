#!/usr/bin/env node
// Final manuscript domain tests, including compatibility with legacy Image URLs.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const assets = path.resolve(__dirname, '../docs/assets');
const source = fs.readFileSync(path.join(assets, 'app-v3-core.js'), 'utf8');
assert.match(source, /\ninit\(\);\s*$/);
const document = { querySelector: () => ({}), querySelectorAll: () => [] };
const location = { search: '', pathname: '/', hash: '' };
const api = vm.runInNewContext(
  source.replace(/\ninit\(\);\s*$/, '\n') +
  '\n({state, normalizeCorpus, buildAddedRecord, uniqueValues, countForValue, visibleItems, readUrl})',
  { document, location, URLSearchParams },
);
const plain = value => JSON.parse(JSON.stringify(value));
const manifest = JSON.parse(fs.readFileSync(path.join(assets, 'benchmarks.json'), 'utf8'));
const shards = [1, 2, 3, 4].flatMap(i => JSON.parse(fs.readFileSync(path.join(assets, `benchmarks-${i}.json`), 'utf8')));
const before = JSON.stringify({manifest, shards});
const corpus = api.normalizeCorpus(shards, manifest);
api.state.benchmarks = corpus;
api.state.metadata = manifest;

assert.equal(corpus.length, 130);
assert.equal(corpus.filter(item => item.crossCategory).length, 108);
assert.deepEqual(plain(api.uniqueValues('domains')), ['driving', 'embodied', 'game', 'video']);
const counts = Object.fromEntries(api.uniqueValues('domains').map(domain => [domain, api.countForValue('domains', domain)]));
assert.deepEqual(counts, {driving: 10, embodied: 35, game: 12, video: 86});
assert.equal(api.countForValue('domains', 'image'), 0);

// Check all eight manuscript-coded fields directly against the final manifest.
for (const item of corpus) {
  const row = manifest.records[item.shortName];
  assert.deepEqual(plain([
    item.ref, item.year, item.domains, item.protocols, item.metrics, item.evaluationData,
    item.targets, item.subtargets,
  ]), [
    row[0], row[1], row[2].split('+'), row[3].split('+'), row[4].split('+'), row[5].split('+'),
    row[6].split('+').filter(Boolean).map(code => manifest.targetLabels[code]),
    row[7].split('+').filter(Boolean).map(code => manifest.subtargetLabels[code]),
  ], item.shortName);
}

api.state.filters.domains.add('video');
assert.equal(api.visibleItems().length, 86);
assert.ok(api.visibleItems().some(item => item.shortName === 'CausalSpatial'));
api.state.search = 'CausalSpatial';
assert.deepEqual(plain(api.visibleItems().map(item => item.shortName)), ['CausalSpatial']);
api.state.search = '';
api.state.filters.domains.clear();

// Old Image filter bookmarks become Video selections, without an orphan filter.
location.search = '?domain=image%7Cvideo';
api.readUrl();
assert.deepEqual([...api.state.filters.domains], ['video']);
assert.equal(api.visibleItems().length, 86);
api.state.filters.domains.clear();

// The added-record path uses the same final coding and never mutates inputs.
const added = {...manifest, added: {CausalSpatial: {shortName: 'CausalSpatial'}}};
assert.deepEqual(plain(api.buildAddedRecord('CausalSpatial', added).domains), ['video']);
assert.equal(manifest.records.CausalSpatial[2], 'video');
assert.equal(JSON.stringify({manifest, shards}), before);
console.log('PASS: website domains Driving=10, Embodied=35, Game=12, Video=86; Image absent.');
console.log('PASS: CausalSpatial is included by Video; 130 benchmarks / 108 cross-category unchanged.');
console.log('PASS: CausalSpatial raw and exported domains are both Video; legacy Image URLs remain compatible.');
