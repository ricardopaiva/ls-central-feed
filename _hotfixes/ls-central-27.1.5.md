---
title: "LS Central hotfixes - 27.1.5, Release date February 12, 2026 - Hotfixes"
product: LS Central
version: "27.1.5"
subproduct: 
minor_version: "27.1"
date: 2026-02-12 00:00:00+00:00
order: 7
guid: 62579dbd9edad34a7174fbb9aba6f0b648bbebfe
---

<strong>77759 Integration Events for Item Import Journal and Replenishment Calculation</strong>
<ul><li>The following integration events have been added to the below objects:<ul><li>Codeunit <b>LSC Item Import Create</b><ul><li>OnCreateItemOnAfterValidateItemRetailProductCode</li><li>OnCreateItemOnBeforeCreateBarcodes</li><li>OnUpdateItemOnBeforeUpdatePurchasePriceList</li><li>OnCreateVariantOnBeforeIncreaseVariantCode</li><li>OnCreateVariantOnBeforeInsertItemVariant</li></ul></li><li><p>These events are accessible via the public codeunit <b>LSC Item Import Create Public</b>.</p></li></ul></li><li>Codeunit <b>LSC Item Import Create</b><ul><li>OnCreateItemOnAfterValidateItemRetailProductCode</li><li>OnCreateItemOnBeforeCreateBarcodes</li><li>OnUpdateItemOnBeforeUpdatePurchasePriceList</li><li>OnCreateVariantOnBeforeIncreaseVariantCode</li><li>OnCreateVariantOnBeforeInsertItemVariant</li></ul></li><li>OnCreateItemOnAfterValidateItemRetailProductCode</li><li>OnCreateItemOnBeforeCreateBarcodes</li><li>OnUpdateItemOnBeforeUpdatePurchasePriceList</li><li>OnCreateVariantOnBeforeIncreaseVariantCode</li><li>OnCreateVariantOnBeforeInsertItemVariant</li><li><p>These events are accessible via the public codeunit <b>LSC Item Import Create Public</b>.</p></li><li>Report <b>LSC Add Items to Replen. Jrnl.</b><ul><li>OnBeforeAssignReplenTemplateFilters.</li></ul></li><li>OnBeforeAssignReplenTemplateFilters.</li></ul>
<strong>73290 Return of a transaction from different store</strong>
<ul><li>Previously a transaction from a different store could not be returned when distribution location was configured. This was fixed.</li></ul>
