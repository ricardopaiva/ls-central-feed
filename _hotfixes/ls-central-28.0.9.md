---
title: "LS Central hotfixes - 28.0.9, Release date May 5, 2026 - Hotfixes"
product: LS Central
version: "28.0.9"
subproduct: 
minor_version: "28.0"
date: 2026-05-05 00:00:00+00:00
order: 2
guid: 7d32019af02295bf342c0cb9e1733670b31fd630
---

<strong>81744 POS fails to launch on BC licenses without LS Activity object range</strong>
<ul><li>There was an issue where launching POS failed with an <b>LSC Activity Front Desk</b> permission error, on tenants whose BC license did not include the LS Activity object range. </li><li>The Activity Front Desk <b>OnBeforeRunPos</b> event subscriber is now skipped when the LS Activity license is missing, allowing POS to open normally for non-Activity customers.</li></ul>
<strong>81685 Integration Events for Item Variants</strong>
<ul><li>The following integration events were added to the relevent objects:<ul><li>Codeunit <b>LSC Product Ext.</b><ul><li>OnCopyFromProductGroupOnBeforeValidateItemVariantFrameworkCode</li></ul></li><li>Page <b>LSC Add a Single Item Variant</b><ul><li>OnBeforeCreateVariant</li></ul></li><li>Page <b>LSC Retail Item Registration</b><ul><li>OnPostToAllItemsOnBeforeCreateExtraTables</li><li>OnPostToPurchOrderOnBeforeModifyPurchaseHeader</li><li>OnPostToPurchOrderOnBeforeCheckFuelItem</li><li>OnPostToPurchOrderOnBeforeRunRetailPurchaseOrderPage</li></ul></li></ul></li></ul>
<strong>81608 AL: Make CustomerOrderEditV2 public</strong>
<ul><li><b>LSCCustomerOrderEditV2Utils</b> was made public.</li></ul>
<strong>81305 BC Shopify April Updates</strong>
<ul><li>Details not available.</li></ul>
<strong>81270 Deal price not displayed correctly in currency in Kiosk</strong>
<ul><li>Currency for deals is now handled correctly in Self Service Kiosk.</li></ul>
<strong>81019 Fix CO Payment LineNo duplication on cancel order</strong>
<ul><li>There was an issue where canceling a Customer Order that included a service item together with two payment lines (loyalty points and card payment) caused an error:<ul><li>The record in table Customer Order Payment already exists. </li><li>The error was due to a <b>Line Number collision</b> on the Customer Order Payment table during the cancel flow, where multiple code paths attempted to insert a new payment entry with the same computed Line Number.</li></ul></li></ul>
<strong>80953 Error when upgrading to version 28.0</strong>
<ul><li>There was an upgrade failure from version 27.1 to 28.0 caused by a new unique key on the LSC Wish List Line table. </li><li>The <b>ItemAndVariantUOM</b> key on table <b>LSC Wish List Line</b> was introduced in version 28.0 with <b>Unique = true</b>. </li><li>Business Central does not allow a new unique key to be added during an upgrade because existing data may contain duplicates, causing Sync-NAVApp to fail. </li><li>The Unique property was removed from the key so the upgrade completes successfully. </li><li>Customers upgrading from version 27.1 to 28.0 or later  no longer encounter a schema sync failure during the upgrade process.</li></ul>
<strong>79773 Publisher Request</strong>
<ul><li>Events were added for KDS and Split bill.</li></ul>
