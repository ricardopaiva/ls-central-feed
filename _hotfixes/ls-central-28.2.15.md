---
title: "LS Central hotfixes - 28.2.15, Release date October 7, 2026 - Hotfixes"
product: LS Central
version: "28.2.15"
subproduct: 
minor_version: "28.2"
date: 2026-10-07 00:00:00+00:00
order: 1
guid: 2f7aae760598774da7a4d373a68bbb7b5ac06501
---

<strong>89016 Retail Messages on Before event request</strong>
<ul><li>New event, <b>OnBeforeRunRequest</b> was added to codeunit LSCRetailMessageGetActiveList/LSCRetailMSGGetActiveListUtil.</li></ul>
<strong>88470 CO Payment Line - Pre Auth not handled on POS Checkout</strong>
<ul><li>There was an issue where a customer order paid with an e-commerce pre-authorization was treated as fully paid at POS checkout, even though the payment was never captured. The e-commerce integration now receives the capture request when you finish the sale, and the payment is recorded.</li><li>This fix applies when you use an e-commerce integration without LS Commerce Server, which means Send LS Commerce Messages is off in Customer Order Setup.</li><li><b>Action required by partners:</b>
<ul>
<li>None.</li>
</ul>
</li></ul>
<strong>87132 Getting issue in fallback return case - hotfixes</strong>
<ul><li>When a card payment reference refund was interrupted during the processing of the card the POS was recreating the payment line with the incorrect sign on the amount in the journal (the payment had a negative number instead of a positive number). This meant that the <b>Balance amount</b> in the POS was duplicated instead of calculated to 0. This was fixed.</li></ul>
