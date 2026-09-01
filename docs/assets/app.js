(() => {
  const script = document.createElement("script");
  script.src = "assets/app-v3.js?v=9";
  script.defer = true;
  script.onerror = () => console.error("Could not load app-v3.js");
  document.head.append(script);
})();
