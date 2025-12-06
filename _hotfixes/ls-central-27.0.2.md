---
title: "LS Central hotfixes - 27.0.2, Release date October 21, 2025 - Hotfixes"
product: LS Central
version: "27.0.2"
subproduct: 
minor_version: "27.0"
date: 2025-10-21 00:00:00+00:00
order: 17
guid: 89216a0698199b7f7caa6044f71d6f1b94fcd3cb
---

<strong>73373 Shopify question - Discount offers</strong>
<ul><li>Price and Discount replication to Shopify where discount value updates were not included. This was fixed. </li></ul>
<strong>73049 Integration Event For Forecast Factor Calculation</strong>
<ul><li>The integration event <b>OnCalculateForecastFactor</b> was replaced by <b>OnCalculateForecastFactorV2</b> in the codeunit <b>LSC Replen. Calculation</b>.</li></ul>
<strong>72966 Integration Event for Item Variant Framework Code</strong>
<ul><li>The integration event <b>OnBeforeConfirmOnValidateVariantFrameworkCode</b> was added to the codeunit <b>LSC Item - Control Public</b>, used by the <b>LSC Variant Framework Code field</b> in Item table extension.</li></ul>
<strong>72940 Integration Event For Replenishment Template</strong>
<ul><li>The integration event <b>OnAfterAssignReplenishmentTemplateFilter</b> was added to the <b>LSC Add Items to Replen. Jrnl</b> report.</li></ul>
