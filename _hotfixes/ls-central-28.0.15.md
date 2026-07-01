---
title: "LS Central hotfixes - 28.0.15, Release date May 19, 2026 - Hotfixes"
product: LS Central
version: "28.0.15"
subproduct: 
minor_version: "28.0"
date: 2026-05-19 00:00:00+00:00
order: 8
guid: 4fd2d7956e6ef3c357e0b55ab7a7822c408283f8
---

<strong>82236 Search for reservation based on rental unit is not working properly</strong>
<ul><li>When a rental unit is returned and the operator uses <b>Search</b> from the Activity Role Center to look up the reservation by rental unit number, the system now returns the <b>most recent</b> rental assignment for that unit instead of the oldest one. </li><li>Before, if a unit had a history of rentals, the search could open a prior (already-completed) reservation, making it impossible to find the currently active rental.</li></ul>
<strong>81505 LS Booking - Rental and Return in Different Location</strong>
<ul><li>Operators can now configure an <b>automatic surcharge</b> that is applied when a rental unit is returned to a location other than the one where it was picked up. When the customer returns the unit at a different store, a charge line is added automatically to the rental reservation at the configured price — there is no need to add it manually at the POS. A message is shown to the operator confirming that the cross-location charge has been added.</li><li>Set up on the <b>Activity Type Card</b> with two new fields: <b>Cross Location Charge Amount</b> (the fixed fee) and <b>Cross Location Posting Item</b> (the item used to post the charge). The return location is also stamped on each processed unit entry and is visible on the <b>Processed Unit Entries</b> FactBox.</li><li>Defaults are blank/zero, so existing tenants see no behavior change until the fields are configured. Late-return charges continue to work independently, a return that is both late and cross-location produces both lines.</li></ul>
