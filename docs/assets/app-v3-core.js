const TARGETS = [
  "Visual & Temporal Quality",
  "Spatial & State Consistency",
  "Long-Horizon Memory & State Persistence",
  "Physical Plausibility",
  "Causal & Counterfactual Reasoning",
  "Control Fidelity & Interactive Dynamics",
  "Functional Utility",
];
const PROTOCOLS = ["OL", "CL"];
const METRICS = ["P", "O"];
const EVALUATION_DATA = ["RWD", "SBG", "SPTC", "HCP"];
const TARGET_COLORS = {
  "Visual & Temporal Quality": "#6f63d9",
  "Spatial & State Consistency": "#2f88b7",
  "Long-Horizon Memory & State Persistence": "#4d998f",
  "Physical Plausibility": "#d05f68",
  "Causal & Counterfactual Reasoning": "#c25b87",
  "Control Fidelity & Interactive Dynamics": "#d5783b",
  "Functional Utility": "#45a15a",
};

const state = {
  benchmarks: [],
  metadata: null,
  search: "",
  sort: "recent",
  period: null,
  filters: {
    targets: new Set(),
    protocols: new Set(),
    metrics: new Set(),
    domains: new Set(),
    evaluationData: new Set(),
  },
};

const $ = (selector, root = document) => root.querySelector(selector);
const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];
const splitCodes = (value) => String(value || "").split("+").filter(Boolean);
const escapeHtml = (value) => String(value ?? "")
  .replace(/&/g, "&amp;")
  .replace(/</g, "&lt;")
  .replace(/>/g, "&gt;")
  .replace(/"/g, "&quot;")
  .replace(/'/g, "&#39;");

const els = {
  grid: $("#benchmark-grid"),
  search: $("#benchmark-search"),
  searchClear: $("#search-clear"),
  sort: $("#benchmark-sort"),
  resultCount: $("#result-count"),
  empty: $("#empty-state"),
  emptyClear: $("#empty-clear"),
  activeFilters: $("#active-filters"),
  clearFilters: $("#clear-filters"),
  filterLabel: $("#filter-count-label"),
  openFilters: $("#open-filters"),
  closeFilters: $("#close-filters"),
  filterBackdrop: $("#filter-backdrop"),
  mobileFilterCount: $("#mobile-filter-count"),
  targetShortcuts: $("#target-shortcuts"),
  protocolShortcuts: $("#protocol-shortcuts"),
  metricsShortcuts: $("#metrics-shortcuts"),
  dataShortcuts: $("#data-shortcuts"),
  matrix: $("#taxonomy-matrix"),
  timeline: $("#timeline-chart"),
  timelineTargetMatrix: $("#timeline-target-matrix"),
  clearPeriod: $("#clear-year"),
  copyCitation: $("#copy-citation"),
  citation: $("#citation-code"),
  downloadJson: $("#download-json"),
};

function prettyDomain(value) {
  const labels = { video: "Video", image: "Image", embodied: "Embodied", driving: "Driving", game: "Game" };
  return labels[value] || value.replace(/\b\w/g, (character) => character.toUpperCase());
}

function targetShortLabel(target) {
  return target === "Long-Horizon Memory & State Persistence"
    ? "Long-Horizon Memory & Persistence"
    : target;
}

function groupLabel(group, value) {
  if (group === "protocols") return state.metadata.protocolLabels[value] || value;
  if (group === "metrics") return state.metadata.metricLabels[value] || value;
  if (group === "evaluationData") return state.metadata.dataLabels[value] || value;
  if (group === "domains") return prettyDomain(value);
  return targetShortLabel(value);
}

function decodeRecord(raw, manifest) {
  const original = raw.shortName;
  const canonical = manifest.aliases?.[original] || original;
  if (manifest.removed.includes(original) || manifest.removed.includes(canonical)) return null;
  const row = manifest.records[canonical];
  if (!row) return null;

  const [ref, year, domain, protocols, metrics, data, targetCodes, subtargetCodes] = row;
  const targets = splitCodes(targetCodes).map((code) => manifest.targetLabels[code]);
  const subtargets = splitCodes(subtargetCodes).map((code) => manifest.subtargetLabels[code]);

  return {
    ...raw,
    shortName: canonical,
    ref,
    year,
    domains: splitCodes(domain),
    protocols: splitCodes(protocols),
    metrics: splitCodes(metrics),
    evaluationData: splitCodes(data),
    targets,
    subtargets,
    crossCategory: targets.length > 1,
  };
}

function buildAddedRecord(name, manifest) {
  const row = manifest.records[name];
  const base = manifest.added?.[name];
  if (!row || !base) return null;
  const [ref, year, domain, protocols, metrics, data, targetCodes, subtargetCodes] = row;
  const targets = splitCodes(targetCodes).map((code) => manifest.targetLabels[code]);
  return {
    ...base,
    ref,
    year,
    domains: splitCodes(domain),
    protocols: splitCodes(protocols),
    metrics: splitCodes(metrics),
    evaluationData: splitCodes(data),
    targets,
    subtargets: splitCodes(subtargetCodes).map((code) => manifest.subtargetLabels[code]),
    crossCategory: targets.length > 1,
  };
}

function normalizeCorpus(rawRecords, manifest) {
  const byName = new Map();
  rawRecords.forEach((raw) => {
    const record = decodeRecord(raw, manifest);
    if (record) byName.set(record.shortName, record);
  });
  Object.keys(manifest.added || {}).forEach((name) => {
    if (!byName.has(name)) {
      const record = buildAddedRecord(name, manifest);
      if (record) byName.set(name, record);
    }
  });

  const missing = Object.keys(manifest.records).filter((name) => !byName.has(name));
  if (missing.length) throw new Error(`Missing latest-paper records: ${missing.join(", ")}`);

  const corpus = [...byName.values()];
  const crossCount = corpus.filter((item) => item.crossCategory).length;
  if (corpus.length !== manifest.total || crossCount !== manifest.crossCategory) {
    throw new Error(`Corpus validation failed: ${corpus.length}/${manifest.total} records, ${crossCount}/${manifest.crossCategory} cross-category`);
  }
  return corpus;
}

function normalizedSearchText(item) {
  return [
    item.shortName,
    item.title,
    item.venue,
    item.domains.join(" "),
    item.targets.join(" "),
    item.subtargets.join(" "),
    item.protocols.join(" "),
    item.metrics.join(" "),
    item.evaluationData.join(" "),
  ].join(" ").toLowerCase();
}

function matchesSearch(item) {
  if (!state.search) return true;
  const terms = state.search.toLowerCase().trim().split(/\s+/).filter(Boolean);
  const haystack = normalizedSearchText(item);
  return terms.every((term) => haystack.includes(term));
}

function periodYears() {
  if (!state.period) return null;
  return state.metadata.timelineBins.find((bin) => bin.label === state.period)?.years || null;
}

function matchesPeriod(item) {
  const years = periodYears();
  return !years || years.includes(item.year);
}

function matchesGroup(item, group, ignoredGroup = null) {
  if (group === ignoredGroup) return true;
  const active = state.filters[group];
  if (!active.size) return true;
  return item[group].some((value) => active.has(value));
}

function matchesItem(item, ignoredGroup = null) {
  if (!matchesSearch(item) || !matchesPeriod(item)) return false;
  return Object.keys(state.filters).every((group) => matchesGroup(item, group, ignoredGroup));
}

function visibleItems() {
  const items = state.benchmarks.filter((item) => matchesItem(item));
  if (state.sort === "oldest") {
    items.sort((a, b) => a.year - b.year || a.shortName.localeCompare(b.shortName));
  } else if (state.sort === "title") {
    items.sort((a, b) => a.shortName.localeCompare(b.shortName));
  } else {
    items.sort((a, b) => b.year - a.year || a.shortName.localeCompare(b.shortName));
  }
  return items;
}

function countForValue(group, value) {
  return state.benchmarks.filter((item) => {
    if (!matchesSearch(item) || !matchesPeriod(item)) return false;
    if (!Object.keys(state.filters).every((key) => matchesGroup(item, key, group))) return false;
    return item[group].includes(value);
  }).length;
}

function uniqueValues(group) {
  if (group === "targets") return TARGETS;
  if (group === "protocols") return PROTOCOLS;
  if (group === "metrics") return METRICS;
  if (group === "evaluationData") return EVALUATION_DATA;
  return [...new Set(state.benchmarks.flatMap((item) => item[group]))]
    .sort((a, b) => groupLabel(group, a).localeCompare(groupLabel(group, b)));
}

function activeFilterCount() {
  return Object.values(state.filters).reduce((sum, values) => sum + values.size, 0) + (state.period ? 1 : 0);
}

function updateUrl() {
  const params = new URLSearchParams();
  if (state.search) params.set("q", state.search);
  if (state.period) params.set("period", state.period);
  const keys = { targets: "target", protocols: "protocol", metrics: "metric", domains: "domain", evaluationData: "data" };
  Object.entries(keys).forEach(([group, key]) => {
    if (state.filters[group].size) params.set(key, [...state.filters[group]].join("|"));
  });
  const query = params.toString();
  history.replaceState(null, "", `${location.pathname}${query ? `?${query}` : ""}${location.hash}`);
}

function readUrl() {
  const params = new URLSearchParams(location.search);
  state.search = params.get("q") || "";
  state.period = params.get("period") || null;
  const keys = { targets: "target", protocols: "protocol", metrics: "metric", domains: "domain", evaluationData: "data" };
  Object.entries(keys).forEach(([group, key]) => {
    const value = params.get(key);
    if (value) value.split("|").filter(Boolean).forEach((part) => state.filters[group].add(part));
  });
  els.search.value = state.search;
  els.searchClear.hidden = !state.search;
}

function toggleFilter(group, value, force = null) {
  const values = state.filters[group];
  const shouldAdd = force == null ? !values.has(value) : force;
  if (shouldAdd) values.add(value);
  else values.delete(value);
  updateUrl();
  renderAll();
}

function clearAll() {
  state.search = "";
  state.period = null;
  Object.values(state.filters).forEach((values) => values.clear());
  els.search.value = "";
  els.searchClear.hidden = true;
  updateUrl();
  renderAll();
}

function setFocusedFilters(target = null, protocol = null) {
  Object.values(state.filters).forEach((values) => values.clear());
  state.period = null;
  if (target) state.filters.targets.add(target);
  if (protocol) state.filters.protocols.add(protocol);
  updateUrl();
  renderAll();
  $("#benchmarks").scrollIntoView({ behavior: "smooth", block: "start" });
}

function buildFilters() {
  Object.keys(state.filters).forEach((group) => {
    const container = document.querySelector(`[data-filter-group="${group}"]`);
    container.innerHTML = "";
    uniqueValues(group).forEach((value) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "filter-option";
      button.dataset.group = group;
      button.dataset.value = value;
      button.setAttribute("aria-pressed", "false");
      button.innerHTML = `<span class="filter-check" aria-hidden="true"></span><span class="filter-text">${escapeHtml(groupLabel(group, value))}</span><span class="filter-number">0</span>`;
      button.addEventListener("click", () => toggleFilter(group, value));
      container.append(button);
    });
  });
}

function updateFilters() {
  Object.keys(state.filters).forEach((group) => {
    const container = document.querySelector(`[data-filter-group="${group}"]`);
    $$(".filter-option", container).forEach((button) => {
      const value = button.dataset.value;
      const count = countForValue(group, value);
      const active = state.filters[group].has(value);
      button.setAttribute("aria-pressed", String(active));
      $(".filter-number", button).textContent = count;
      button.disabled = count === 0 && !active;
    });
  });
  const count = activeFilterCount();
  els.mobileFilterCount.textContent = count;
  els.filterLabel.textContent = count ? `${count} active filter${count === 1 ? "" : "s"}` : "All benchmarks";
}

function addActiveChip(prefix, label, onClick) {
  const button = document.createElement("button");
  button.type = "button";
  button.className = "active-chip";
  button.innerHTML = `${prefix ? `<b>${escapeHtml(prefix)}:</b> ` : ""}${escapeHtml(label)} <span aria-hidden="true">×</span>`;
  button.addEventListener("click", onClick);
  els.activeFilters.append(button);
}

function renderActiveFilters() {
  els.activeFilters.innerHTML = "";
  if (state.search) addActiveChip("Search", state.search, () => {
    state.search = "";
    els.search.value = "";
    els.searchClear.hidden = true;
    updateUrl();
    renderAll();
  });
  if (state.period) addActiveChip("Period", state.period, () => {
    state.period = null;
    updateUrl();
    renderAll();
  });
  Object.entries(state.filters).forEach(([group, values]) => {
    [...values].forEach((value) => addActiveChip(null, groupLabel(group, value), () => toggleFilter(group, value, false)));
  });
}

function buildShortcuts() {
  const groups = [
    [els.targetShortcuts, TARGETS, "targets"],
    [els.protocolShortcuts, PROTOCOLS, "protocols"],
    [els.metricsShortcuts, METRICS, "metrics"],
    [els.dataShortcuts, EVALUATION_DATA, "evaluationData"],
  ];
  groups.forEach(([container, values, group]) => {
    container.innerHTML = "";
    values.forEach((value, index) => {
      const count = state.benchmarks.filter((item) => item[group].includes(value)).length;
      const button = document.createElement("button");
      button.type = "button";
      button.className = "taxonomy-option";
      const label = group === "targets" ? targetShortLabel(value) : groupLabel(group, value);
      button.innerHTML = `<span>${group === "targets" ? `${index + 1}. ` : ""}${escapeHtml(label)}</span><span>${count}</span>`;
      button.addEventListener("click", () => {
        Object.values(state.filters).forEach((selected) => selected.clear());
        state.period = null;
        state.filters[group].add(value);
        updateUrl();
        renderAll();
        $("#benchmarks").scrollIntoView({ behavior: "smooth" });
      });
      container.append(button);
    });
  });
}

function createMatrixHead(text) {
  const head = document.createElement("div");
  head.className = "matrix-head";
  head.textContent = text;
  return head;
}

function buildMatrix() {
  els.matrix.innerHTML = "";
  els.matrix.append(createMatrixHead("Evaluation target"));
  PROTOCOLS.forEach((protocol) => els.matrix.append(createMatrixHead(state.metadata.protocolLabels[protocol])));
  const allCounts = TARGETS.flatMap((target) => PROTOCOLS.map((protocol) =>
    state.benchmarks.filter((item) => item.targets.includes(target) && item.protocols.includes(protocol)).length
  ));
  const max = Math.max(...allCounts, 1);
  TARGETS.forEach((target) => {
    const label = document.createElement("div");
    label.className = "matrix-row-label";
    label.textContent = targetShortLabel(target);
    els.matrix.append(label);
    PROTOCOLS.forEach((protocol) => {
      const count = state.benchmarks.filter((item) => item.targets.includes(target) && item.protocols.includes(protocol)).length;
      const button = document.createElement("button");
      button.type = "button";
      button.className = "matrix-cell";
      button.style.setProperty("--heat", Math.round((count / max) * 100));
      button.setAttribute("aria-label", `${target}, ${state.metadata.protocolLabels[protocol]}: ${count} benchmarks`);
      button.innerHTML = `<strong>${count}</strong><small>benchmarks</small>`;
      button.addEventListener("click", () => setFocusedFilters(target, protocol));
      els.matrix.append(button);
    });
  });
}

function buildTimeline() {
  els.timeline.innerHTML = "";
  const counts = state.metadata.timelineBins.map((bin) =>
    state.benchmarks.filter((item) => bin.years.includes(item.year)).length
  );
  const max = Math.max(...counts, 1);
  let cumulative = 0;
  state.metadata.timelineBins.forEach((bin, index) => {
    cumulative += counts[index];
    const column = document.createElement("div");
    column.className = "year-column";
    const area = document.createElement("div");
    area.className = "year-bar-area";
    const bar = document.createElement("button");
    bar.type = "button";
    bar.className = "year-bar";
    bar.style.setProperty("--height", Math.max(5, Math.round((counts[index] / max) * 100)));
    bar.setAttribute("aria-pressed", String(state.period === bin.label));
    bar.setAttribute("aria-label", `${bin.label}: ${counts[index]} new benchmarks, ${cumulative} cumulative`);
    bar.innerHTML = `<span class="year-count">${counts[index]}</span>`;
    bar.addEventListener("click", () => {
      state.period = state.period === bin.label ? null : bin.label;
      updateUrl();
      renderAll();
      $("#benchmarks").scrollIntoView({ behavior: "smooth" });
    });
    area.append(bar);
    const label = document.createElement("div");
    label.className = "year-label";
    label.innerHTML = `<strong>${escapeHtml(bin.label)}</strong><small>${cumulative} cumulative</small>`;
    column.append(area, label);
    els.timeline.append(column);
  });
  els.clearPeriod.hidden = !state.period;
  buildTimelineTargetMatrix();
}

function focusTimelineTarget(target, period = null) {
  Object.values(state.filters).forEach((values) => values.clear());
  state.period = period;
  state.filters.targets.add(target);
  updateUrl();
  renderAll();
  $("#benchmarks").scrollIntoView({ behavior: "smooth", block: "start" });
}

function buildTimelineTargetMatrix() {
  if (!els.timelineTargetMatrix) return;

  const bins = state.metadata.timelineBins;
  const counts = TARGETS.flatMap((target) => bins.map((bin) =>
    state.benchmarks.filter((item) => bin.years.includes(item.year) && item.targets.includes(target)).length
  ));
  const max = Math.max(...counts, 1);

  const head = bins.map((bin) => `<th scope="col">${escapeHtml(bin.label)}</th>`).join("");
  const rows = TARGETS.map((target) => {
    const color = TARGET_COLORS[target] || "#6f63d9";
    const cells = bins.map((bin) => {
      const count = state.benchmarks.filter((item) =>
        bin.years.includes(item.year) && item.targets.includes(target)
      ).length;
      const active = state.period === bin.label && state.filters.targets.has(target);
      return `<td><button type="button" class="timeline-target-cell" data-target="${escapeHtml(target)}" data-period="${escapeHtml(bin.label)}" style="--target-color:${color};--cell-opacity:${(0.04 + (count / max) * 0.32).toFixed(3)}" aria-label="${escapeHtml(target)}, ${escapeHtml(bin.label)}: ${count} benchmarks" aria-pressed="${active}" ${count === 0 ? "disabled" : ""}><strong>${count}</strong></button></td>`;
    }).join("");
    const active = state.filters.targets.has(target) && !state.period;
    return `<tr><th scope="row"><button type="button" class="timeline-target-row-button" data-target="${escapeHtml(target)}" style="--target-color:${color}" aria-pressed="${active}"><span class="timeline-target-dot" aria-hidden="true"></span><span>${escapeHtml(targetShortLabel(target))}</span></button></th>${cells}</tr>`;
  }).join("");

  els.timelineTargetMatrix.innerHTML = `
    <table class="timeline-target-matrix">
      <caption class="sr-only">Benchmark counts for each evaluation target and release window. Counts overlap for cross-category benchmarks.</caption>
      <thead><tr><th scope="col">Evaluation target</th>${head}</tr></thead>
      <tbody>${rows}</tbody>
    </table>`;

  $$(".timeline-target-row-button", els.timelineTargetMatrix).forEach((button) => {
    button.addEventListener("click", () => focusTimelineTarget(button.dataset.target));
  });
  $$(".timeline-target-cell", els.timelineTargetMatrix).forEach((button) => {
    button.addEventListener("click", () => focusTimelineTarget(button.dataset.target, button.dataset.period));
  });
}

function renderCards(items) {
  els.grid.innerHTML = "";
  items.forEach((item) => {
    const card = document.createElement("article");
    card.className = "benchmark-card";
    card.style.setProperty("--card-accent", TARGET_COLORS[item.targets[0]] || "#6f63d9");
    const targetPills = item.targets.map((target) => `<span class="target-pill">${escapeHtml(targetShortLabel(target))}</span>`).join("");
    const subtarget = item.subtargets.length ? item.subtargets.join(" · ") : "Top-level target coding";
    const venue = item.venue || "Publication";
    const paperUrl = item.paperUrl || "#";
    card.innerHTML = `
      <div class="card-topline">
        <span class="card-year">${item.year} · ${escapeHtml(venue)}</span>
        ${item.crossCategory ? '<span class="cross-badge">△ Cross-category</span>' : ""}
      </div>
      <h3>${escapeHtml(item.shortName)}</h3>
      <p class="paper-title">${escapeHtml(String(item.title || item.shortName).replace(/[,.]+$/, ""))}</p>
      <div class="card-meta">
        <span class="meta-pill">${item.domains.map(prettyDomain).join(" + ")}</span>
        <span class="meta-pill">Protocol ${escapeHtml(item.protocols.join(" · "))}</span>
        <span class="meta-pill">Metrics ${escapeHtml(item.metrics.join(" · "))}</span>
        <span class="meta-pill">Data ${escapeHtml(item.evaluationData.join(" · "))}</span>
      </div>
      <div class="card-targets">${targetPills}</div>
      <div class="card-footer">
        <small>Ref. [${item.ref}] · ${escapeHtml(subtarget)}</small>
        <a class="paper-link" href="${escapeHtml(paperUrl)}" target="_blank" rel="noreferrer">Paper <span aria-hidden="true">↗</span></a>
      </div>`;
    els.grid.append(card);
  });
}

function renderAll() {
  const items = visibleItems();
  els.resultCount.textContent = items.length;
  $("#stat-total").textContent = state.metadata.total;
  $("#stat-cross").textContent = state.metadata.crossCategory;
  els.empty.hidden = items.length !== 0;
  els.grid.hidden = items.length === 0;
  renderCards(items);
  updateFilters();
  renderActiveFilters();
  buildTimeline();
}

function openFilters() {
  document.body.classList.add("filters-open");
  els.filterBackdrop.hidden = false;
  setTimeout(() => els.closeFilters.focus(), 50);
}

function closeFilters() {
  document.body.classList.remove("filters-open");
  els.filterBackdrop.hidden = true;
}

function setupEvents() {
  let searchTimer = null;
  els.search.addEventListener("input", () => {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(() => {
      state.search = els.search.value.trim();
      els.searchClear.hidden = !state.search;
      updateUrl();
      renderAll();
    }, 120);
  });
  els.searchClear.addEventListener("click", () => {
    state.search = "";
    els.search.value = "";
    els.searchClear.hidden = true;
    updateUrl();
    renderAll();
    els.search.focus();
  });
  els.sort.addEventListener("change", () => {
    state.sort = els.sort.value;
    renderAll();
  });
  els.clearFilters.addEventListener("click", clearAll);
  els.emptyClear.addEventListener("click", clearAll);
  els.openFilters.addEventListener("click", openFilters);
  els.closeFilters.addEventListener("click", closeFilters);
  els.filterBackdrop.addEventListener("click", closeFilters);
  els.clearPeriod.addEventListener("click", () => {
    state.period = null;
    updateUrl();
    renderAll();
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && document.body.classList.contains("filters-open")) closeFilters();
  });
  $$(".taxonomy-jump").forEach((button) => {
    button.addEventListener("click", () =>
      document.getElementById(button.dataset.scrollTarget)?.scrollIntoView({ behavior: "smooth", block: "center" })
    );
  });
  els.copyCitation.addEventListener("click", async () => {
    const text = els.citation.innerText;
    try {
      await navigator.clipboard.writeText(text);
      const previous = els.copyCitation.textContent;
      els.copyCitation.textContent = "Copied";
      setTimeout(() => { els.copyCitation.textContent = previous; }, 1400);
    } catch {
      window.prompt("Copy this BibTeX:", text);
    }
  });
  els.downloadJson.addEventListener("click", () => {
    const payload = JSON.stringify({ metadata: state.metadata, benchmarks: state.benchmarks }, null, 2);
    const url = URL.createObjectURL(new Blob([payload], { type: "application/json" }));
    const link = document.createElement("a");
    link.href = url;
    link.download = "world-model-benchmarks-2026-08-31.json";
    document.body.append(link);
    link.click();
    link.remove();
    URL.revokeObjectURL(url);
  });
}

function setupNavObserver() {
  const links = $$(".primary-nav a");
  const sections = links.map((link) => document.querySelector(link.getAttribute("href"))).filter(Boolean);
  const observer = new IntersectionObserver((entries) => {
    const visible = entries.filter((entry) => entry.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
    if (!visible) return;
    links.forEach((link) => link.removeAttribute("aria-current"));
    links.find((link) => link.getAttribute("href") === `#${visible.target.id}`)?.setAttribute("aria-current", "true");
  }, { rootMargin: "-25% 0px -65%", threshold: [0, .15, .4] });
  sections.forEach((section) => observer.observe(section));
}

async function init() {
  try {
    const shardUrls = [1, 2, 3, 4].map((index) => `assets/benchmarks-${index}.json`);
    const responses = await Promise.all([...shardUrls, "assets/benchmarks.json"].map((url) => fetch(url, { cache: "no-store" })));
    const failed = responses.find((response) => !response.ok);
    if (failed) throw new Error(`HTTP ${failed.status} while loading benchmark data`);
    const decoded = await Promise.all(responses.map((response) => response.json()));
    const manifest = decoded.at(-1);
    state.metadata = {
      ...manifest,
      dimensions: 4,
      yearMin: 2018,
      yearMax: 2026,
      targets: TARGETS,
    };
    state.benchmarks = normalizeCorpus(decoded.slice(0, 4).flat(), manifest);
    readUrl();
    buildFilters();
    buildShortcuts();
    buildMatrix();
    setupEvents();
    setupNavObserver();
    renderAll();
  } catch (error) {
    console.error(error);
    els.grid.innerHTML = `<div class="empty-state"><h3>Benchmark data could not be loaded.</h3><p>${escapeHtml(error.message)}</p></div>`;
  }
}

init();
