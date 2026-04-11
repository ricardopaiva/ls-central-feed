---
title: "LS Central hotfixes - 27.1.20, Release date March 31, 2026 - Hotfixes"
product: LS Central
version: "27.1.20"
subproduct: 
minor_version: "27.1"
date: 2026-03-31 00:00:00+00:00
order: 1
guid: d599803c51838879c151d6b348b7419eacd7187d
---

<strong>80022 AL: Multiline Value attribute is not syncing to Shopify</strong>
<ul><li>Handle multiline text in <b>Attribute Values</b> when used in Shopify Meta Data.</li></ul>
<strong>79912 Integration Event for Replenishment Transfer Rule #639</strong>
<ul><li>The integration event <b>OnBeforeProcessTransferRule</b> was deprecated in codeunit <b>LSC Replen. Calculation</b>, and replaced with <b>OnBeforeProcessTransferRuleV2</b>, added with an additional parameter ReplenJrnlDetails.</li></ul>
<strong>79601 Implement GetCardData Request in EFT Utility</strong>
<ul><li>Details not available.</li></ul>
<strong>79507 Dining Table Availability does not listen to dining area attributes - BL</strong>
<ul><li>When finding availability for dining reservation through bookings, dining area attributes (Section and preferences) are taken into account. If you have  the <b>Available Tables</b> field visible in the LSC Product Availab. Lookup page, Available Tables shows how many dining tables are available for the number of guests specified and with any section and table preferences selected for the reservation.</li><li>In the Reservation Desk, if you have set a filter on sections, clearing the filter recalculates the availability.</li></ul>
<strong>77100 Option to use Asynchronous Printing through POS Add-In</strong>
<ul><li>Details not available.</li></ul>
