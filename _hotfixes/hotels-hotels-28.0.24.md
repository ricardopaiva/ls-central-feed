---
title: "Hotels hotfixes - 28.0.24 Hotels, Release date August 4, 2026 - Hotfixes"
product: Hotels
version: "28.0.24"
subproduct: Hotels
minor_version: "28.0"
date: 2026-08-04 00:00:00+00:00
order: 58
guid: 11567ef6b1b24822582a3301604a48f7668c92fd
---

<strong>85401 Missing Rate Code Currency on DRE lines for earlier BEC Reservations affects to upgrade calculations</strong>
<ul><li>Older reservations created through the Booking Engine Connector (BEC) in a foreign currency now show correct amounts. An upgrade step backfills the missing rate code currency on their detailed revenue entry lines, so factbox totals, extra charges, and rate changes made through room type upgrades calculate correctly again.</li><li><b>Action required by partners</b>: None — the fix applies automatically on upgrade.</li></ul>
<strong>84467 Unable to update Guest Name and Guest List</strong>
<ul><li>Rename a guest on a reservation and the new name now sticks. When you change the guest name and confirm the prompt, the reservation, the guest list, and the guest's member contact all update to the new name — no more re-selecting the guest to force it, and no "information on the page is not up-to-date" error.</li><li><b>Action required by partners</b>: None — the fix applies automatically on upgrade.</li></ul>
<strong>83958 No. of persons in Room type setup is not taken into account when adding guests to a room from v27.1 to 28.1</strong>
<ul><li>The Guest List now evaluates two Room Type capacity caps when adding or modifying guests in the back office:<ul><li><b>Total cap</b>: Adults + Children + Infants must not exceed No. of Persons. No. of Extra beds is not part of this calculation.</li><li><b>Children cap</b>: Children + Infants must not exceed No. of Children.</li></ul>Exceeding a cap shows a warning message, but the guest is still added so operators can override it. Caps set to zero are treated as not configured and skipped. The Room Type card now rejects setups where No. of Adults or No. of Children is greater than No. of Persons. <b>Web service capacity threshold is unchanged</b>: the reservationSave API guard (Adults must not exceed No. of Persons + No. of Extrabeds) is untouched by this fix. However, guest additions that route through the shared Guest List capacity check (used internally by some integration paths) will now also generate a capacity notification when a cap is exceeded, since that check no longer skips confirmed reservations — this is a new, visible side effect for those paths that did not occur before.</li></ul>
