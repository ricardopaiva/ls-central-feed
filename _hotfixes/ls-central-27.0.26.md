---
title: "LS Central hotfixes - 27.0.26, Release date January 20, 2026 - Hotfixes"
product: LS Central
version: "27.0.26"
subproduct: 
minor_version: "27.0"
date: 2026-01-20 00:00:00+00:00
order: 3
guid: 8aa13c84023c50b5fb8e74a6117d0f45bc9d99b0
---

<strong>76884 POSview.Close changes causes vital code not being run in Hosp POS</strong>
<ul><li>There was an issue with closing the POS, due to obsolete code being removed in 27.0. This was fixed. </li></ul>
<strong>76844 Add Periodic Discount Line as parameter to event to validate price check #616</strong>
<ul><li>New event, <b>OnValidatePriceCheckOnAfterCalcDiscPriceV2</b> was added. </li></ul>
<strong>76751 AL: Method "LogToFile" is marked for removal - MarketUtils Codeunit</strong>
<ul><li>LogToFile, ChopString, GetBlobAsText were made public in MarketUtils codeunit.</li></ul>
<strong>76724 filter-receiptNo-in-VoidCouponQtyUsed #614</strong>
<ul><li>
<p>Code was added to handle the ALL type option when voiding coupon lines.</p>
</li></ul>
<strong>76698 Mandatory station group ID</strong>
<ul><li>Details not available.</li></ul>
<strong>76668 Overflow on KOT to JSON Generation in AL</strong>
<ul><li>There was an overflow error when converting KOTs to JSON. This was fixed. </li></ul>
<strong>76629 AL: Added payment line error</strong>
<ul><li>There was a Line Number Exist error when new Shopify payment line was added to existing payments in Customer order. This was fixed. </li></ul>
<strong>76611 LS New Event "OnBeforeUpdateSHSL"</strong>
<ul><li>New event, <b>OnCreateorderPressedBeforeUpdateSHSL</b> was added. </li></ul>
<strong>76458 Add skip compression condition on POS #611</strong>
<ul><li>Skip compression condition was added on POS.</li></ul>
<strong>76183 After settlement of activity reservation, the transaction has Hotel Reservation No. even if it is not a hotel transaction</strong>
<ul><li>There was an issue with unexpected <b>Hotel Res No.</b> value in Booking POS transactions unrelated to Hotels. This was fixed. </li></ul>
<strong>75167 Fix Record Zoom Validation on Enum fields #597</strong>
<ul><li>Details not available.</li></ul>
<strong>72600 OnBeforeLoadDevice Event</strong>
<ul><li>Details not available.</li></ul>
<strong>59613 Incorrect Pin Message when checking Voucher</strong>
<ul><li>When asking for Gift Card balance on POS and Pin number is required on the <b>POS Data Entry Type</b>,  then the user is prompted for the Pin number (POS Command VIEW_DATAENTRY_BAL).</li></ul>
<strong>33603 Add DirectIO functionality to EFT2 dialog</strong>
<ul><li>Details not available.</li></ul>
