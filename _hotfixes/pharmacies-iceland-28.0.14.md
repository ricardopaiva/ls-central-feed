---
title: "Pharmacies hotfixes - 28.0.14 Iceland, Release date September 1, 2026 - Hotfixes"
product: Pharmacies
version: "28.0.14"
subproduct: Iceland
minor_version: "28.0"
date: 2026-09-01 00:00:00+00:00
order: 116
guid: 9d773e95c329187778da6672449653da99952f94
---

<strong>63458 LS Pharmacy IS - Siblings both with card</strong>
<ul><li>Improved Sibling e‑Prescription: Siblings holding drug cards now correctly receive insurance benefits, regardless of who is added first.</li></ul>
<strong>83461 It is not possible to access Insurance Documents from Dispense Posted Orders</strong>
<ul><li>Insurance Document is now accessible from Posted Dispense Production (list and card).</li></ul>
<strong>84092 LS Central Pharmacy Dispense - Creating rationing dispensation - More than one line (pharmacy item) for same dispense prescription: Wrong calculation of dispensed packages</strong>
<ul><li>Dispense production lines containing copied lines are now sent individually to Hekla at posting instead of accumulate the quantities pr. e-prescription number.</li><li>Remaining quantity numbers are shown as Subordinate (blue text) in the Dispense Order to indicate that line is copied but those numbers are calculated for the initial line.</li></ul>
<strong>85812 Import of Lyfjaverdskra does not update purhcase price list</strong>
<ul><li>Import of Lyfjaverðskrá, now updates the purchase price list.</li></ul>
<strong>86734 AE - getallacceptances error</strong>
<ul><li>It is possible to get the all acceptances for today.</li><li>Currently, it is not possible to choose the date to retrieve acceptances for, that will come later.</li></ul>
<strong>86982 Pharmacy - Insurance request lines missing</strong>
<ul><li>Prescriptions without insurance caused the error <b>No Active Requests exist for document %1 %2</b>. These prescriptions were not raised to the user nor was the process stopped.</li><li>Now if there is an issue with the insurance it is raised to the user and the process is stopped.</li></ul>
