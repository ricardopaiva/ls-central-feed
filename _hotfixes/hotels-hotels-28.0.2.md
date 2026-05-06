---
title: "Hotels hotfixes - 28.0.2 Hotels, Release date April 21, 2026 - Hotfixes"
product: Hotels
version: "28.0.2"
subproduct: Hotels
minor_version: "28.0"
date: 2026-04-21 00:00:00+00:00
order: 19
guid: 13aedc0f8a794439cf3bf05b1f4098171495015b
---

<strong>80883 Unable to open folio view</strong>
<ul><li>An issue was fixed, where the <b>Folio Summary View</b> would fail to open with a string length error, when the hotel reservation number exceeded ten characters.</li></ul>
<strong>80259 Upgrade Codeunit: Update invoice details on folios for reservations that were booked before change</strong>
<ul><li>A new upgrade function was added to solve missing invoice details for reservations done before changes in v27.1.</li></ul>
<strong>80195 Guest Management - Child rates are not included on total rate</strong>
<ul><li><b>Extra Charge</b> field was added on guest records to track applied charges.</li><li>When adding a child to a confirmed reservation the user can now choose between adding the child price to the rate or keep the current price. Same for Extra adults.</li><li>When removing a guest whose extra charge was applied, the user is prompted to reverse the charge.</li><li>When modifying a guest type, the old charge is reversed and the new charge is prompted.</li></ul>
<strong>79793 Deposit not consumed by Night Audit when collected for a specific payer via payer selection dialog in POS</strong>
<ul><li>An issue was fixed, on collecting deposit using <b>Payer selector</b> panel. It was getting a wrong value for <b>Payer No.</b></li></ul>
<strong>79545 When posting invoice in blank accounting the discount is not added to Sales Lines correctly</strong>
<ul><li>An issue was fixed, where discounts applied to hotel reservations were not correctly reflected on invoice lines when using blank accounting.</li><li>Previously, the discount was visible on DRE lines but disappeared from the Sales Invoice, and closing a preview invoice would overwrite the original DRE values.</li><li>Now, discount information is properly carried over to invoice lines.</li></ul>
