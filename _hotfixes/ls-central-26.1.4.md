---
title: "LS Central hotfixes - 26.1.4,  Release date July 8, 2025 - Hotfixes"
product: LS Central
version: "26.1.4"
date: 2025-07-08 00:00:00+00:00
---

<strong>68822 No change in service charge on total press when sales type is changes from dine in to takeaway</strong>
<ul><li><li>If a retail charge is inserted on <b>TotalPressed</b> based on a sales type, and then lines with that sales type, change sales type, or are voided, when <b>TotalPressed</b> is pressed again, the retail charge line becomes voided.</li></li></ul>
<strong>68675 Error in codeunit LSCShopifySchOrder "COpayment already exist with blank DocumentID, Store = web and Line No. 10000</strong>
<ul><li><li>Details not available.</li></li></ul>
<strong>68634 ValidateTaxParameter not working as expected</strong>
<ul><li><li>Event <b>OnBeforeValidationOfTaxCalculation</b> added to Customer Order Line table.</li></li></ul>
<strong>68623 Added OnBeforeOutgoingShopifyImageData event #530</strong>
<ul><li><li>
<p>Shopify Image Events activated</p>
<ul>
<li>
<p><b>OnBeforeOutgoingShopifyImageData2</b>
</p>
</li>
<li>
<p><b>OnAfterProcessShopifyImageData2</b>
</p>
</li>
</ul>
</li></li>
<li><li>
<p><b>OnBeforeOutgoingShopifyImageData2</b>
</p>
</li></li>
<li><li>
<p><b>OnAfterProcessShopifyImageData2</b>
</p>
</li></li>
<li><li>
<p><b>Note:</b> Event will be added to Central 26.1. Central 27 uses GraphQL for images, so these events will not be available there as the process for image uploads are totally different.</p>
</li></li></ul>
<strong>68433 Reprice on refund when member added</strong>
<ul><li><li>Reprice on refund was skipped. This was fixed.</li></li></ul>
<strong>68396 Setting  0 Discount on Payment Lines sets Amount to 0</strong>
<ul><li><li>
<p>The POS allowed the cashier to add a discount to a payment line, which could result in the payment amount being set to 0. This was fixed.</p>
</li></li></ul>
<strong>68248 Valid Offer not triggered in Hospitality POS</strong>
<ul><li><li>Resolved discount was not  applied when the Member Club did not have attributes.</li></li></ul>
<strong>68160 Member card number missing error when editing a CO with member points payment</strong>
<ul><li><li>Updated record on the POS Transactions <b>singleinstance</b> codeunit.</li></li>
<li><li>Fixed an issue on backoffice when opening the Member Card from a Customer order.</li></li></ul>
<strong>68071 Payment difference G/L line in Sales Order linked to CO</strong>
<ul><li><li>Rounding issue was solved when a second Sales Order was created from Customer Order. CO was created for Warehouse delivery. The SO was partly delivered. Then the Customer Order was edited on POS and additional Item was added. That resulted in an abnormal rounding line, created in the second Sales Order.</li></li></ul>
<strong>67527 Transaction goes into Payment mode without Item Lines</strong>
<ul><li><li>Pressing Total is no longer  allowed, unless having at least one POS Trans. Line.</li></li></ul>
<strong>64466 Reprice on refund when member added</strong>
<ul><li><li>Reprice on refund was skipped. This was fixed.</li></li></ul>
