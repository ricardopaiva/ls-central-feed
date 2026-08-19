---
title: "Hotels hotfixes - 28.0.26 Hotels, Release date August 18, 2026 - Hotfixes"
product: Hotels
version: "28.0.26"
subproduct: Hotels
minor_version: "28.0"
date: 2026-08-18 00:00:00+00:00
order: 58
guid: 0186cc9757c12d62239204865ea83bd31f481961
---

<strong>86396 Eternal loading is displayed when user allocates a room to a different room type</strong>
<ul><li>There was an issue where the loading icon stayed endlessly on after assigning to another room type. This was fixed. </li></ul>
<strong>86112 Upsell and upgrade indicators on hotel reservations</strong>
<ul><li>Fixed: The upgrade indicator on a reservation now turns on when you upgrade a room type.</li><li>Fixed: the upsell indicator only turns on when the new room type actually costs more — a downgrade no longer gets marked as an upsell.</li><li>Fixed: Changing a room type again now updates the upgrade and upsell indicators to match your latest change, instead of keeping an outdated indicator from an earlier change.</li><li><b>Action required by partners</b>:<ul><li>None — the fix applies automatically once you update.</li></ul></li></ul>
<strong>83678 Service charge on a discounted POS line is calculated inconsistently</strong>
<ul><li>When you discount an item that carries a service charge (added on top of the price), the service charge now reflects the discount everywhere — on the POS line and in the reservation's Detailed Revenue Entries.<ul><li>Previously the service charge could ignore the discount at the POS (charging the full amount) or apply it twice in the back office (charging too little).</li></ul></li><li><b>Action required:</b>
<ul>
<li>None — the correct amount is calculated automatically.</li>
</ul>
</li></ul>
