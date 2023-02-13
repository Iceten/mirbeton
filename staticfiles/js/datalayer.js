const btnFreeQuote = document.querySelector(".section-top-cta--wrap-cta__link");
const btnFreeEvaluation = document.querySelector(
  ".section-content--container__wrap-txt--btn-cta"
);
const btnTopPhoneLink = document.querySelector(
  ".section-top-cta--wrap-cta__phonelink"
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

if (btnTopPhoneLink != null) {
  btnTopPhoneLink.addEventListener("click", function () {
    var delayInMilliseconds = 100;
    setTimeout(function () {
      //your code to be executed after 1 second
      console.log("Click Top Phone Link");
    }, delayInMilliseconds);

    if (window.dataLayer != null) {
      dataLayer.push({ event: "clickTopPhoneLink" });
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

let urlPath = window.location.href;
if (urlPath.search("thank-you") > -1) {
  var delayInMilliseconds = 1000;
  setTimeout(function () {
    if (window.dataLayer != null) {
      dataLayer.push({ event: "consultationFormSent" });
    }
    console.log("Consultation form sent");
  }, delayInMilliseconds);
}
