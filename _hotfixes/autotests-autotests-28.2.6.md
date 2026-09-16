---
title: "Autotests hotfixes - 28.2.6 Autotests, Release date September 8, 2026 - Hotfixes"
product: Autotests
version: "28.2.6"
subproduct: Autotests
minor_version: "28.2"
date: 2026-09-08 00:00:00+00:00
order: 14
guid: 96bc8ec119dd390587fba12310b910397f782d7e
---

<strong>87059 Coupon with Handling::Tender cannot be used more than once in Transaction</strong>
<ul><li>You can now redeem a tender coupon more than once in the same transaction, whether the eligible items sit on one line or are split across several lines. Previously, only one redemption applied unless all the eligible quantity was on a single line with a quantity greater than one.</li><li>This fixes a regression introduced by the changes included in hotfix 28.2.4.</li></ul>
<strong>86777 Change in Z Report</strong>
<ul><li>Z report shows denomination breakdown for every counted currency</li><li>Work item: AB#86777 · Type: Fix · Affects version: 28.2</li><li>Area: Backoffice — XZ Report</li><li>The end-of-day (Z) report now prints the coin and note breakdown for every currency you count in the safe, not just one. Previously, when a register counted more than one currency (for example DKK and EUR), only the last currency's denomination breakdown appeared — the totals were correct, but the detailed breakdown for the other currencies was missing.</li><li><b>Why it matters</b>:<ul><li>Stores handling multiple currencies could not reconcile each currency's coins and notes from the Z report, making end-of-day cash counting harder to verify.</li></ul></li></ul>
<strong>85741 Exchange Function is not working on 28 Version</strong>
<ul><li>Handling of Receipt Barcode was fixed.</li></ul>
<strong>80119 Not possible to scan GS1 barcode on POS using GS1 version 2</strong>
<ul><li>Barcodes with leading zeros are now, correctly handled in GS1 barcode handling v2.</li></ul>
