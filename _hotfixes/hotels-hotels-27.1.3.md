---
title: "Hotels hotfixes - 27.1.3 Hotels, Release date March 3, 2026 - Hotfixes"
product: Hotels
version: "27.1.3"
subproduct: Hotels
minor_version: "27.1"
date: 2026-03-03 00:00:00+00:00
order: 16
guid: 72423c5242288ce0216c45270a649cc4a3e3ab0d
---

<strong>78258 Hotels package manager high severity issue</strong>
<ul><li>Details not available.</li></ul>
<strong>77703 When there is Rate Attribute which is Included in Rate = TRUE, when no. of adults/guest is changed, the Rate Attribute arrives at incorrect values</strong>
<ul><li>There were issues fixed, related to the assigning of Rate Attributes on Hotel Reservations:<ul><li>When a Rate Attribute is Included in Rate and <b>Per Guest = true</b>, the resulting Reservation Extra and Revenue Entry now has the Quantity set according to the number of Persons in the Guest List, as long as the Rate has configured the price for Extra Adults or is Occupancy Based Pricing.</li><li>When adding or removing guests on a confirmed reservation, the quantity of the Res. Extras and Revenue Entries that come from Rate Attributes Included in Rate is now updated as well.</li><li>When a Rate Attribute with Daily Posting Pattern and <b>Included in Rate = false</b>, the resulting Revenue Entries are no longer multiplied by the number of nights.</li></ul></li><li>When a Rate Attribute is Included in Rate and <b>Per Guest = true</b>, the resulting Reservation Extra and Revenue Entry now has the Quantity set according to the number of Persons in the Guest List, as long as the Rate has configured the price for Extra Adults or is Occupancy Based Pricing.</li><li>When adding or removing guests on a confirmed reservation, the quantity of the Res. Extras and Revenue Entries that come from Rate Attributes Included in Rate is now updated as well.</li><li>When a Rate Attribute with Daily Posting Pattern and <b>Included in Rate = false</b>, the resulting Revenue Entries are no longer multiplied by the number of nights.</li></ul>
