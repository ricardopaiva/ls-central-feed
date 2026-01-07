---
title: "LS Central hotfixes - 27.0.22, Release date December 23, 2025 - Hotfixes"
product: LS Central
version: "27.0.22"
subproduct: 
minor_version: "27.0"
date: 2025-12-23 00:00:00+00:00
order: 3
guid: a94575d2524487fb9bce407a5b62f2341f1ab149
---

<strong>76255 Not available status wrong in allocation panel</strong>
<ul><li>Available Status was fixed in Allocation Panel. Dining Table is correctly shown <b>not available</b>.</li></ul>
<strong>76113 Changing priorities adjusted event</strong>
<ul><li>New event <b>OnBeforeModifyPriorities</b>  was added in table <b>LSC Periodic Discount.</b></li></ul>
<strong>76107 Fix EFT Post Transaction After Void on ProcessInfoCode</strong>
<ul><li>Details not available.</li></ul>
<strong>76099 P/R lines - New event-publishers OnAfterSetFiltersOnCheckReceivingOrder & OnAfterSetFiltersOnCheckPickingOrder</strong>
<ul><li>New events <b>OnAfterSetFiltersOnCheckReceivingOrder</b> and <b>OnAfterSetFiltersOnCheckPickingOrder</b> were added in table <b>LSC Picking / Receiving lines.</b></li></ul>
<strong>76098 Add event OnBeforeSafeManagementCheck on codeunit LSC Statement-Post</strong>
<ul><li>New event <b>OnBeforeSafeManagementCheck</b> was added in <b>LSC Statement-Post</b> codeunit.</li></ul>
<strong>76093 Event Publisher for CLE creation in Statement Posting</strong>
<ul><li>New event <b>OnBeforeCLESkip</b>  was added in <b>LSC Statement-Post</b> codeunit.</li></ul>
<strong>76009 Integration Event for Replenishment Effective Inventory Calculation</strong>
<ul><li>The integration event <b>OnAfterCalculateEffectiveInventory</b> was added to the codeunit <b>LSC Replen. Calculation</b>.</li></ul>
<strong>75903 AL: Shopify Order Import LS 27</strong>
<ul><li>Procedure <b>InsertOrderToBuffer</b> was restored to public. New Event was added, before pull request is sent to Shopify: <b>OnBeforeShopifyOrderPull</b>.</li></ul>
<strong>75159 POS Card Entry, replication counter not working</strong>
<ul><li>Replication counter was fixed.</li></ul>
<strong>72292 GS1 procedures made public and some refactoring</strong>
<ul><li>GS1 Barcode functionality was made public for both versions through the GS1 Barcode Public codeunit.</li></ul>
<strong>71575 Fix EFT Post Transaction After Void on ProcessInfoCode</strong>
<ul><li>Details not available.</li></ul>
<strong>63599 Discount Offers standard Business Central Variants</strong>
<ul><li>Details not available.</li></ul>
