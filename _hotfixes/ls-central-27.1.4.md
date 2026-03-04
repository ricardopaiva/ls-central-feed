---
title: "LS Central hotfixes - 27.1.4, Release date February 11, 2026 - Hotfixes"
product: LS Central
version: "27.1.4"
subproduct: 
minor_version: "27.1"
date: 2026-02-11 00:00:00+00:00
order: 7
guid: fd8925bcc8ab55198ce61e041eda2486bad34afc
---

<strong>77648 Scale Formatting for printing and display</strong>
<ul><li>New events were added to allow localization to comply with scale certification requirements:<ul><li>OnAfterPrintSalesDiscountInfo</li><li>OnBeforeVoidPressed</li></ul></li><li>OnAfterPrintSalesDiscountInfo</li><li>OnBeforeVoidPressed</li><li>To manage prefixes and design strings for printing scale items the following events were added:<ul><li>OnBeforeGetWeightInformationPrefix</li><li>OnBeforeGetManuallyEnteredWeightPrefix</li><li>OnBeforeGetManuallyEnteredWeightDesignString</li><li>OnBeforeGetScaleItemDesignString</li><li>OnBeforeGetManuallyEnteredWeightDesignStringPrintSalesInfoEx</li><li>OnBeforeGetScaleItemDesignStringPrintSalesInfoEx</li><li>OnBeforePrintingWeightInformation</li></ul></li><li>OnBeforeGetWeightInformationPrefix</li><li>OnBeforeGetManuallyEnteredWeightPrefix</li><li>OnBeforeGetManuallyEnteredWeightDesignString</li><li>OnBeforeGetScaleItemDesignString</li><li>OnBeforeGetManuallyEnteredWeightDesignStringPrintSalesInfoEx</li><li>OnBeforeGetScaleItemDesignStringPrintSalesInfoEx</li><li>OnBeforePrintingWeightInformation</li><li>
<p>Previously existing event, <b>OnBeforeEvaluateSaleIsReturnItemPhase1</b> has additional parameters that  allows a localization to decide, if the scale should be asked for the weight when returning and item or if the user can enter the return weight manually.</p>
</li></ul>
<strong>77089 Refund from another store with Sales Type creates incorrect Item Ledger entry</strong>
<ul><li>The Salestype location will not overwrite the store location when doing a refund at a different store.</li></ul>
