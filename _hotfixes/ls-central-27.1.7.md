---
title: "LS Central hotfixes - 27.1.7, Release date February 19, 2026 - Hotfixes"
product: LS Central
version: "27.1.7"
subproduct: 
minor_version: "27.1"
date: 2026-02-19 00:00:00+00:00
order: 2
guid: 2411f16804d6b90124afad7a4985157599ec9b18
---

<strong>78202 AL: Inventory Synchronization Failure</strong>
<ul><li>There was an issues with Shopify Inventory update where Item qty was 0 or less the update was not sent to Shopify. This was fixed. </li></ul>
<strong>78188 Add events for routing with priority by store</strong>
<ul><li>Details not available.</li></ul>
<strong>77858 Event Modify Request IncludeSender in POS Controller</strong>
<ul><li>Details not available.</li></ul>
<strong>77470 POS Printing: FormatStr does not consider fullwidth and halfwidth characters</strong>
<ul><li>A new option was added to Printers. <b>Account for Character Width.</b></li><li>When Printing lines with a mix of fullwidth  (typically East-Asian) and halfwidth characters alignment of the Text would not be correct according the the design (#C###### etc).</li><li>Detecting characters that are fullwidth (2 spaces) and calculating the alignment based on that tries to fix this issue.</li><li><b>Note:</b> The character-set, font, and capabilities of the Printer in question might also have an effect on the alignment of the text.</li><li>More info on full-width vs half-width characters in Unicode. <a href="https://en.wikipedia.org/wiki/Halfwidth_and_fullwidth_forms">https://en.wikipedia.org/wiki/Halfwidth_and_fullwidth_forms</a></li></ul>
<strong>73374 Add a hotfix for the new feature - receipt printer connection selection</strong>
<ul><li>Details not available.</li></ul>
<strong>73341 Store Coupon - Item Modifiers are not discounted</strong>
<ul><li>Setup, <b>Affect Linked Item</b> was added on store coupon to apply coupons to all linked items.</li></ul>
<strong>70166 Multicurrency in ecom</strong>
<ul><li>With the addition of the new fields <b>Currency Code</b> and <b>Currency Factor</b> on the <b>Customer Order Header</b>, multicurrency support was enhanced for Customer Orders. </li><li>The update ensures consistent currency handling between Ecom, LS Central, and POS, supporting order creation and processing in non-LCY currencies while keeping amounts and currency codes aligned across Customer Orders, Sales Orders, and Transactions.</li></ul>
