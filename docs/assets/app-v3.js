(() => {
  const LABELS = {
    protocol: {
      OL: "Open-Loop Evaluation",
      CL: "Closed-Loop Interaction",
    },
    metrics: {
      P: "Prediction-Level Metrics",
      O: "Downstream Outcome Metrics",
    },
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
    const raw = String(text || "")
      .replace(new RegExp(`^${prefix}\\s*:?\\s*`, "i"), "")
      .trim();
    const expanded = raw
      .split(/\s*[·+]\s*/)
      .filter(Boolean)
      .map((code) => labels[code] || code)
      .join(" · ");
    return expanded ? `${prefix}: ${expanded}` : prefix;
  }

  function loadLatestStyles() {
    if (document.querySelector('link[href$="latest-schema.css"]')) return;
    const link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = new URL("latest-schema.css?v=1", document.currentScript?.src || document.baseURI).href;
    document.head.append(link);
  }

  function rewriteStaticPageCopy() {
    const protocolCaption = document.querySelector(".protocol-node .viz-caption");
    const metricsCaption = document.querySelector(".metrics-node .viz-caption");
    setTextIfChanged(protocolCaption, "open-loop · closed-loop");
    setTextIfChanged(metricsCaption, "prediction-level · downstream");

    const stats = [...document.querySelectorAll(".stat-strip > div")];
    if (stats[0]) {
      setTextIfChanged(stats[0].querySelector("strong"), "95");
      setTextIfChanged(stats[0].querySelector("span"), "representative benchmarks");
    }
    if (stats[1]) {
      setTextIfChanged(stats[1].querySelector("strong"), "58");
      setTextIfChanged(stats[1].querySelector("span"), "cross-category benchmarks");
    }
    if (stats[3]) {
      const strong = stats[3].querySelector("strong");
      const span = stats[3].querySelector("span");
      setTextIfChanged(strong, "2 / 2");
      setTextIfChanged(span, "protocol classes / metric levels");
    }

    const snapshot = document.querySelector(".snapshot-note");
    if (snapshot) {
      snapshot.innerHTML = '<span class="status-dot"></span> Latest manuscript snapshot · 95 benchmarks · 58 cross-category · checked July 30, 2026';
    }

    const cards = [...document.querySelectorAll(".principle-card")];
    if (cards[1]) {
      setTextIfChanged(
        cards[1].querySelector("p"),
        "Distinguishes open-loop evaluation from feedback-driven closed-loop interaction."
      );
    }
    if (cards[2]) {
      setTextIfChanged(
        cards[2].querySelector("p"),
        "Separates prediction-level evidence from downstream outcome evidence."
      );
    }

    const phaseThree = document.querySelector(".timeline-insight:nth-child(3) p");
    if (phaseThree) {
      phaseThree.innerHTML =
        '<strong>31 new benchmarks in 2025</strong>, raising the cumulative corpus to <strong>53</strong>.';
    }

    const phaseFour = document.querySelector(".timeline-insight:nth-child(4) p");
    if (phaseFour) {
      phaseFour.innerHTML =
        '<strong>42 new benchmarks in 2026</strong>, bringing the corpus to <strong>95</strong>.';
    }

    const benchmarkSummary = document.querySelector("#benchmarks .benchmark-heading > p");
    if (benchmarkSummary) {
      benchmarkSummary.textContent =
        "Search and filter the 95 representative benchmarks coded in Figure 4 and Tables 3–9 of the latest manuscript.";
    }

    const resultCount = document.querySelector("#result-count");
    if (resultCount && resultCount.textContent !== "95") resultCount.textContent = "95";

    const communityMetricCopy = [...document.querySelectorAll(".community-grid article p")]
      .find((node) => node.textContent.includes("metric family"));
    if (communityMetricCopy) {
      communityMetricCopy.textContent = communityMetricCopy.textContent.replace(
        "metric family",
        "metric level"
      );
    }

    const chart = document.querySelector("#timeline-chart");
    if (chart) chart.setAttribute("aria-label", "Unique benchmark totals by release window");
    const clearPeriod = document.querySelector("#clear-year");
    if (clearPeriod) setTextIfChanged(clearPeriod, "Clear period filter");
  }

  function updateCard(card) {
    const pills = [...card.querySelectorAll(".card-meta .meta-pill")];
    if (pills[1]) {
      setTextIfChanged(pills[1], expandCodes(pills[1].textContent, "Protocol", LABELS.protocol));
    }
    if (pills[2]) {
      setTextIfChanged(pills[2], expandCodes(pills[2].textContent, "Metrics", LABELS.metrics));
    }
    if (pills[3]) {
      setTextIfChanged(pills[3], expandCodes(pills[3].textContent, "Data", LABELS.data));
    }

    const footerLabel = card.querySelector(".card-footer small");
    if (footerLabel) {
      const cleaned = footerLabel.textContent
        .replace(/^Ref\.\s*\[\d+\]\s*·\s*/i, "")
        .trim();
      if (cleaned) setTextIfChanged(footerLabel, cleaned);
      else footerLabel.remove();
    }
  }

  function updateCards(root = document) {
    root.querySelectorAll(".benchmark-card").forEach(updateCard);
  }

  async function loadCanonicalExplorer() {
    const sourceUrl = new URL("app-v3-core.js?v=9", document.currentScript?.src || document.baseURI);
    const response = await fetch(sourceUrl, { cache: "no-store" });
    if (!response.ok) throw new Error(`HTTP ${response.status} while loading explorer core`);

    let source = await response.text();
    source = source
      .replace(
        'const PROTOCOLS = ["OL", "CR", "CL"];',
        'const PROTOCOLS = ["OL", "CL"];'
      )
      .replace(
        'const METRICS = ["A", "J", "O"];',
        'const METRICS = ["P", "O"];'
      );

    if (source.includes('const PROTOCOLS = ["OL", "CR", "CL"];') ||
        source.includes('const METRICS = ["A", "J", "O"];')) {
      throw new Error("Explorer core taxonomy patch did not apply");
    }

    new Function(source)();
  }

  loadLatestStyles();
  rewriteStaticPageCopy();

  const grid = document.querySelector("#benchmark-grid");
  if (grid) {
    new MutationObserver(() => updateCards(grid)).observe(grid, {
      childList: true,
      subtree: true,
    });
  }

  loadCanonicalExplorer()
    .then(() => {
      rewriteStaticPageCopy();
      updateCards();
    })
    .catch((error) => {
      console.error(error);
      if (grid) {
        grid.innerHTML =
          `<div class="empty-state"><h3>Benchmark data could not be loaded.</h3>` +
          `<p>${String(error.message || error)}</p></div>`;
      }
    });
})();
