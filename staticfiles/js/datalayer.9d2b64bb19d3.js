const btnFreeQuote = document.querySelector(
  ".section-navigation--wrapper-nav__links--wrap-cta__link"
);
const btnFreeEvaluation = document.querySelector(
  ".section-content--container__wrap-txt--btn-cta"
);
const btnPromo = document.querySelector("section-top-banner--para");

// Add Events to DataLayer
if (btnFreeQuote != null) {
  btnFreeQuote.addEventListener("click", function () {
    if (window.dataLayer != null) {
      dataLayer.push({ event: "clickQuote" });
    }
  });
}

if (btnFreeEvaluation != null) {
  btnFreeEvaluation.addEventListener("click", function () {
    if (window.dataLayer != null) {
      dataLayer.push({ event: "clickEvaluation" });
    }
  });
}

if (btnPromo != null) {
  btnPromo.addEventListener("click", function () {
    if (window.dataLayer != null) {
      dataLayer.push({ event: "clickPromo" });
    }
  });
}
