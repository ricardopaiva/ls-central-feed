---
title: "LS Central hotfixes - 28.0.10, Release date May 6, 2026 - Hotfixes"
product: LS Central
version: "28.0.10"
subproduct: 
minor_version: "28.0"
date: 2026-05-06 00:00:00+00:00
order: 10
guid: 5210892a13fd7444eac70a7a49b1355bbd295113
---

<strong>81725 Update CO eCommerce Mgt codeunit with new event OnBeforeCheckPreApprovedAmount</strong>
<ul><li>New event, <b>OnBeforeCheckPreApprovedAmount</b> was added in CU CO eCommerce Mgt.</li></ul>
<strong>81577 License Manager Warning Mismatch</strong>
<ul><li>A message when checking the account/license account was removed.</li></ul>
<strong>81443 Suspend Transaction - Receipt No. on POS Not Incrementing Properly</strong>
<ul><li>LastSlipNo assignment logic was fixed, to prevent incorrect incrementing on POS transactions after suspending transactions.</li></ul>
<strong>80953 Error when upgrading to version 28.0</strong>
<ul><li>There was an upgrade failure from version 27.1 to 28.0 caused by a new unique key on the LSC Wish List Line table. </li><li>The <b>ItemAndVariantUOM</b> key on table <b>LSC Wish List Line</b> was introduced in version 28.0 with <b>Unique = true</b>. </li><li>Business Central does not allow a new unique key to be added during an upgrade because existing data may contain duplicates, causing Sync-NAVApp to fail. </li><li>The Unique property was removed from the key so the upgrade completes successfully. </li><li>Customers upgrading from version 27.1 to 28.0 or later  no longer encounter a schema sync failure during the upgrade process.</li></ul>
<strong>79802 Customer Price in POS Trans. Sales Entry not rounded</strong>
<ul><li>There were issues with Customer Price rounding in POS transactions and refactored duplicated pricing logic that were fixed, and configurable decimal precision for discount percentages was added.<ul><li>Customer Price on POS transaction lines is now rounded according to the <b>Price Rounding to</b> setting in POS Functionality Profile, matching the existing rounding behavior of the regular Price field.</li><li>Extracted shared customer price calculation logic from RecalcSlipOld and RecalcSlipNew into a new procedure CalculateCustomerUnitPrice, eliminating code duplication.</li><li>New <b>Discount % Decimal Places</b> field to <b>POS Functionality Profile</b> was added, allowing retailers to control how discount percentages are formatted on POS transaction lines. Formatting is applied through the AutoFormatMgt Ext extension.</li><li>Extended IRetailPriceUtils interface with GetStandardCustomerPrice, GetStandardMemberPrice, and CalcPriceInclVat to support unit testing.</li></ul></li><li>POS users with customer-specific pricing will see accurate discount percentages on transaction lines, with configurable decimal precision.</li><li>Currencies with large numbers should have a the correct discount % displayed, instead of zero.</li></ul>
