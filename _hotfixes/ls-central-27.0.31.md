---
title: "LS Central hotfixes - 27.0.31, Release date February 12, 2026 - Hotfixes"
product: LS Central
version: "27.0.31"
subproduct: 
minor_version: "27.0"
date: 2026-02-12 00:00:00+00:00
order: 1
guid: de7501fa7b3f05a829b776b3aae3e069dc08f7fc
---

<strong>77837 Items Sync to Shopify is deleting the prices</strong>
<ul><li>Check was added to Shopify product update to not include 0 price values.</li></ul>
<strong>77648 Scale Formatting for printing and display</strong>
<ul><li>New events were added to allow localization to comply with scale certification requirements:<ul><li>OnAfterPrintSalesDiscountInfo</li><li>OnBeforeVoidPressed</li></ul></li><li>OnAfterPrintSalesDiscountInfo</li><li>OnBeforeVoidPressed</li><li>To manage prefixes and design strings for printing scale items the following events were added:<ul><li>OnBeforeGetWeightInformationPrefix</li><li>OnBeforeGetManuallyEnteredWeightPrefix</li><li>OnBeforeGetManuallyEnteredWeightDesignString</li><li>OnBeforeGetScaleItemDesignString</li><li>OnBeforeGetManuallyEnteredWeightDesignStringPrintSalesInfoEx</li><li>OnBeforeGetScaleItemDesignStringPrintSalesInfoEx</li><li>OnBeforePrintingWeightInformation</li></ul></li><li>OnBeforeGetWeightInformationPrefix</li><li>OnBeforeGetManuallyEnteredWeightPrefix</li><li>OnBeforeGetManuallyEnteredWeightDesignString</li><li>OnBeforeGetScaleItemDesignString</li><li>OnBeforeGetManuallyEnteredWeightDesignStringPrintSalesInfoEx</li><li>OnBeforeGetScaleItemDesignStringPrintSalesInfoEx</li><li>OnBeforePrintingWeightInformation</li><li>
<p>Previously existing event, <b>OnBeforeEvaluateSaleIsReturnItemPhase1</b> has additional parameters that  allows a localization to decide, if the scale should be asked for the weight when returning and item or if the user can enter the return weight manually.</p>
</li></ul>
<strong>73290 Return of a transaction from different store</strong>
<ul><li>Previously a transaction from a different store could not be returned when distribution location was configured. This was fixed.</li></ul>
<strong>70941 SCO Performance testing</strong>
<ul><li>Details not available.</li></ul>
<strong>60835 Missing float difference</strong>
<ul><li>Details not available.</li></ul>
