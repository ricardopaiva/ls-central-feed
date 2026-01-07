---
title: "LS Central hotfixes - 27.0.15, Release date November 25, 2025 - Hotfixes"
product: LS Central
version: "27.0.15"
subproduct: 
minor_version: "27.0"
date: 2025-11-25 00:00:00+00:00
order: 10
guid: a2e07f75e8a823a3473587198873a14c5bed689e
---

<strong>75007 Handling of a 100% discount on a Deal during the reservation process in the POS system</strong>
<ul><li>There was an issue in the PUSH2EVENTS POS command that caused discounts assigned on deals on the POS to be not correctly transferred to the reservation additional items. This was fixed. </li></ul>
<strong>74932 Add public function PrintCustomerSlip to CU LSC POS Print Utility #592</strong>
<ul><li><b>PrintCustomerSlip</b> was added as public function in POS Print Utility Public.</li></ul>
<strong>74801 Active line not moving when adding Activity Items</strong>
<ul><li>When inserting activity product line to a POS journal,  the related text lines are activated for scrolling purposes, but at the end of the insertion to the POS journal the product journal lines are activated as the selected line, so if the user needs to void er change, the line is by default the selected journal line.</li></ul>
<strong>74773 Customer Order Emails</strong>
<ul><li>
<p>Var to MessageSubject, MessageBody, HtmlFormated parameters were added in the <b>LSC CO Shipping Message Public Codeunit  OnBeforeSendMessageto Publisher</b>.</p>
</li></ul>
<strong>74736 SC-2978-"Entry Type" field in table "LSC POS Voided Trans. Line" required as extensible Enum like in table "LSC POS Trans. Line"</strong>
<ul><li>Field <b>Entry Type</b> from <b>LSC POS Voided Trans. Line</b> table was changed into enum.</li></ul>
<strong>74636 Performance issue with Activity Resource Unavailability after upgrade to LS Central 26.1</strong>
<ul><li>A performance issue was fixed on the <b>Resource Unavailability</b> page.  When the page is checking if unavailability conflicts with existing reservations, the logic was extremely slow when unavailability entry was covering large period.  This was fixed.</li></ul>
<strong>74286 Pricing Fast Tab is not visible in item card</strong>
<ul><li>Old Pricing Functions were made accessible in <b>Retail Item Card</b>.</li></ul>
