---
title: "Hotels hotfixes - 28.0.20 Hotels, Release date July 7, 2026 - Hotfixes"
product: Hotels
version: "28.0.20"
subproduct: Hotels
minor_version: "28.0"
date: 2026-07-07 00:00:00+00:00
order: 53
guid: 2c1a4d3493ee89e140e0ede2d128f89c9e255a26
---

<strong>84186 Number of Nights Resets After Interacting with Guest List</strong>
<ul><li>Set the number of nights on a hotel reservation, add enough adults to open the guest list, and your night count now stays put.<ul><li>Previously, interacting with the guest list reset the nights back to 1, so a reservation could be saved with the wrong stay length if nobody noticed.</li></ul></li><li><b>Action required by partners</b>:</li><li><b>None.</b> The fix applies automatically once the hotfix (28.0.20) or version 28.1.0 is installed.</li></ul>
<strong>83879 Balance Recalculation Incorrect After Moving Charges Between Reservations</strong>
<ul><li>When you move a charge from one reservation to another within a group and then take payment, the charge now stays on the reservation you moved it to. Balances on both reservations stay correct, so you no longer see the moved charge lingering on the original reservation, or a negative balance on the reservation you moved it to.</li><li><b>Action required by partners</b>:<ul><li><b>None.</b></li></ul></li></ul>
<strong>83656 Charge-to-room fails for service-charge items from outlet POS ('Property[] not found in Hotel Setup'); add Select All to refund lookup</strong>
<ul><li>Charge an item that carries a service charge profile to a guest's room directly from an outlet POS, such as a restaurant. Selling the item, sending it to the kitchen, and charging the table to the room now posts the item and its service charges to the reservation. <ul><li>Previously this failed with <b>Property[] not found in 'Hotel Setup'</b> and nothing was posted.</li><li>The POS item-refund lookup also gets a Select all command that marks every line at once — the inverse of the existing Reset all.</li></ul></li><li><b>Action required by partners</b>:<ul><li><b>None.</b> To use the fix, make sure outlet stores have their Service Charge Location configured in Hotel Setup as usual.</li></ul></li></ul>
