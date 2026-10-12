(function (root) {
  "use strict";
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }
  function money(c) { return "$" + Math.floor(c / 100) + "." + ("0" + (c % 100)).slice(-2); }

  function stemPlan(totalStems, focalRatio, secondaryRatio, fillerRatio, vaseHeightCm) {
    if (!(totalStems > 0) || !(focalRatio > 0) || !(secondaryRatio > 0) || !(fillerRatio > 0) || !(vaseHeightCm > 0)) return { error: "stems, ratios and vase height must be positive" };
    var sum = focalRatio + secondaryRatio + fillerRatio;
    var focal = Math.round(totalStems * focalRatio / sum);
    var secondary = Math.round(totalStems * secondaryRatio / sum);
    var filler = totalStems - focal - secondary;
    var stemLen = Math.round(vaseHeightCm * 1.5);
    return { focal: focal, secondary: secondary, filler: filler, stemLen: stemLen };
  }

  function bunchPlan(stemsNeeded, bunchSize, bunchPriceDollars) {
    if (!(stemsNeeded > 0) || !(bunchSize > 0) || !(bunchPriceDollars > 0)) return { error: "stems, bunch size and bunch price must be positive" };
    var bunches = Math.ceil(stemsNeeded / bunchSize);
    var bought = bunches * bunchSize;
    var leftover = bought - stemsNeeded;
    var costCents = Math.round(bunches * bunchPriceDollars * 100);
    return { bunches: bunches, bought: bought, leftover: leftover, costCents: costCents };
  }

  function lifePlan(focalDays, secondaryDays, fillerDays, focalCount, secondaryCount, fillerCount, bouquetPriceDollars) {
    if (!(focalDays > 0) || !(secondaryDays > 0) || !(fillerDays > 0) || !(focalCount > 0) || !(secondaryCount > 0) || !(fillerCount > 0) || !(bouquetPriceDollars > 0)) return { error: "days, counts and price must be positive" };
    var total = focalCount + secondaryCount + fillerCount;
    var days = Math.round((focalDays * focalCount + secondaryDays * secondaryCount + fillerDays * fillerCount) / total);
    var priceCents = Math.round(bouquetPriceDollars * 100);
    var perDayCents = Math.round(priceCents / days);
    return { days: days, priceCents: priceCents, perDayCents: perDayCents };
  }

  function renderStem(r, totalStems, focalRatio, secondaryRatio, fillerRatio, vaseHeightCm) {
    return "A bouquet of " + plural(totalStems, "stem") + " on the labeled " + focalRatio + ":" + secondaryRatio + ":" + fillerRatio + " recipe: " + plural(r.focal, "focal stem") + ", " + r.secondary + " secondary, " + r.filler + " filler. For a vase " + vaseHeightCm + " cm tall, cut stems to about " + r.stemLen + " cm.";
  }

  function renderBunch(r, stemsNeeded, bunchSize, bunchPriceDollars) {
    return plural(stemsNeeded, "stem") + " needed, sold " + plural(bunchSize, "stem") + " a bunch at $" + bunchPriceDollars + ": " + plural(r.bunches, "bunch", "bunches") + ", " + r.bought + " stems home, " + plural(r.leftover, "stem") + " left over - " + money(r.costCents) + " on the counter.";
  }

  function renderLife(r, focalDays, secondaryDays, fillerDays, focalCount, secondaryCount, fillerCount, bouquetPriceDollars) {
    return "A labeled " + focalDays + "-day focal, " + secondaryDays + "-day secondary and " + fillerDays + "-day filler average out to about " + plural(r.days, "day") + " of vase life - " + money(r.perDayCents) + " a day on a " + money(r.priceCents) + " bouquet.";
  }

  var api = { stemPlan: stemPlan, bunchPlan: bunchPlan, lifePlan: lifePlan, renderStem: renderStem, renderBunch: renderBunch, renderLife: renderLife };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.BouquetMath = api;
})(this);
