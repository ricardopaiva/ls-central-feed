---
title: "LS Central hotfixes - 27.1.17, Release date March 20, 2026 - Hotfixes"
product: LS Central
version: "27.1.17"
subproduct: 
minor_version: "27.1"
date: 2026-03-20 00:00:00+00:00
order: 2
guid: 2bb564af28906445690b27f7e77623066f3be28b
---

<strong>79750 Urgent Event Request for Table 10001313 LSC Store Inventory Line</strong>
<ul><li>New event, <b>OnBeforeCheckItemTypeIsInventory</b> was added to <b>LSC Store Inventory Line</b> table.</li></ul>
<strong>79595 New Integration Events</strong>
<ul><li>The following integration events have been added to the relevant objects:<ul><li>Codeunit <b>LSC Item Import Create</b><ul><li>OnUpdateItemOnBeforeValidateItemFields</li><li>OnUpdateItemOnBeforeCheckVariantDataInJnl</li></ul></li><li>Codeunit <b>LSC Lifecycle Management</b><ul><li>OnActiveDiscountCountOnAfterProcessPeriodicDiscountLine, accessible through the public codeunit <b>LSC Lifecycle Mgt. Public</b>.</li></ul></li><li>Codeunit <b>LSC Item Variants Functions</b><ul><li>OnBeforeVariantFrameworkDelete</li></ul></li><li><p class="RelNotes">Codeunit <b>LSC Replen. Create Purch Order</b></p><ul><li>OnCreatePurchaseOrdersOnAfterInsertPurchaseHeader</li></ul></li></ul></li><li>Codeunit <b>LSC Item Import Create</b><ul><li>OnUpdateItemOnBeforeValidateItemFields</li><li>OnUpdateItemOnBeforeCheckVariantDataInJnl</li></ul></li><li>OnUpdateItemOnBeforeValidateItemFields</li><li>OnUpdateItemOnBeforeCheckVariantDataInJnl</li><li>Codeunit <b>LSC Lifecycle Management</b><ul><li>OnActiveDiscountCountOnAfterProcessPeriodicDiscountLine, accessible through the public codeunit <b>LSC Lifecycle Mgt. Public</b>.</li></ul></li><li>OnActiveDiscountCountOnAfterProcessPeriodicDiscountLine, accessible through the public codeunit <b>LSC Lifecycle Mgt. Public</b>.</li><li>Codeunit <b>LSC Item Variants Functions</b><ul><li>OnBeforeVariantFrameworkDelete</li></ul></li><li>OnBeforeVariantFrameworkDelete</li><li><p class="RelNotes">Codeunit <b>LSC Replen. Create Purch Order</b></p><ul><li>OnCreatePurchaseOrdersOnAfterInsertPurchaseHeader</li></ul></li><li>OnCreatePurchaseOrdersOnAfterInsertPurchaseHeader</li></ul>
<strong>79549 Linked Resources on Matrix</strong>
<ul><li>Details not available.</li></ul>
<strong>79365 New Events</strong>
<ul><li>Seven new integration events were added across three modules in LS Central Core to support client upgrades from BC 14.<ul><li>New events in Microsoft Extension (Discount Ledger), Store Management (Attributes, Inventory, Picking/Receiving), and Web Integrations (Price Sync).</li><li>Events include IsHandled patterns for skipping default logic and notification events for pre/post-processing hooks.</li><li>Breaking change: <b>OnBeforePostItemJnlLine</b> in Picking/Receiving - Post now includes a <b>CountingLines</b> parameter.</li></ul></li><li>New events in Microsoft Extension (Discount Ledger), Store Management (Attributes, Inventory, Picking/Receiving), and Web Integrations (Price Sync).</li><li>Events include IsHandled patterns for skipping default logic and notification events for pre/post-processing hooks.</li><li>Breaking change: <b>OnBeforePostItemJnlLine</b> in Picking/Receiving - Post now includes a <b>CountingLines</b> parameter.</li></ul>
<strong>79348 AL: LSCShopifySchItem (10034382) creates unwanted variants</strong>
<ul><li>Set Lable <b>Title</b>, for Shopify Default variant, to locked so it cannot be translated.</li></ul>
<strong>79117 LSC 26.1 COPY_TR with Discount, auto apply additional total discount upon post sales</strong>
<ul><li>Details not available.</li></ul>
<strong>78882 Bug with Item Point Offer</strong>
<ul><li>Points used as Item Point Offer discounts were not written off when Member Club <b>Min. Trans.Amt for Point Calc.</b> was set, POS now always deducts points used as discounts while still preventing awarding points below the minimum.</li></ul>
<strong>77785 V27 – Incorrect distribution when splitting item by 1/3, 1/4, or 1/? across selected seats</strong>
<ul><li>When splitting a bill to four parts it now splits it correctly.</li></ul>
