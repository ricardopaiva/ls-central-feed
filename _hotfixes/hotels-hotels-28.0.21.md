---
title: "Hotels hotfixes - 28.0.21 Hotels, Release date July 14, 2026 - Hotfixes"
product: Hotels
version: "28.0.21"
subproduct: Hotels
minor_version: "28.0"
date: 2026-07-14 00:00:00+00:00
order: 54
guid: a07e10152a7b15ab81a43c1f625751231d0d1d17
---

<strong>84971 Room rate recalculated too low (included rate-attribute amount deducted) for reservations created through the API</strong>
<ul><li>Fixed an issue where the room rate on reservations created or updated through the LS Hotels web service (Web and Channel Management) was recalculated too low.<ul><li>When the rate code carried rate attributes marked as <b>Included in Rate</b>, the attribute amount was deducted twice from the room rate.</li><li>The room rate now reflects a single deduction, and the reservation total matches the price sent by the API.</li></ul></li></ul>
<strong>84187 New Contact Created for Reservation Is Incorrectly Flagged as a Child</strong>
<ul><li>Details not available.</li></ul>
<strong>83995 Hotel POS charge-to-room does not pass the correct unit of measure to the revenue entry</strong>
<ul><li>Items you charge to a guest's room now keep their unit of measure.<ul><li>When you charge a POS item to a room, the resulting revenue entry now shows the unit of measure you selected, instead of leaving it blank.</li></ul></li><li><b>Action required by partners</b>:<ul><li><b>None.</b> The correction applies automatically once you're on a version that includes it.</li></ul></li><li><b>Not included in this fix</b>:<ul><li>This update doesn't change the <b>Invalid Unit of Measure</b> warning that can appear when you change a unit of measure at the POS. That warning doesn't block posting — you can dismiss it and post the charge — and we're addressing it in a separate issue.</li></ul></li></ul>
<strong>83151 ReservationExtraSave API - Updating an existing extra (lineNo ≠ 0) fails with "record is not up-to-date"</strong>
<ul><li>Updating an existing reservation extra through the hotel web API now works.<ul><li>Previously, re-sending an extra with its assigned line number to change a value — such as quantity, unit price, or discount — failed with a <b>record is not up-to-date</b> error, and the change was lost.</li><li>The line now updates in place, with no duplicate line, and the linked revenue stays in sync.</li></ul></li><li><b>Action required by partners</b>:<ul><li><b>None</b>, beyond applying the 27.1 hotfix.</li></ul></li></ul>
<strong>83128 Changing price on one DRE line changes applies same change for all DRE lines if adding a routing rule to the reservation</strong>
<ul><li>Manual room-rate prices on a reservation now stay put.<ul><li>Previously, changing a routing rule — or switching the reservation's customer or payer — could reset every included-in-rate line back to the standard rate, flattening a multi-night stay to a single price and overwriting any price you'd entered by hand.</li><li>Routing changes now only re-route charges, and changing the customer or payer keeps each night's own rate along with any manual prices you've set.</li></ul></li><li><b>Action required by partners</b>:<ul><li><b>None.</b> The fix applies automatically on upgrade — per-night rates and manual price changes are preserved from then on, with no setup or configuration changes.</li></ul></li></ul>
