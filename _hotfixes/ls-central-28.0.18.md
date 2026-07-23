---
title: "LS Central hotfixes - 28.0.18, Release date June 2, 2026 - Hotfixes"
product: LS Central
version: "28.0.18"
subproduct: 
minor_version: "28.0"
date: 2026-06-02 00:00:00+00:00
order: 8
guid: 0522f9f37aab8affdd68d179f50c8a7b723a0152
---

<strong>83189 Error when charging to a Reservation</strong>
<ul><li>Charge a reservation at the POS even when its description is longer than 50 characters. Previously the charge failed with a string-length error and the reservation signature slip didn't print.</li><li><b>Action required by partners</b>
<ul>
<li>None. Apply the hotfix. No setup or data changes needed.</li>
</ul>
</li></ul>
<strong>83020 New Integration Event for Add Items to Replen. Journal Report #666</strong>
<ul></ul>
<strong>82968 CO Prepayment - Permission Error</strong>
<ul><li>Permission error was solved, in <b>Statement Post</b> when using prepayment invoices.</li></ul>
<strong>82873 Add integration event for marking selected line before update in refund management #665</strong>
<ul><li>New event <b>OnMarkSelectedLineOnbeforeUpdateAndMarkLine</b> was created in POS Refund Mgt codeunit.</li></ul>
<strong>82839 Add option to change RoleID for Drawers</strong>
<ul><li>New event in POS Transaction Functions.codeunit was added to update drawers to open.</li></ul>
<strong>82817 Added handling before RunBatchJob to skip queue entry processing</strong>
<ul><li>New event was added in Batch Posting Codeunit.</li></ul>
<strong>82704 Error when try to open Options of the attributes</strong>
<ul><li>An error was fixed, when opening the options of an attribute.</li></ul>
<strong>82627 EFT Dialog causes "client callback after write transaction started"</strong>
<ul><li>Card payments through the EFT dialog now run cleanly to the end.</li><li>Previously, finishing a card payment could trigger a runtime error on the POS and add unnecessary processing overhead. Payments now complete reliably and a little faster.</li></ul>
<strong>82619 Issue with Incorrect Discount Calculation in Mix & Match Offer</strong>
<ul><li>Mix &amp; Match Offer is Calculated was fixed, to handle combination of Print bill and split line.</li></ul>
<strong>82364 Retail Item Registration — "Sales Price Incl. VAT" Populated with Ex-VAT Price</strong>
<ul><li><b>Sales Price Incl. VAT</b> was being populated with the ex-VAT unit price when validating an Item No. on a Retail Item Registration line. <ul><li>When a user entered an Item No. on a Retail Item Registration line and the item had <b>Price Includes VAT = false</b> (common in Nordic countries), the <b>Sales Price Incl. VAT</b> field was incorrectly populated with Item."Unit Price" (the ex-VAT price) instead of the VAT-inclusive price. </li><li>This caused the ex-VAT value to be written back to the item's VAT-inclusive price field when running Create/Update Items, effectively double-deflating all prices.</li><li>The fix corrects the field assignment in the table trigger to use the VAT-inclusive price, supporting both Price Module V15 (Item.<b>LSC Unit Price Incl. VAT</b>) and V16 (price list line lookup via LSC Retail Price Utils). </li></ul></li><li>Users who perform Retail Item Registration with items where <b>Price Includes VAT = false</b>  now see the correct VAT-inclusive price in the <b>Sales Price Incl. VAT</b> column and do not experience price deflation when running Create/Update Items.</li></ul>
<strong>82360 AL: Shopify integration: ERR: There is error message in Response XML data</strong>
<ul><li>Collection update in shopify was fixed, to bypass limit of 250 products per collection.</li></ul>
<strong>82300 [CRONUS]Send to KDS field in KDS KOT Overview using Web KDS 27.1</strong>
<ul><li><b>Sent To KDS</b> column was fixed, on the KDS KOT Overview page not being populated when using the <b>POS pushes KOTs to Web KDS</b> service mode.<ul><li>When a restaurant was configured to have the POS push Kitchen Order Tickets directly to Web KDS, the KDS KOT Overview page showed an empty <b>Sent To KDS</b> timestamp for those KOTs even though the KOT itself was delivered successfully.</li><li>This was because the push path did not record the delivery timestamp that the overview page relies on, while the poll-mode path correctly recorded it.</li><li>The fix ensures that after each successful push from the POS to Web KDS, a delivery timestamp is written for every KOT in the pushed batch, bringing push-mode behavior in line with poll mode.</li></ul></li><li>Restaurant operators using the <b>POS pushes KOTs to Web KDS</b> setting  now see the <b>Sent To KDS</b> column correctly populated on the KDS KOT Overview page after KOTs are sent. <ul><li>No configuration changes or schema changes are required. Restaurants using <b>Web KDS polls for new KOTs</b> or Standard KDS are not affected.</li></ul></li></ul>
<strong>82121 Duplicate Article Addition via QR Scan After RFID EPC Scan 2</strong>
<ul><li>There was an issue where the same EPC would be stored with different casing making the EPC not unique in the database. This was fixed. </li></ul>
<strong>81997 FBP Incorrect Reward Calculation with Fractional Quantities</strong>
<ul><li>Details not available.</li></ul>
<strong>81447 Price history cleanup</strong>
<ul><li>Event <b>OnBeforeApplyRetentionPolicyToPriceHistoryTable</b> was added to LSC InstallRetentionPolicy.</li></ul>
<strong>81382 Making a better SetWebKDSRouting</strong>
<ul><li>Making the <b>SetWebKDSRouting</b> give us errors by order and not failling the whole order when one order on the batch fails.</li></ul>
<strong>80455 OrderHospCreate - CurrentAvailability still deducted when orders is not going through</strong>
<ul><li>If a request from ECom fails, it does not decrease the number of Current availability.</li></ul>
<strong>76229 Sales type is not registered from a transaction that is replicated from Mobile POS</strong>
<ul><li>Sales type is now registered from a transaction that is replicated from Mobile POS.</li></ul>
