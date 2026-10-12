# Bouquet math

The recipe split for a bouquet, how many bunches to buy at the market, and what a day of vase life costs. Exact arithmetic in the browser, every borrowed number labeled.

Live site: https://ilanis-agent.github.io/bouquetmath/

## The three tools

- **Stem plan** - `stemPlan(totalStems, focalRatio, secondaryRatio, fillerRatio, vaseHeightCm)`: focal, secondary and filler counts, plus the cut length for the vase.
- **Bunch plan** - `bunchPlan(stemsNeeded, bunchSize, bunchPriceDollars)`: bunches to buy, stems home, leftovers and the counter total.
- **Life plan** - `lifePlan(focalDays, secondaryDays, fillerDays, focalCount, secondaryCount, fillerCount, bouquetPriceDollars)`: weighted vase life and cost per day.

## Labeled norms (illustrative estimates, not rules)

- Labeled recipe: 3:5:8 focal, secondary, filler. Labeled cut: stems about 1.5 times the vase height. Labeled vase lives: 7 days focal, 10 secondary, 14 filler. The florist's eye and the flower's own condition win.

## Files

- `index.html` / `app.html` - landing and calculators (static, no dependencies)
- `engine.js` - pure arithmetic + renderers, runs in browser and node
- `oracle.py` - python mirror of the engine; regenerates `expected.json`
- `test.js` - compares engine output to the oracle: `node test.js` (12 cases, 66 checks)

Regenerate the oracle expectations: `python3 oracle.py`
