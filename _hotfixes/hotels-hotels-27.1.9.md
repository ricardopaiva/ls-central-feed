---
title: "Hotels hotfixes - 27.1.9 Hotels, Release date April 7, 2026 - Hotfixes"
product: Hotels
version: "27.1.9"
subproduct: Hotels
minor_version: "27.1"
date: 2026-04-07 00:00:00+00:00
order: 37
guid: 4c4982982ca6f99d44a85bee7a27d7a338884ef0
---

<strong>79785 Blank Accounting - Creating credit memo with deposit results in wrong balance when posting invoice again</strong>
<ul><li>There was an issue in Blank Accounting where reversing a posted invoice and posting a new one resulted in an incorrect negative balance. </li><li>The deposit was not being consumed in the re-issued invoice because it remained marked as used from the original invoice after the credit memo.</li><li>The deposit entries are now properly reset when a credit memo is posted, allowing them to be consumed again in subsequent invoices. </li></ul>
<strong>79628 Unit price not showing in Invoice management detailed and standard views</strong>
<ul><li>There was an issue  where the Unit Price column was only visible in the Simple view of the Invoice Management page.</li><li>The Unit Price is now correctly displayed in all view modes (Simple, Standard, and Detailed).</li></ul>
