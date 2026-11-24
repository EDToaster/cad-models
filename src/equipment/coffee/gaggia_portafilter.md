# Gaggia Classic / Classic Pro bottomless portafilter

This reference models the head, installed basket, connector and black plastic handle. The owner's measurements and side photograph supersede retailer dimensions for the side profile. The plan dimensions still come from a similar listing, not a confirmed SKU.

| Owner's measurement | mm | Model interpretation |
| --- | ---: | --- |
| Basket height | 26.30 | Basket underside (Z=0) to top of rim |
| Exposed metal connector length | ~22.8 | Along the handle axis, from outer head wall to start of black flare |
| Connector thickness | 10 | Vertical thickness; underside 4 mm below the basket bottom, top 6 mm above |
| Lowest point of handle | 18 below portafilter bottom | Low point at the grip flare in the photo; referenced to the metal head underside |

The basket bottom and the underside of the metal head are provisionally set flush; their exact relationship and the actual bearing surface have not been measured. The 18 mm grip drop is **not** measured from the connector: do not add the 4 mm neck drop to it.

| Parameter | Layout input | Evidence |
| --- | ---: | --- |
| Overall length | ~215 mm | [Shades of Coffee, Gaggia OEM black plastic handle](https://www.shadesofcoffee.co.uk/gaggia-bottomless-portafilter-oem) |
| Across the two ear tips | ~78 mm | [Shades of Coffee](https://www.shadesofcoffee.co.uk/gaggia-bottomless-portafilter-oem); this is a diagonal tip-to-tip distance, not a head body diameter. |
| Oval grip cross-section | ~35 × 22 mm | [Shades of Coffee](https://www.shadesofcoffee.co.uk/gaggia-bottomless-portafilter-oem) |

These parts vary. [BrewRatio](https://thebrewratio.com/product/gaggia-classic-naked-portafilter-58mm/) lists 220 mm overall with a 25 mm basket, and [Blue Star Coffee](https://www.bluestarcoffee.eu/en/Gaggia-Classic-Naked-Portafilter/m-2960.aspx) lists 77.8 mm fin-to-fin and a 25 mm basket. [Gaggia North America](https://www.gaggia-na.com/products/gaggia-bottomless-portafilter) lists an 18 g basket and compatibility with different basket depths. The nominal 58 mm basket size is not a locator diameter. Do not combine the extremes from different listings into a purported exact part.

The assumed 70 mm outer head diameter, underside bearing surface, lug angles/profile, connector width and detailed grip contour are **mockup only**. The installed basket is modeled with an unperforated floor. Do not machine a mating profile or claim load capacity from this model. Before designing the seat, verify the actual underside contact band, basket projection beneath it and lug/neck clearance.

From `src/`, run `cad run -m equipment.coffee.gaggia_portafilter`. The local +X axis points to the handle tip. At 215 mm overall with the estimated head radius of 35 mm, the basket-center-to-tip reach is 180 mm in this mockup, not a catalog dimension.
