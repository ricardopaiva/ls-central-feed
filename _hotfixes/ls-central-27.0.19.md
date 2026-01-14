---
title: "LS Central hotfixes - 27.0.19, Release date December 16, 2025 - Hotfixes"
product: LS Central
version: "27.0.19"
subproduct: 
minor_version: "27.0"
date: 2025-12-16 00:00:00+00:00
order: 7
guid: 23564074881c37afc0ee7503b7492e27e3b9f540
---

<strong>75727 Publisher after filtering the Sales Lines in LSC Item Variants Functions</strong>
<ul><li>New events were added, <b>OnAfterFilteringSalesLineForCalcTotals</b> and <b>OnAfterFilteringPurchaseLineForCalcTotals</b> in Item Variants Functions codeunit.</li></ul>
<strong>75637 Fix for #572</strong>
<ul><li>Details not available.</li></ul>
<strong>75632 Serial number check in statement</strong>
<ul><li>New event was added, <b>OnBeforeCheckSerialLotValid.</b></li></ul>
<strong>75589 AL: Publish Offer not returning todays offer</strong>
<ul><li>GetDirectMarketingInfo did not return offers, when coupons had end date as today. This was fixed. </li></ul>
<strong>75563 CommerceService - OrderHospCreate - Comments</strong>
<ul><li>OnBeforeInsertFABOrder event was added.</li></ul>
<strong>75561 New Events in codeunit 99001574 LSC POS Transaction events</strong>
<ul><li>Events were added, <b>OnBeforeTransPostingFunctionAddSerialNoAndLotNoTracking</b> and <b>OnBeforePOSTransactionAskForLot.</b></li></ul>
<strong>75559 Add event OnBeforeItemLineCheckRetrievedFromReceipt #598</strong>
<ul><li>New event was added on POS Transaction <b>OnBeforeItemLineCheckRetrievedFromReceipt.</b></li></ul>
<strong>75554 New Events in codeunit 99001456 LSC Statement-Calculate</strong>
<ul><li>New Event was added in codeunit <b>LSC Statement-Calculate OnCheckLotNo</b>.</li></ul>
<strong>75538 KDS - Sending Items to the Kitchen</strong>
<ul><li>Three new events were added to POS Print Utility Public that you can use to:<ul><li>Skip the KOT header text START NOW when firing.</li><li>Only print the lines that are added after the KOT has been announced (skip the lines already announced).</li><li>Skip printing the item details when firing (only print which course should start now).</li></ul></li><li>Skip the KOT header text START NOW when firing.</li><li>Only print the lines that are added after the KOT has been announced (skip the lines already announced).</li><li>Skip printing the item details when firing (only print which course should start now).</li><li>One event was added to KDS Coursing Public, OnCheckAutoFireCourseOnAnnouncing.</li><li>Used for example to autofire a course when it is added after the KOT has been created: A dessert is added when the main has been finished and is autofired. If the starting order includes the dessert, the dessert is not autofired.</li></ul>
<strong>75431 AL: Sales Channel are not syncing</strong>
<ul><li>Publish Sales Channels were added to Shopify to update sales channels for existing Shopify products.</li></ul>
<strong>75308 Fix refunding on POS when collecting and some items have been shortaged or canceled.</strong>
<ul><li>Details not available.</li></ul>
<strong>75295 Invalid customer no. in Transactions (Item number in customer no. field in transactions)</strong>
<ul><li>There was an error when using Item Lookup after adding Member Account/Linked Customer and prompt the infocode. This was fixed.</li></ul>
<strong>75282 Page 10001459 "LSC Retail Item Registration" not accessible</strong>
<ul><li>Details not available.</li></ul>
<strong>75240 Customer paper selection to print report</strong>
<ul><li>Send Paper Width and Height to Hardware Station when printing Custom paper size.</li></ul>
<strong>75067 Issue with Suspended Transaction Retrieval and Re-Suspension</strong>
<ul><li>Details not available.</li></ul>
<strong>75046 Event after CheckBasicData for StoreInventoryLine when processing worksheet in codeunit 10001319 "LSC Store Inventory Management"</strong>
<ul><li>Event, <b>OnAfterCheckBasicData</b> was added to Store Inventory Management.</li></ul>
<strong>75033 POS Line Display adjustment #595</strong>
<ul><li>Details not available.</li></ul>
<strong>74930 New Event OnAfterCreateDataEntryProcessInfoCode #591</strong>
<ul><li>Event, <b>OnAfterCreateDataEntryProcessInfoCode</b> was added in POS Transaction codeunit.</li></ul>
<strong>74929 New events in Member Posting Utils #590</strong>
<ul><li>Events <b>OnBeforeInsertMemberAttributeEntries</b>, <b>OnBeforeUpdateOrInsertDiscTrackingEntry</b> and <b>OnAfterUpdateOrInsertDiscTrackingEntry</b> were added in Member Posting Utils codeunit.</li></ul>
<strong>73820 INVlookup not updating all items</strong>
<ul><li>Details not available.</li></ul>
<strong>73051 POS Exit After Each transaction setup on POS Terminal card generates an error</strong>
<ul><li>There was an error when attempting to get a staff record when staff was logged off. This was fixed. </li></ul>
<strong>64719 We use our own Tender Rounding logic, but we cannot do the same on button which shows exact payment amount QC_EXACT command #599</strong>
<ul><li>A different procedure was used to calculate RoundedBalance.</li></ul>
