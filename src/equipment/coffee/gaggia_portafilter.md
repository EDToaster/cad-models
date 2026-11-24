# Gaggia Classic / Classic Pro bottomless portafilter

This layout reference models the head, installed basket, connector and black plastic handle. It is based on a close product listing, not a scan, factory drawing or confirmation of the owner's exact SKU.

| Parameter | Layout input | Evidence |
| --- | ---: | --- |
| Overall length | ~215 mm | [Shades of Coffee, Gaggia OEM black plastic handle](https://www.shadesofcoffee.co.uk/gaggia-bottomless-portafilter-oem) |
| Across the two ear tips | ~78 mm | [Shades of Coffee](https://www.shadesofcoffee.co.uk/gaggia-bottomless-portafilter-oem); this is a diagonal tip-to-tip distance, not a head body diameter. |
| Oval grip cross-section | ~35 × 22 mm | [Shades of Coffee](https://www.shadesofcoffee.co.uk/gaggia-bottomless-portafilter-oem) |
| Included triple basket depth | ~28 mm | [Shades of Coffee](https://www.shadesofcoffee.co.uk/gaggia-bottomless-portafilter-oem); not the measured drop below the metal head. |

These parts vary. [BrewRatio](https://thebrewratio.com/product/gaggia-classic-naked-portafilter-58mm/) lists 220 mm overall with a 25 mm basket, and [Blue Star Coffee](https://www.bluestarcoffee.eu/en/Gaggia-Classic-Naked-Portafilter/m-2960.aspx) lists 77.8 mm fin-to-fin and a 25 mm basket. [Gaggia North America](https://www.gaggia-na.com/products/gaggia-bottomless-portafilter) lists an 18 g basket and compatibility with different basket depths. The nominal 58 mm basket size is not a locator diameter. Do not combine the extremes from different listings into a purported exact part.

The assumed 70 mm outer head diameter, underside bearing surface, lug angles/profile, head height, basket detail/protrusion and handle slope/contour are **mockup only**. The basket floor is unperforated in CAD. Do not machine a mating profile or claim load capacity from this model. Before designing the seat, confirm the actual underside contact band, basket projection beneath it, and lug/neck clearance on the user's assembly.

From `src/`, run `cad run -m equipment.coffee.gaggia_portafilter`. The local +X axis points to the handle tip. At 215 mm overall with the estimated head radius of 35 mm, the basket-center-to-tip reach is 180 mm in this mockup, not a catalog dimension.
