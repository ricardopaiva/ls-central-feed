---
title: "Hotels hotfixes - 27.1.7 Hotels, Release date March 26, 2026 - Hotfixes"
product: Hotels
version: "27.1.7"
subproduct: Hotels
minor_version: "27.1"
date: 2026-03-26 00:00:00+00:00
order: 30
guid: c15c154cf5e19fa793c3a3317ad6f2c2be2ea058
---

<strong>79987 Appsource issues with "Doc. Attachment FactBox"</strong>
<ul><li>There were issues related to <b>Doc. Attachment FactBox</b> happening on validation of v27.1 to v28. This was fixed. </li></ul>
<strong>79625 Blank Accounting - DRE lines not marked as Paid after Invoice is paid</strong>
<ul><li>DRE lines are now correctly marked as <b>Paid</b> when invoice is paid (Blank Accounting)</li><li>There was an issue where <b>Detailed Revenue Entry</b> (DRE) lines were not being marked as Paid after their associated invoice was fully paid. This now works correctly for all payment application methods:<ul><li>Posting payments from journals (both <b>Applies-to Doc. No.</b> and <b>Applies-to ID</b>)</li></ul><ul><li>Manual application from Customer Ledger Entries (payment→invoice and invoice→payment)</li><li>Additionally, unapplying a payment  correctly reverts the DRE Paid status when the invoice becomes open again.</li></ul></li><li>Posting payments from journals (both <b>Applies-to Doc. No.</b> and <b>Applies-to ID</b>)</li><li>Manual application from Customer Ledger Entries (payment→invoice and invoice→payment)</li><li>Additionally, unapplying a payment  correctly reverts the DRE Paid status when the invoice becomes open again.</li></ul>
