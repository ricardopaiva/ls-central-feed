---
title: "Hotels hotfixes - 28.0.15 Hotels, Release date June 9, 2026 - Hotfixes"
product: Hotels
version: "28.0.15"
subproduct: Hotels
minor_version: "28.0"
date: 2026-06-09 00:00:00+00:00
order: 42
guid: 0f3082cfcb6e69afef5fa3d4e6cabb15f0d212d1
---

<strong>83287 Tape chart hover not shown correctly when reservation spans entire width</strong>
<ul><li>The hover behaviour was updated so that long reservations now display their tooltip reliably. <ul><li>The tooltip logic was improved to detect when a reservation is too wide for standard hover detection, and switches to a cursor-entry-based approach in those cases — falling back to the original hover behaviour for shorter reservations.</li></ul></li></ul>
<strong>83260 Tape Chart not showing reservations that span the entire visible date range</strong>
<ul><li>Reservations that span the entire visible date range now show correctly on the Tape Chart. <ul><li>Previously, a long stay (for example a 28-night booking that started before the first visible day and ended after the last) showed nothing on the chart, even when you scrolled forward to dates inside the stay.</li><li>Long and group reservations are now drawn across the full multiday view as expected.</li></ul></li><li><b>Action required by partners:</b>
<ul>
<li>None, the fix applies automatically once the updated version or hotfix is installed.</li>
</ul>
</li><li><b>Known issue</b>
<ul>
<li>The hover tooltip on a reservation that spans the entire visible date range is misplaced. This will be addressed in a separate fix.</li>
</ul>
</li></ul>
<strong>82598 Service charges post incorrectly on POS Pay and Charge to Room (missing income/expense lines, duplicate lines, wrong revenue account)</strong>
<ul><li>Service charges now post correctly on hotel POS transactions, whether you pay at the POS or charge to a room. </li><li>When the service charge is included in the item price, it now appears as a separate income/expense line; when it is not, charging to room no longer creates a duplicate line.</li><li>Service-charge lines charged to a room now use the correct Room Charge revenue account, and returns reverse service charges correctly too.</li><li><b>Action required by partners:</b>
<ul>
<li>None. Deposit and folio payment transactions opened from the reservation card are unchanged by this fix.</li>
</ul>
</li></ul>
