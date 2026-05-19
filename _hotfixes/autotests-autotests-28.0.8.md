---
title: "Autotests hotfixes - 28.0.8  Autotests, Release date May 6, 2026 - Hotfixes"
product: Autotests
version: "28.0.8"
subproduct: Autotests
minor_version: "28.0"
date: 2026-05-06 00:00:00+00:00
order: 14
guid: adcab66b96a422e4682ef5efebee44ec68a42f2a
---

<strong>81577 License Manager Warning Mismatch</strong>
<ul><li>A message when checking the account/license account was removed.</li></ul>
<strong>79802 Customer Price in POS Trans. Sales Entry not rounded</strong>
<ul><li>There were issues with Customer Price rounding in POS transactions and refactored duplicated pricing logic that were fixed, and configurable decimal precision for discount percentages was added.<ul><li>Customer Price on POS transaction lines is now rounded according to the <b>Price Rounding to</b> setting in POS Functionality Profile, matching the existing rounding behavior of the regular Price field.</li><li>Extracted shared customer price calculation logic from RecalcSlipOld and RecalcSlipNew into a new procedure CalculateCustomerUnitPrice, eliminating code duplication.</li><li>New <b>Discount % Decimal Places</b> field to <b>POS Functionality Profile</b> was added, allowing retailers to control how discount percentages are formatted on POS transaction lines. Formatting is applied through the AutoFormatMgt Ext extension.</li><li>Extended IRetailPriceUtils interface with GetStandardCustomerPrice, GetStandardMemberPrice, and CalcPriceInclVat to support unit testing.</li></ul></li><li>POS users with customer-specific pricing will see accurate discount percentages on transaction lines, with configurable decimal precision.</li><li>Currencies with large numbers should have a the correct discount % displayed, instead of zero.</li></ul>
