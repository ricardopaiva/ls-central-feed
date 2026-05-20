---
title: "LS Central hotfixes - 28.0.2, Release date April 15, 2026 - Hotfixes"
product: LS Central
version: "28.0.2"
subproduct: 
minor_version: "28.0"
date: 2026-04-15 00:00:00+00:00
order: 14
guid: bd2be89a88821c46fcdd6864aa0f95aa32506ddb
---

<strong>80633 Unable to create open statement (Document No length more than 10) version 27.1.21.3433</strong>
<ul><li>There was an issue introduced in v27.1.21 that would not allow the user to create an open statement under certain circumstances, when the Statement No. had more than 10 characters. This was fixed. </li></ul>
<strong>80612 New publishers in Shopify Integration</strong>
<ul><li>New order create events were added from Shopify:<ul><li>OnBeforeInsertCOShippingLineTemp</li><li>OnBeforeInsertTotalDiscountLineTemp</li><li>OnBeforeInsertCODiscountLineTemp</li><li>OnBeforeInsertCODPaymentTemp.</li></ul></li></ul>
<strong>80598 Move The Waiver Report within the Repo to General Reports directory so its available to the user in runtime</strong>
<ul><li>The Waiver Report was added to the Repo in the General Reports directory.</li></ul>
<strong>80484 Make AssignMemberAttributes procedures public</strong>
<ul><li>Two procedures were made public on codeunit <b>LSC Member Attribute Mgmt</b> (99009002) to allow external extensions to assign member attributes:</li></ul>
<strong>80385 Skip barcode creation</strong>
<ul><li><b>OnBeforeAssignBarcode_OnCreateVariantAction</b> integration event was added on page LSC Item Variant Suggestion, allowing extensions to skip automatic barcode creation during the Create Variants action.</li></ul>
<strong>80374 Tanweer_31.03.2026 #642 Retail Message Panel Control CU</strong>
<ul><li>Displays an error text when an error occurs on the Retail Message Panel.</li></ul>
<strong>80373 Add integration events for various processes and enhance existing fun</strong>
<ul><li><b>New Integration Events</b>
<ul>
<li><b>LSC CO Customer Info Panel</b>
<ul>
<li>OnAfterButtonPress_OnRun</li>
</ul>
</li>
<li><b>LSC CO Utility</b>
<ul>
<li>OnAfterCustomerOrderPayment</li>
<li>OnAfterInsertCOLines_CreateCOTempFromPOSTransaction</li>
</ul>
</li>
<li><b>LSC CO Create Panel</b>
<ul>
<li>OnBeforeEditMemberContact</li>
<li>OnBeforeModifyDataBuffer_OnLookupResult</li>
</ul>
</li>
<li><b>LSC CO Sched. Jobs</b>
<ul>
<li>OnBeforePostSalesOrders</li>
</ul>
</li>
<li><b>LSC CO Web Service Functions</b>
<ul>
<li>OnBeforeInsertCOHeaderTemp_OnReserveOrderLines</li>
<li>OnBeforeItemTrackingValidations_OnSetupItemAndDiscountLines</li>
</ul>
</li>
<li><b>LSC CO eCommerce Mgt</b>
<ul>
<li>OnAfterCreateTransaction</li>
</ul>
</li>
<li><b>LSC Dashboard Alarms Public (new codeunit)</b>
<ul>
<li>OnAfterCheckRoleStoreAlerts</li>
</ul>
</li>
<li><b>LSC Item Finder Public (new codeunit)</b>
<ul>
<li>OnBeforeProcessItemFinderSetup_OnFindItemSet</li>
</ul>
</li>
<li><b>LSC Retail Purchase Order Ext.</b>
<ul>
<li>OnBeforePurchaseHeaderOrderAddressCodeOnAfterValidateEvent</li>
</ul>
</li>
<li><b>LSC Retail Sales Order Ext.</b>
<ul>
<li>OnBeforeOnAfterFinalizePosting</li>
</ul>
</li>
<li><b>LSC Retail ICT Processes</b>
<ul>
<li>OnBeforeAddItemTracking</li>
<li>OnBeforeProcessICTHeader_OnProcessICTDocSplit</li>
</ul>
</li>
<li><b>LSCCreateNewCardForContUtils</b>
<ul>
<li>OnBeforeInsertMemberCard_OnRunRequest</li>
</ul>
</li>
<li><b>LSCGetMemberInfoForPosUtils</b>
<ul>
<li>OnBeforeGetMemberCouponList_OnRunRequest</li>
</ul>
</li>
<li><b>LSCGetDataEntryUtils</b>
<ul>
<li>OnBeforeRunRequest</li>
</ul>
</li>
</ul>
</li><li>Modified Event<ul><li><b>LSC CO Web Service Functions</b><ul><li>OnBeforeShouldCreateSalesorderCheck - added RunFromScheduler: Boolean parameter.</li></ul></li></ul></li></ul>
<strong>80372 Adding Event OnBeforeValidateJournalLine in Point Jnl.-Check Line</strong>
<ul><li>An event was added, <b>OnBeforeValidateJournalLine</b> in codenit Point Jnl.-Check Line.</li></ul>
<strong>80357 AL: Issue with translations</strong>
<ul><li>Shopify translation error was fixed: The record in table <b>Shopify Locale Data</b> already exists.</li></ul>
<strong>79972 Bug in Prepayment Invoices</strong>
<ul><li>Details not available.</li></ul>
<strong>79600 EventSubscriber needed for LSC POS View Codeunit - Procedure name LoginEx LS Central OnPrem Version 27.1</strong>
<ul><li>Details not available.</li></ul>
<strong>79075 Runtime error in Codeunit 99009601 due to type mismatch between Integer and Decimal fields.</strong>
<ul><li>FBP quantities should always be in whole number. If Quantity sold on POS is 2.4 then it is rounded to 2. 2.5 is rounded to 3. </li><li>FBP quantities should always be displayed as integers as for example Quantity. Quantity to Trigger, Remaining Quantity in FBP Ledger Entry.</li><li><b>Note</b>: <b>Notify Data Row Selected</b> in POS Data Grid Control Card - ##DEFAULT, #MEMBER_FBP_OVERVIEW in demodata must be turned OFF for the Frequent Buyer Program panel to work on POS. Instead turn <b>Notify Marked Count Changed</b> ON.</li></ul>
<strong>77313 Multiple pcs lines are printing without a currency symbol (Measurements Canada requirements)</strong>
<ul><li>Details not available.</li></ul>
