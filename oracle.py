import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def money(c): return "$" + str(c // 100) + "." + str(c % 100).zfill(2)
def fmt(x): return str(jsnum(x))
def rnd(x): return math.floor(x + 0.5)

def stem_plan(totalStems, focalRatio, secondaryRatio, fillerRatio, vaseHeightCm):
    if not (totalStems > 0) or not (focalRatio > 0) or not (secondaryRatio > 0) or not (fillerRatio > 0) or not (vaseHeightCm > 0):
        return {"error": "stems, ratios and vase height must be positive"}
    s = focalRatio + secondaryRatio + fillerRatio
    focal = rnd(totalStems * focalRatio / s)
    secondary = rnd(totalStems * secondaryRatio / s)
    return {"focal": focal, "secondary": secondary, "filler": totalStems - focal - secondary,
            "stemLen": rnd(vaseHeightCm * 1.5)}

def bunch_plan(stemsNeeded, bunchSize, bunchPriceDollars):
    if not (stemsNeeded > 0) or not (bunchSize > 0) or not (bunchPriceDollars > 0):
        return {"error": "stems, bunch size and bunch price must be positive"}
    bunches = math.ceil(stemsNeeded / bunchSize)
    bought = bunches * bunchSize
    return {"bunches": bunches, "bought": bought, "leftover": bought - stemsNeeded,
            "costCents": rnd(bunches * bunchPriceDollars * 100)}

def life_plan(focalDays, secondaryDays, fillerDays, focalCount, secondaryCount, fillerCount, bouquetPriceDollars):
    if not (focalDays > 0) or not (secondaryDays > 0) or not (fillerDays > 0) or not (focalCount > 0) or not (secondaryCount > 0) or not (fillerCount > 0) or not (bouquetPriceDollars > 0):
        return {"error": "days, counts and price must be positive"}
    total = focalCount + secondaryCount + fillerCount
    days = rnd((focalDays * focalCount + secondaryDays * secondaryCount + fillerDays * fillerCount) / total)
    priceCents = rnd(bouquetPriceDollars * 100)
    return {"days": days, "priceCents": priceCents, "perDayCents": rnd(priceCents / days)}

def render_stem(r, totalStems, focalRatio, secondaryRatio, fillerRatio, vaseHeightCm):
    return ("A bouquet of " + plural(totalStems, "stem") + " on the labeled " + fmt(focalRatio) + ":" + fmt(secondaryRatio) + ":"
            + fmt(fillerRatio) + " recipe: " + plural(r["focal"], "focal stem") + ", " + fmt(r["secondary"]) + " secondary, "
            + fmt(r["filler"]) + " filler. For a vase " + fmt(vaseHeightCm) + " cm tall, cut stems to about " + fmt(r["stemLen"]) + " cm.")

def render_bunch(r, stemsNeeded, bunchSize, bunchPriceDollars):
    return (plural(stemsNeeded, "stem") + " needed, sold " + plural(bunchSize, "stem") + " a bunch at $" + fmt(bunchPriceDollars)
            + ": " + plural(r["bunches"], "bunch", "bunches") + ", " + fmt(r["bought"]) + " stems home, "
            + plural(r["leftover"], "stem") + " left over - " + money(r["costCents"]) + " on the counter.")

def render_life(r, focalDays, secondaryDays, fillerDays, focalCount, secondaryCount, fillerCount, bouquetPriceDollars):
    return ("A labeled " + fmt(focalDays) + "-day focal, " + fmt(secondaryDays) + "-day secondary and " + fmt(fillerDays)
            + "-day filler average out to about " + plural(r["days"], "day") + " of vase life - " + money(r["perDayCents"])
            + " a day on a " + money(r["priceCents"]) + " bouquet.")

cases = []
for a in [(16, 3, 5, 8, 20), (24, 3, 5, 8, 25), (10, 2, 3, 5, 18), (0, 3, 5, 8, 20)]:
    r = stem_plan(*a)
    cases.append({"fn": "stemPlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_stem(r, *a)})
for a in [(16, 5, 6), (24, 10, 9), (12, 6, 7), (16, 0, 6)]:
    r = bunch_plan(*a)
    cases.append({"fn": "bunchPlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_bunch(r, *a)})
for a in [(7, 10, 14, 3, 5, 8, 24), (5, 8, 12, 5, 8, 11, 27), (6, 9, 14, 2, 4, 7, 18), (0, 10, 14, 3, 5, 8, 24)]:
    r = life_plan(*a)
    cases.append({"fn": "lifePlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_life(r, *a)})

with open("expected.json", "w") as f:
    f.write(json.dumps(cases, separators=(",", ":")) + "\n")
print("wrote", len(cases), "cases")
