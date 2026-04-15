---
title: "LS Central hotfixes - 27.1.15, Release date March 14, 2026 - Hotfixes"
product: LS Central
version: "27.1.15"
subproduct: 
minor_version: "27.1"
date: 2026-03-14 00:00:00+00:00
order: 8
guid: eab93a3779a34eff7a86f86b7230e0b54b130428
---

<strong>79446 AL: Item Distribution status not working</strong>
<ul><li>Shopify Item Push to check for Item Distribution status was fixed, only Active items are added, if not Active, then product is set as Draft or Deleted depending on the setting in Administration page.</li></ul>
<strong>79405 Unable to insert Retail Transfer Order lines after upgraded LS Central Version from 27.1.1.3155 to 27.1.10.3312</strong>
<ul><li>Details not available.</li></ul>
<strong>79380 CO Payment lines amounts in foreign currency</strong>
<ul><li>There was an issue with how payment line in different currency than ledger entry lcy is set to are handled. By putting correct values in Amount and Amount LCY with currency code and factor. This was fixed. </li></ul>
<strong>79135 Page "LSC SB Active Offers" - Query Status Read function error</strong>
<ul><li>Fixed runtime error on page LSC SB Active Offers (10016310) that caused query Status Read function error.<ul><li>Changed to use the explicit enum type reference LSC Toggle Status::Enabled instead, which does not require a data row to be retrieved first.</li><li>Affects users who navigate to the Active Offers page, view the LS Central home page, or print receipts where this page part is embedded.</li></ul></li><li>Changed to use the explicit enum type reference LSC Toggle Status::Enabled instead, which does not require a data row to be retrieved first.</li><li>Affects users who navigate to the Active Offers page, view the LS Central home page, or print receipts where this page part is embedded.</li></ul>
<strong>78879 Sending Transactions using Storage Queue flow - Adding custom events</strong>
<ul><li>New Events were added in Web Replication objects:<ul><li>OnBeforeUpdateTSWTErrorMessage</li><li>OnUploadTransPacketCalled</li><li>OnBeforeSendTransByExternalStorageMessage</li><li>OnAfterSendTransByExternalStorageMessage. </li></ul></li><li>OnBeforeUpdateTSWTErrorMessage</li><li>OnUploadTransPacketCalled</li><li>OnBeforeSendTransByExternalStorageMessage</li><li>OnAfterSendTransByExternalStorageMessage. </li></ul>
<strong>78538 Coupon use on POS with Triggers Offer not resulting in discount</strong>
<ul><li>Only apply the required number of Coupons to a Transaction when using Coupons triggering offer despite how many Coupons were assigned to the Transaction.</li></ul>
<strong>78496 POS EFT Device Requested amount has invalid number of decimal digits</strong>
<ul><li>When calculating the VAT and/or tax amount before sending the tax amount with the card payment request to LS Pay the POS was not using the rounding configurations for amounts. This was fixed.</li></ul>
<strong>77176 Void Posted transaction with DD Void creating entries in trans server work table</strong>
<ul><li>Retry entries in TS Work table for refund transactions are only created if the POS Functionality Profile has TS Send Transaction or DD Send Transactions active.  For example if transactions are replicated to HO.</li></ul>
<strong>76232 Discount Ledger entries not created when posting statement</strong>
<ul><li>Discount Ledger Entries are correctly calculated and updated when posting a Statement (so that Offer Statistics are updated).</li></ul>
