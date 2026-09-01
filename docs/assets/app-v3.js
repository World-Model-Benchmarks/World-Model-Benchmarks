(() => {
  const LABELS = {
    protocol: { OL: "Open-Loop Evaluation", CL: "Closed-Loop Interaction" },
    metrics: { P: "Prediction-Level Metrics", O: "Downstream Outcome Metrics" },
    data: {
      RWD: "Real-World Data Collection",
      SBG: "Simulation-Based Generation",
      SPTC: "Scenario, Prompt, and Task Curation",
      HCP: "Hybrid Construction Pipelines",
    },
  };

  function setTextIfChanged(element, nextText) {
    if (element && element.textContent !== nextText) element.textContent = nextText;
  }

  function expandCodes(text, prefix, labels) {
    const raw = String(text || "").replace(new RegExp(`^${prefix}\\s*:?\\s*`, "i"), "").trim();
    const expanded = raw.split(/\s*[·+]\s*/).filter(Boolean).map((code) => labels[code] || code).join(" · ");
    return expanded ? `${prefix}: ${expanded}` : prefix;
  }

  function loadLatestStyles() {
    if (document.querySelector('link[href*="latest-schema.css"]')) return;
    const link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = new URL("latest-schema.css?v=2", document.currentScript?.src || document.baseURI).href;
    document.head.append(link);
  }

  function rewriteStaticPageCopy() {
    setTextIfChanged(document.querySelector(".protocol-node .viz-caption"), "open-loop · closed-loop");
    setTextIfChanged(document.querySelector(".metrics-node .viz-caption"), "prediction-level · downstream");

    const stats = [...document.querySelectorAll(".stat-strip > div")];
    if (stats[0]) {
      setTextIfChanged(stats[0].querySelector("strong"), "102");
      setTextIfChanged(stats[0].querySelector("span"), "representative benchmarks");
    }
    if (stats[1]) {
      setTextIfChanged(stats[1].querySelector("strong"), "85");
      setTextIfChanged(stats[1].querySelector("span"), "cross-category benchmarks");
    }
    if (stats[3]) {
      setTextIfChanged(stats[3].querySelector("strong"), "2 / 2");
      setTextIfChanged(stats[3].querySelector("span"), "protocol classes / metric levels");
    }

    const snapshot = document.querySelector(".snapshot-note");
    if (snapshot) snapshot.innerHTML = '<span class="status-dot"></span> Latest manuscript snapshot · 102 benchmarks · 85 cross-category · checked August 31, 2026';

    const benchmarkSummary = document.querySelector("#benchmarks .benchmark-heading > p");
    if (benchmarkSummary) benchmarkSummary.textContent = "Search and filter the 102 representative benchmarks coded in Figure 4 and Tables 3–9 of the latest manuscript.";

    const resultCount = document.querySelector("#result-count");
    if (resultCount && resultCount.textContent !== "102") resultCount.textContent = "102";
    const chart = document.querySelector("#timeline-chart");
    if (chart) chart.setAttribute("aria-label", "Unique benchmark totals by release window");
    const clearPeriod = document.querySelector("#clear-year");
    if (clearPeriod) setTextIfChanged(clearPeriod, "Clear period filter");
  }

  function updateCard(card) {
    const pills = [...card.querySelectorAll(".card-meta .meta-pill")];
    if (pills[1]) setTextIfChanged(pills[1], expandCodes(pills[1].textContent, "Protocol", LABELS.protocol));
    if (pills[2]) setTextIfChanged(pills[2], expandCodes(pills[2].textContent, "Metrics", LABELS.metrics));
    if (pills[3]) setTextIfChanged(pills[3], expandCodes(pills[3].textContent, "Data", LABELS.data));

    const footerLabel = card.querySelector(".card-footer small");
    if (footerLabel) {
      const cleaned = footerLabel.textContent.replace(/^Ref\.\s*\[\d+\]\s*·\s*/i, "").trim();
      if (cleaned) setTextIfChanged(footerLabel, cleaned);
      else footerLabel.remove();
    }
  }

  function updateCards(root = document) {
    root.querySelectorAll(".benchmark-card").forEach(updateCard);
  }

  async function loadCanonicalExplorer() {
    const sourceUrl = new URL("app-v3-core.js?v=12", document.currentScript?.src || document.baseURI);
    const response = await fetch(sourceUrl, { cache: "no-store" });
    if (!response.ok) throw new Error(`HTTP ${response.status} while loading explorer core`);
    new Function(await response.text())();
  }

  loadLatestStyles();
  rewriteStaticPageCopy();
  const grid = document.querySelector("#benchmark-grid");
  if (grid) new MutationObserver(() => updateCards(grid)).observe(grid, { childList: true, subtree: true });

  loadCanonicalExplorer().then(() => {
    rewriteStaticPageCopy();
    updateCards();
  }).catch((error) => {
    console.error(error);
    if (grid) grid.innerHTML = `<div class="empty-state"><h3>Benchmark data could not be loaded.</h3><p>${String(error.message || error)}</p></div>`;
  });
})();
