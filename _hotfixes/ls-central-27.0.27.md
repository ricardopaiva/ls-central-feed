---
title: "LS Central hotfixes - 27.0.27, Release date January 20, 2026 - Hotfixes"
product: LS Central
version: "27.0.27"
subproduct: 
minor_version: "27.0"
date: 2026-01-20 00:00:00+00:00
order: 2
guid: d2812fe4b7b188cd611ba99dd2475d01783ece46
---

<strong>76969 Add event OnBeforeTransactionAlreadyProcessed for MemberPostingUtils #618</strong>
<ul><li>A new event, <b>OnBeforeTransactionAlreadyProcessed</b>, was added in procedure TransactionAlreadyProcessed in codeunit Member Posting Utils.</li></ul>
<strong>76940 Add events to extend store attributes #617</strong>
<ul><li>New event <b>OnAfterIsStoreHardAttributeInUse</b> was added on table <b>Attribute Setup.</b></li><li>New events:<ul><li><p style="font-weight: bold;">OnSoftAttributeMgmt_OnAfterFindAttributeCode</p></li><li><p style="font-weight: bold;">OnSetHardAttribValueFromAttrValue_OnAfterFindAttributeFieldNo</p></li><li><p style="font-weight: bold;">OnBeforeIsHardAttribute</p></li><li><p style="font-weight: bold;">OnBeforeIsUsedAsHardAttribute</p></li><li><p style="font-weight: bold;">OnBeforeReturnHardAttributeNo on codeunit, <b>Attribute Utils</b>.</p></li></ul></li><li><p style="font-weight: bold;">OnSoftAttributeMgmt_OnAfterFindAttributeCode</p></li><li><p style="font-weight: bold;">OnSetHardAttribValueFromAttrValue_OnAfterFindAttributeFieldNo</p></li><li><p style="font-weight: bold;">OnBeforeIsHardAttribute</p></li><li><p style="font-weight: bold;">OnBeforeIsUsedAsHardAttribute</p></li><li><p style="font-weight: bold;">OnBeforeReturnHardAttributeNo on codeunit, <b>Attribute Utils</b>.</p></li></ul>
<strong>76773 Global Access Request</strong>
<ul><li>Global access to procedures.</li></ul>
<strong>76724 filter-receiptNo-in-VoidCouponQtyUsed #614</strong>
<ul><li>
<p>Code was added to handle the ALL type option when voiding coupon lines.</p>
</li></ul>
<strong>76433 OnBeforeRetrieveMemberInformation - Result #610</strong>
<ul><li>New parameter was added to <b>OnBeforeRetrieveMemberInformation</b> event.</li></ul>
