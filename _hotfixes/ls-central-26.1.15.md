---
title: "LS Central hotfixes - 26.1.15,  Release date August 12, 2025 - Hotfixes"
product: LS Central
version: "26.1.15"
date: 2025-08-12 00:00:00+00:00
---

<strong>69978 Published Offer not showing</strong>
<ul><li><li>Redundant local variable removed, to get access to the results from the <b>GetDirectMarketingInfo WS</b>.</li></li></ul>
<strong>69953 Problem with cancelling orders on Shopify - BC</strong>
<ul><li><li>Posting Customer Order non refundable shipping cost was wrongly done to fixed account. Now it follows normal Sales account.</li></li></ul>
<strong>69882 Customer Orders are not posted at the end of transaction</strong>
<ul><li><li>Added parameter <b>ReturnValue</b> to publisher event <b>OnBeforeApplyFilterToStatusCOReadyForPosting</b>.</li></li></ul>
<strong>69873 Codeunit 99001486 LSC Delete Logs</strong>
<ul><li><li>Bugfix to avoid overflow error on <b>EntryFilter</b> value in <b>Delete Logs</b> codeunit.</li></li></ul>
<strong>69853 SumAmountInclVATByCustomerOrderID calculates in LCY causing error creating Customer Orders</strong>
<ul><li><li>Customer Orders and Sales Orders are now in the same currency when creating SO and CO values.</li></li></ul>
<strong>69827 Skip Validating Pos Data Entry Number Series #553</strong>
<ul><li><li>Event <b>OnBeforeValidateNumberSeries</b> was added in <b>Backoffice Ext</b>.codeunit.</li></li></ul>
<strong>69809 Enable SumIndexFields on key 5 on Transaction Header</strong>
<ul><li><li>Details not available.</li></li></ul>
<strong>69790 Event Request: LS Omni Inventory Endpoint XmlPort Insert Lines</strong>
<ul><li><li>Event <b>OnBeforeInsertPOSTransInvLinesTemp</b> was added to <b>GetDocumentXML</b></li></li></ul>
<strong>69670 Clear IsHandled on FindPromotion loop #552</strong>
<ul><li><li>Details not available.</li></li></ul>
<strong>69668 Make procedure Push accessible in LSC POS Control Event #550</strong>
<ul><li><li>Event <b>OnBeforeAssignActivePanelID</b>was added in <b>Safe Denom. Panel Commands</b>.</li></li></ul>
<strong>69605 Extra Print Eventsubscribtion</strong>
<ul><li><li>Parameters <b>DataEntryTypeCode</b> and <b>InfoNumber</b> were added to event <b>OnBeforeAddFieldValueToTmpStr</b>.</li></li></ul>
<strong>69597 Commit changes for "To Skip UOMPopUp" #549</strong>
<ul><li><li>New event <b>OnBeforeIsUOMPopUp</b> was added to <b>LSC POS Transaction Impl</b> codeunit.</li></li></ul>
<strong>69595 Issue new coupon entry fix, fill "Value Type" based on "Calculation Type" #548</strong>
<ul><li><li>Respect Coupon Header Calculation type field, when creating the coupon entries using web services.</li></li></ul>
<strong>69532 OnBeforeExistEachTransaction Event #546</strong>
<ul><li><li>Event <b>OnBeforeExistEachTransaction</b> was added in <b>POS Transaction</b> codeunit.</li></li></ul>
<strong>69487 This PR adds a public wrapper procedure GetResourceAvailabilityText #541</strong>
<ul><li><li>Access was added to function <b>ShowResourceAvailability</b> in <b>LS Activities functions CU</b>.  The access point is in the hotel integration codeunit.</li></li></ul>
<strong>68667 Incorrect VAT calculation on Sales Order created by Customer Order</strong>
<ul><li><li>Fixed VAT calculation on Sales Order, created by Customer Order.</li></li></ul>
<strong>62087 Flexible bag should start with start amount 0</strong>
<ul><li><li>When you use <b>POS Start Amount Method = Flexible Bag</b>  it should always open the start of day float with amount 0 (as the online help). But it behaved exactly the same as the fixed bag. This was fixed. </li></li></ul>
