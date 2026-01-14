---
title: "LS Central hotfixes - 27.0.9, Release date November 14, 2025 - Hotfixes"
product: LS Central
version: "27.0.9"
subproduct: 
minor_version: "27.0"
date: 2025-11-14 00:00:00+00:00
order: 17
guid: fc4ace045373238d13b10186b36e85e53e83e168
---

<strong>74494 Integration CU :Access to Exclude Group Parameter (ChangeInternalStatusReservation)</strong>
<ul><li>An access was added to one more parameter in the <b>ChangeInternalStatusReservation</b> function in the hotel integration codeunit.</li></ul>
<strong>74385 StoreInvTransactionSendV2 performance issues tests - III</strong>
<ul><li>Details not available.</li></ul>
<strong>74384 POS Click & Collect - Items Missing After Changed Staff ID - HF</strong>
<ul><li>Do not clear Customer Order temp records when changing Staff ID on Customer Order Collect.</li></ul>
<strong>74382 Trans. Date field value missing in LSC Trans. Sales Entry (Table ID: 99001473) - HF</strong>
<ul><li>Trans. Date and Trans Time field value was missing in LSC Trans. Sales Entry. This was fixed.</li></ul>
<strong>74270 Fix overflow StaffId in PosPrintUtility</strong>
<ul><li>Variable length was extended to avoid text overflow error for StaffId.</li></ul>
<strong>74235 Requests for Events (LSTS-42054)</strong>
<ul><li>Details not available.</li></ul>
<strong>74156 New event WebServicePosLight</strong>
<ul><li>New Event <b>OnReturnCouponHeaderBeforeCheckBarcodeMask</b> was added in Codeunit <b>LSC Web Service POS Light.</b></li></ul>
<strong>74142 ADD EVENT</strong>
<ul><li>Event <b>OnAfterPurchaseDocuments_CalcTotals</b> was added in codeunit <b>LSC Item Variants Functions.</b></li></ul>
<strong>71685 CheckBarcodeMask procedure on LSC Coupon Management is receiving parameters incorrectly</strong>
<ul><li>Details not available.</li></ul>
<strong>41129 Issue when Item (PLU_K) pressed in POS</strong>
<ul><li>New event <b>OnBeforeProcessReceiptBarcode</b> was added to <b>LSC POS Transaction Impl</b> codeunit.</li></ul>
