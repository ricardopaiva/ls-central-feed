---
title: "LS Central hotfixes - 27.1.8, Release date February 24, 2026 - Hotfixes"
product: LS Central
version: "27.1.8"
subproduct: 
minor_version: "27.1"
date: 2026-02-24 00:00:00+00:00
order: 1
guid: 2c4ca4e8ad23e37981eaac1a34d43dcad658b198
---

<strong>78389 AL: Payment failure gets added to order</strong>
<ul><li>There was an issue with excluding Shopify order payment line that had status error or failed in Customer Order This was fixed. </li></ul>
<strong>78294 Bookings package manager high severity issues</strong>
<ul><li>Details not available.</li></ul>
<strong>78264 Add integration event to enable setting Purchase Header fields before insert trigger</strong>
<ul><li>New event, <b>OnBeforeInsertPurchHeaderOnBeforeRun</b> was added to <b>LSC Store Inventory Process PO</b> codeunit.</li></ul>
<strong>78180 EventSubscriber needed for LSC POS Price Utility Codeunit - Procedure name RegisterMixMatch LS Central OnPrem Version 27.0</strong>
<ul><li>New event, <b>OnAfterCalculateMixMatchDiscountValues</b> was added to <b>LSC POS Price Utility</b> codeunit.</li></ul>
<strong>78177 Make IsStoreHardAttributeInUse and HardAttributeMgmt procedures public</strong>
<ul><li><b>IsStoreHardAttributeInUse and HardAttributeMgmt</b> procedures were made public.</li></ul>
<strong>78160 Add new integration events</strong>
<ul><li>New events were added to <b>LSC Picking/Receiving - Post</b> and <b>LSC Picking/Receiving Confirm</b> codeunit.</li></ul>
<strong>77916 Bonia MY - Unable to post sales invoice via warehouse shipment who linked with customer order</strong>
<ul><li>Bugfix - Posting zero Amount Sales Order linked to Customer Order resulted in an error.</li></ul>
<strong>77881 Change in Z report</strong>
<ul><li>New event, <b>OnAfterFilterPaymEntryOnPrintXZReport</b> was added to <b>LSC POS Print Utility Impl</b> codeunit.</li></ul>
<strong>77823 EventSubscriber needed for LSC Retail Price Utils Codeunit - Procedure name FindPromotion LS Central OnPrem Version 27.0</strong>
<ul><li>New event, <b>OnBeforeFilterDiscOfferOnFindPromotion</b> was added to <b>LSC Retail Price Utils</b> codeunit.</li></ul>
<strong>77800 Incorrect Income/expense entry</strong>
<ul><li>Details not available.</li></ul>
<strong>77606 SC-3182-Need Event to avoid revalidate on RFID Scanned , EPC when scanning through QR Code</strong>
<ul><li>Details not available.</li></ul>
<strong>75150 Returning item that has quantity less than 1</strong>
<ul><li>When returning items the configuration on the Item card: <b>Qty not in Decimals</b> is used to determine if an item can be sold or returned in quantities with decimals and with a quantity below 1.</li><li>When returning a scale item the item is now automatically marked as <b>Manually weighted item</b>.</li></ul>
<strong>75118 Returning a scale item, line should be marked as "Manually weighted item"</strong>
<ul><li>When returning a scale item the item is now automatically marked as <b>Manually weighted item</b>.</li></ul>
