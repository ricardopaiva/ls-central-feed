---
title: "LS Central hotfixes - 27.0.33, Release date February 24, 2026 - Hotfixes"
product: LS Central
version: "27.0.33"
subproduct: 
minor_version: "27.0"
date: 2026-02-24 00:00:00+00:00
order: 1
guid: 766d385bf02c43e83cab66326fc58be8f49d3c73
---

<strong>78264 Add integration event to enable setting Purchase Header fields before insert trigger</strong>
<ul><li>New event, <b>OnBeforeInsertPurchHeaderOnBeforeRun</b> was added to <b>LSC Store Inventory Process PO</b> codeunit.</li></ul>
<strong>78180 EventSubscriber needed for LSC POS Price Utility Codeunit - Procedure name RegisterMixMatch LS Central OnPrem Version 27.0</strong>
<ul><li>New event, <b>OnAfterCalculateMixMatchDiscountValues</b> was added to <b>LSC POS Price Utility</b> codeunit.</li></ul>
<strong>77916 Bonia MY - Unable to post sales invoice via warehouse shipment who linked with customer order</strong>
<ul><li>Bugfix - Posting zero Amount Sales Order linked to Customer Order resulted in an error.</li></ul>
<strong>77606 SC-3182-Need Event to avoid revalidate on RFID Scanned , EPC when scanning through QR Code</strong>
<ul><li>Details not available.</li></ul>
<strong>77470 POS Printing: FormatStr does not consider fullwidth and halfwidth characters</strong>
<ul><li>A new option was added to Printers. <b>Account for Character Width.</b></li><li>When Printing lines with a mix of fullwidth  (typically East-Asian) and halfwidth characters alignment of the Text would not be correct according the the design (#C###### etc).</li><li>Detecting characters that are fullwidth (2 spaces) and calculating the alignment based on that tries to fix this issue.</li><li><b>Note:</b> The character-set, font, and capabilities of the Printer in question might also have an effect on the alignment of the text.</li><li>More info on full-width vs half-width characters in Unicode. <a href="https://en.wikipedia.org/wiki/Halfwidth_and_fullwidth_forms">https://en.wikipedia.org/wiki/Halfwidth_and_fullwidth_forms</a></li></ul>
<strong>73374 Add a hotfix for the new feature - receipt printer connection selection</strong>
<ul><li>Details not available.</li></ul>
