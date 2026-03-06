---
title: "LS Central hotfixes - 27.1.6, Release date February 18, 2026 - Hotfixes"
product: LS Central
version: "27.1.6"
subproduct: 
minor_version: "27.1"
date: 2026-02-18 00:00:00+00:00
order: 6
guid: b05781478b48189bd76a9c0d6d8ad1343d286cc0
---

<strong>77759 Integration Events for Item Import Journal and Replenishment Calculation</strong>
<ul><li>The following integration events have been added to the below objects:<ul><li>Codeunit <b>LSC Item Import Create</b><ul><li>OnCreateItemOnAfterValidateItemRetailProductCode</li><li>OnCreateItemOnBeforeCreateBarcodes</li><li>OnUpdateItemOnBeforeUpdatePurchasePriceList</li><li>OnCreateVariantOnBeforeIncreaseVariantCode</li><li>OnCreateVariantOnBeforeInsertItemVariant</li></ul></li></ul></li><li>Codeunit <b>LSC Item Import Create</b><ul><li>OnCreateItemOnAfterValidateItemRetailProductCode</li><li>OnCreateItemOnBeforeCreateBarcodes</li><li>OnUpdateItemOnBeforeUpdatePurchasePriceList</li><li>OnCreateVariantOnBeforeIncreaseVariantCode</li><li>OnCreateVariantOnBeforeInsertItemVariant</li></ul></li><li>OnCreateItemOnAfterValidateItemRetailProductCode</li><li>OnCreateItemOnBeforeCreateBarcodes</li><li>OnUpdateItemOnBeforeUpdatePurchasePriceList</li><li>OnCreateVariantOnBeforeIncreaseVariantCode</li><li>OnCreateVariantOnBeforeInsertItemVariant</li><li>
<p>These events are accessible via the public codeunit <b>LSC Item Import Create Public</b>.</p>
</li><li>
<p>Report <b>LSC Add Items to Replen. Jrnl</b></p>
<ul>
<li>OnBeforeAssignReplenTemplateFilters</li>
</ul>
</li><li>OnBeforeAssignReplenTemplateFilters</li><li>Codeunit <b>LSC Franchise Create Outbound Msgs</b><ul><li>OnCreateOutboundMessageOnValueEntrySetFilters</li></ul></li><li>OnCreateOutboundMessageOnValueEntrySetFilters</li><li>Codeunit <b>LSC Franchise Process Documents</b><ul><li>OnCreaProcesPurchDocFromSalesDocOnBeforeValidatePurchLineQty</li><li>OnProcessPurchDocFromSalesDocOnBeforeResetQtyInPurchLine</li><li>OnBeforeCreatePurchCommentLines</li></ul></li><li>OnCreaProcesPurchDocFromSalesDocOnBeforeValidatePurchLineQty</li><li>OnProcessPurchDocFromSalesDocOnBeforeResetQtyInPurchLine</li><li>OnBeforeCreatePurchCommentLines</li><li>
<p>Codeunit <b>LSC Retail ICT Processes</b></p>
<ul>
<li>OnBeforePostItemJnlLineForIJMirror</li>
<li>OnBeforePostGenJnlLineForGLJMirror</li>
<li>OnBeforeIsIJnlLineQtyPosting</li>
<li>OnBeforeCreateICTLinesOnIJnlLineMirror</li>
<li>OnBeforeDestUnitCostOnProcessIJMirror</li>
<li>OnAfterInitItemJournalLineOnProcessIJMirror</li>
<li>OnBeforeReservationEntryInsertOnAddItemTracking</li>
</ul>
</li><li>OnBeforePostItemJnlLineForIJMirror</li><li>OnBeforePostGenJnlLineForGLJMirror</li><li>OnBeforeIsIJnlLineQtyPosting</li><li>OnBeforeCreateICTLinesOnIJnlLineMirror</li><li>OnBeforeDestUnitCostOnProcessIJMirror</li><li>OnAfterInitItemJournalLineOnProcessIJMirror</li><li>OnBeforeReservationEntryInsertOnAddItemTracking</li><li>Codeunit <b>LSC Batch Posting</b><ul><li>OnAfterCreatePrinterSetup</li><li>OnBeforeRunBatchJob</li><li>OnBeforeRunBatchLinkedJobs</li><li>OnAfterInsertNewJobInBatchQueue</li><li>OnBeforeSendEmail</li><li>OnBeforeValidatePurchaseDocument</li></ul></li><li>OnAfterCreatePrinterSetup</li><li>OnBeforeRunBatchJob</li><li>OnBeforeRunBatchLinkedJobs</li><li>OnAfterInsertNewJobInBatchQueue</li><li>OnBeforeSendEmail</li><li>OnBeforeValidatePurchaseDocument</li></ul>
<strong>77144 Refund customer order from HO on POS with a different receipt no.</strong>
<ul><li>It is possible to refund a CO that is finalized with a Sales Order.  The receipt number of the Transaction created is now a regular receipt number, not the Sales Order Number.</li></ul>
<strong>76194 Key in new price disregards price in barcode</strong>
<ul><li>If item has mandatory to key in new price, the price in the barcode is disregarded. Item."Keying in Price" = Item."Keying in Price"::"Must Key in New Price" -&gt; price in barcode not used.</li></ul>
<strong>68683 Improve performance of Adjust Cost job</strong>
<ul><li>Details not available.</li></ul>
<strong>61283 Managing the size of the price history table in SaaS</strong>
<ul><li>Details not available.</li></ul>
