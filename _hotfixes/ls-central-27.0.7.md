---
title: "LS Central hotfixes - 27.0.7, Release date November 7, 2025 - Hotfixes"
product: LS Central
version: "27.0.7"
subproduct: 
minor_version: "27.0"
date: 2025-11-07 00:00:00+00:00
order: 6
guid: 1f5eab0d44bf3447f5e3e88a29705e4f4319d3fe
---

<strong>74292 HOTFIX request for Issue 71599</strong>
<ul><li>New field <b>LSC Block UnderTender Compl.</b> was added on Retail currency. This field allows, avoid transaction to be completed if the balance is less than the lowest acceptable denomination amount, requiring the remaining amount to be paid by another tender type.</li></ul>
<strong>74219 Store Inventory Line performance improvement</strong>
<ul><li>Details not available.</li></ul>
<strong>74153 Fix Lookup Users page in License Manager User assignment</strong>
<ul><li>There was an issue where no Users or too many Users would be displayed when the Assign Base Units Lookup page. This was fixed. </li></ul>
<strong>73943 POS Calc. Member Points - RetrieveMemberInformation</strong>
<ul><li>New event <b>OnBeforeRetrieveMemberInformation</b>was added to <b>LSC POS Calc. Member Points</b> codeunit.</li></ul>
<strong>73794 Adding a subscriber on CheckMSRcards</strong>
<ul><li>New event <b>OnBeforeCheckMSRCardInput</b> was added to <b>LSC POS Transaction Impl</b> codeunit.</li></ul>
<strong>73717 LS Central Offer Configuration Query</strong>
<ul><li>Details not available.</li></ul>
<strong>73527 LSC NA - Inconsistent Unit Price (normal item) on Split Bills</strong>
<ul><li>There was an issue with the unit price. It must be unchanged (original price) when performing the Split All Even. This was fixed.</li></ul>
<strong>73233 limit Periodic Discounts on LoadOfferTables procedure</strong>
<ul><li>Three new events were added in POS Functions codeunit.</li></ul>
<strong>69737 Call Center -KOT Font Configuration Not Retained After POS Restart</strong>
<ul><li>Call Center: The font on the kitchen printout was not retained after POS restart. This was fixed.</li></ul>
