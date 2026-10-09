---
title: "Autotests hotfixes - 28.2.13 Autotests, Release date October 7, 2026 - Hotfixes"
product: Autotests
version: "28.2.13"
subproduct: Autotests
minor_version: "28.2"
date: 2026-10-07 00:00:00+00:00
order: 15
guid: d5a2099a0a3dddc86ca9902467a4d1fea33c9430
---

<strong>89016 Retail Messages on Before event request</strong>
<ul><li>New event, <b>OnBeforeRunRequest</b> was added to codeunit LSCRetailMessageGetActiveList/LSCRetailMSGGetActiveListUtil.</li></ul>
<strong>88470 CO Payment Line - Pre Auth not handled on POS Checkout</strong>
<ul><li>There was an issue where a customer order paid with an e-commerce pre-authorization was treated as fully paid at POS checkout, even though the payment was never captured. The e-commerce integration now receives the capture request when you finish the sale, and the payment is recorded.</li><li>This fix applies when you use an e-commerce integration without LS Commerce Server, which means Send LS Commerce Messages is off in Customer Order Setup.</li><li><b>Action required by partners:</b>
<ul>
<li>None.</li>
</ul>
</li></ul>
