const sectionValueStack = document.querySelector(".section-value-stack");
const sectionValueStackOption = document.querySelector(
  ".section-value-stack.option-section"
);
const valueStackCheckbox = document.querySelector(
  ".section-value-stack--checkbox"
);

const sideNavToggle = document.getElementById("side-nav-toggle");

// const sideNavToggle = document.querySelector(
//   ".section-navigation--wrapper-small-nav__checkbox-wrap--checkbox"
// );
const sideNav = document.querySelector(".section-navigation--wrapper-side-nav");
const sideNavToggleBis = document.querySelector(
  ".section-navigation-bis--wrapper-small-nav__checkbox-wrap--checkbox"
);
const sideNavBis = document.querySelector(
  ".section-navigation-bis--wrapper-side-nav"
);

const wrapSubs = document.querySelector(
  ".section-navigation--wrapper-nav__item--wrap-sub"
);
const wrapSubsBis = document.querySelector(
  ".section-navigation-bis--wrapper-nav__item--wrap-sub"
);
const navAll = document.querySelector(".section-navigation");
const navAllBis = document.querySelector(".section-navigation-bis");
const navBg = document.querySelector(".section-navigation--bg");
const navBgBis = document.querySelector(".section-navigation-bis--bg");

const popUpCheckBox = document.querySelector(".section-popup--toggle");
const sectionPopUp = document.querySelector(".section-popup");

const sectionOfferAlert = document.querySelector(".section-offer-alert");
const offerAlertCheckBox = document.querySelector(
  ".section-offer-alert--checkbox"
);

const btnTest = document.querySelector(
  ".section-headline--wrapper__wrapper-btn--phone"
);

const sectionTopBanner = document.querySelector(".section-top-banner");
const topBannerCheckBox = document.querySelector(
  ".section-top-banner--checkbox"
);

const sectionTopCta = document.querySelector(".section-top-cta");

//Side Nav Toggle
if (sideNavToggle != null) {
  sideNavToggle.checked = false;
  sideNavToggle.addEventListener("change", function () {
    if (this.checked) {
      sideNav.style.transform = "translate(0)";
      sectionTopCta.classList.add("display-none");
      sectionTopBanner.classList.add("translate-up");
      navAll.classList.remove("margin-top-5");
      sectionTopCta.classList.remove("position-top-5");
      console.log("Checked");
    } else {
      sideNav.style.transform = "translate(-101vw)";
      sectionTopCta.classList.remove("display-none");
    }
  });
}

//Side Nav Toggle Bis
if (sideNavToggleBis != null) {
  sideNavToggleBis.checked = false;
  sideNavToggleBis.addEventListener("change", function () {
    if (this.checked) {
      sideNavBis.style.transform = "translate(0)";
    } else {
      sideNavBis.style.transform = "translate(-60vw)";
    }
  });
}

// Navigation Background
if (navAll != null) {
  if (wrapSubs != null) {
    wrapSubs.classList.add("secondaryBg");
    window.addEventListener("scroll", function () {
      if (window.pageYOffset > 10 && window.pageYOffset < 400) {
        wrapSubs.classList.remove("secondaryBg");
        navAll.classList.remove("fixedNav");
        navAll.classList.add("stickyNav");
        navBg.classList.add("opacityShow");
        wrapSubs.classList.add("primaryBg");
      } else if (window.pageYOffset > 400) {
        navAll.classList.remove("stickyNav");
        wrapSubs.classList.remove("secondaryBg");
        navAll.classList.add("fixedNav");
        navBg.classList.add("opacityShow");
        wrapSubs.classList.add("primaryBg");
      } else if (window.pageYOffset < 10) {
        navAll.classList.remove("fixedNav");
        navAll.classList.remove("stickyNav");
        navBg.classList.remove("opacityShow");
        wrapSubs.classList.remove("primaryBg");
        wrapSubs.classList.add("secondaryBg");
      }
    });
  }
}

// Navigation Background Bis
if (navAllBis != null) {
  wrapSubsBis.classList.add("secondaryBg");
  window.addEventListener("scroll", function () {
    if (window.pageYOffset > 10 && window.pageYOffset < 400) {
      wrapSubsBis.classList.remove("secondaryBg");
      // wrapSubsBis.classList.remove("tertiaryBg");
      navAllBis.classList.remove("fixedNav");
      navAllBis.classList.add("stickyNav");
      navBgBis.classList.add("opacityShow");
      wrapSubsBis.classList.add("primaryBg");
    } else if (window.pageYOffset > 400) {
      navAllBis.classList.remove("stickyNav");
      wrapSubsBis.classList.remove("secondaryBg");
      // wrapSubsBis.classList.remove("tertiaryBg");
      navAllBis.classList.add("fixedNav");
      navBgBis.classList.add("opacityShow");
      wrapSubsBis.classList.add("primaryBg");
    } else if (window.pageYOffset < 10) {
      navAllBis.classList.remove("fixedNav");
      navAllBis.classList.remove("stickyNav");
      navBgBis.classList.remove("opacityShow");
      wrapSubsBis.classList.remove("primaryBg");
      wrapSubsBis.classList.add("secondaryBg");
    }
  });
}

//Pop Up Script - source:  https://www.webtips.dev/how-to-make-an-effective-exit-intent-popup-in-javascript
//Cookie Handling
const CookieService = {
  setCookie(name, value, days, path) {
    let expires = "";
    let path2 = "";

    if (days) {
      const date = new Date();
      date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
      expires = "; expires=" + date.toUTCString();
    }

    if (path) {
      path2 = "; path=/" + path;
    }

    document.cookie = name + "=" + (value || "") + expires + path2 + ";";
  },

  getCookie(name) {
    const cookies = document.cookie.split(";");

    for (const cookie of cookies) {
      if (cookie.indexOf(name + "=") > -1) {
        return cookie.split("=")[1];
      }
    }

    return null;
  },
};

// Wrap the setTimeout into an if statement checking the cookie status and setting a time out to add the event listener
if (!CookieService.getCookie("exitIntentShown")) {
  setTimeout(() => {
    document.addEventListener("mouseout", mouseEvent);
    // document.addEventListener("keydown", return);
    console.log("Function to Add Event listener is on");
  }, 5_000);
}

//Creating the named function to use in the event which will trigger the popup

const mouseEvent = (e) => {
  const shouldShowExitIntent =
    !e.toElement && !e.relatedTarget && e.clientY < 10;

  if (shouldShowExitIntent) {
    document.removeEventListener("mouseout", mouseEvent);
    if (sectionPopUp != null) {
      sectionPopUp.classList.remove("noShow");
    }
    // Set the cookie when the popup is shown to the user
    CookieService.setCookie("exitIntentShown", true, 15, "siteMain");
  }
};

//Event listener to close the popup
if (popUpCheckBox != null) {
  popUpCheckBox.addEventListener("change", function () {
    if (this.checked) {
      sectionPopUp.classList.add("noShow");
    }
  });
}

// Checking the cookie status for the offer alert banner
if (sectionOfferAlert != null) {
  if (!CookieService.getCookie("closeOfferAlert")) {
    sectionOfferAlert.classList.remove("noShow");
    console.log("No cookie removal of noShow class on Offer Alert");
  } else {
    sectionOfferAlert.classList.add("noShow");
    console.log("Cookie is present so adding noShow class on Offer Alert");
  }
}

if (offerAlertCheckBox != null) {
  offerAlertCheckBox.addEventListener("change", function () {
    if (this.checked) {
      sectionOfferAlert.classList.add("noShow");
      // Set the cookie for 6 hours when the offer alert is hidden by the user
      CookieService.setCookie("closeOfferAlert", true, 0.25, "siteMain");
    }
  });
}

// Checking the cookie status for the offer alert banner
if (sectionValueStackOption != null) {
  if (!CookieService.getCookie("closeValueStackOption")) {
    sectionValueStackOption.classList.remove("noShow");
    console.log(
      "No cookie removal of noShow class on section value stack option"
    );
  } else {
    sectionValueStackOption.classList.add("noShow");
    console.log(
      "Cookie is present so adding noShow class on section value stack option"
    );
  }
}

if (sectionValueStackOption != null && valueStackCheckbox != null) {
  valueStackCheckbox.addEventListener("change", function () {
    if (this.checked) {
      sectionValueStackOption.classList.add("noShow");
      // Set the cookie for 6 hours when the offer alert is hidden by the user
      CookieService.setCookie("closeValueStackOption", true, 0.25, "siteMain");
    }
  });
} else if (valueStackCheckbox != null) {
  valueStackCheckbox.addEventListener("change", function () {
    if (this.checked) {
      sectionValueStack.classList.add("noShow");
    }
  });
}

// Checking the cookie status for the offer alert banner
if (sectionTopBanner != null) {
  if (!CookieService.getCookie("closeTopBanner")) {
    sectionTopBanner.classList.remove("translate-up");
    navAll.classList.add("margin-top-5");
    sectionTopCta.classList.add("position-top-5");
    console.log("No cookie removal of translate-up class on Offer Alert");
  } else {
    sectionTopBanner.classList.add("translate-up");
    navAll.classList.remove("margin-top-5");
    sectionTopCta.classList.remove("position-top-5");
    console.log(
      "Cookie is present so adding translate-up class on Offer Alert"
    );
  }
}

if (topBannerCheckBox != null) {
  topBannerCheckBox.addEventListener("change", function () {
    if (this.checked) {
      sectionTopBanner.classList.add("translate-up");
      navAll.classList.remove("margin-top-5");
      sectionTopCta.classList.remove("position-top-5");
      // Set the cookie for 6 hours when the offer alert is hidden by the user
      CookieService.setCookie("closeTopBanner", true, 0.25, "siteMain");
    }
  });
}
