---
title: "Autotests hotfixes - 29.0.8 Autotests, Release date November 27, 2026 - Hotfixes"
product: Autotests
version: "29.0.8"
subproduct: Autotests
minor_version: "29.0"
date: 2026-11-27 00:00:00+00:00
order: 9
guid: f0a56738f686821fd964fd51f2d5853f504a5012
---

<strong>87157 PAYM_ACC_INV POS Command – Payment Amount Not Cleared After Invalid Input</strong>
<ul><li>Paying an invoice into a Customer Account now allows entering new amount if you enter amount higher than the Invoice balance.</li><li>Previously, POS kept reusing the rejected amount, so every retry failed instantly until you restarted the POS.</li></ul>
<strong>91834 Customer Order Sale and Return in Same Transaction</strong>
<ul><li>Block negative prices keyed in while adding an item to a transaction that has a customer order line. The POS now shows <b>You can not mix return quantity/negative amount and Customer Order in the same Transaction</b>, as it already does when you change a price. Before, a deposit item rung up at a negative price against a new order was not recorded on the order. The order then showed as unpaid, and the statement could not be posted.</li><li><b>Action required by partners:</b></li><li>  ◦ None.</li></ul>
<strong>92468 Referenced refund is not working in the new card engine</strong>
<ul><li>A check to make sure that a referenced refund payment was being done on the correct Card payment engine was not working properly and was stopping the user from doing a referenced refund regardless of Card payment engine selection.</li><li>This was fixed.</li></ul>
<strong>92629 Possibility to Post Statement in background with skipping check as user can</strong>
<ul><li>Post statements in the background without the pre-posting question. Extensions can now step in when the posting question would otherwise stop posting because there is no user interface, such as in a job queue session.</li><li>If an extension handles it, posting continues without an error. Without such an extension, nothing changes and posting is still cancelled with <b>Posting was cancelled.</b> The Max. Diff. to Allow Post. error and the blocked item and customer checks work as before.</li><li><b>Action required by partners:</b></li><li>  ◦ None. To post statements in the background, develop an extension that handles the new event in the statement posting.</li></ul>
<strong>92756 Customer order collection on POS fails when the store language is not English: SetView error in "LSC CO Collect PreAuth Tender"</strong>
<ul><li>Collect customer orders at the POS without errors when the store language is not English. Before, collecting a web customer order failed when the store's language was set to Croatian, for example. Collection now works the same as with an English store.</li><li><b>Action required by partners:</b></li><li>  ◦ None.</li></ul>
<strong>92759 Statement posting fails with "Prepayment invoice account not found" for customer orders paid on account (after #89177)</strong>
<ul><li>Post statements for customer orders paid in full on account without errors. Before, posting failed with <b>Prepayment Invoice Posting Account was not found</b> when <b>Use Prepayment Invoices</b> was on.</li><li>The on-account amount is not posted by the statement. The final sales invoice creates the receivable, so customers are not charged twice.</li><li><b>Action required by partners:</b></li><li>  ◦ None.</li></ul>
<strong>92991 PAYM_ACC_INV POS Command – Payment Amount Not Cleared After Invalid Input</strong>
<ul><li>Paying an invoice into a Customer Account now allows entering new amount if you enter amount higher than the Invoice balance.</li><li>Previously, POS kept reusing the rejected amount, so every retry failed instantly until you restarted the POS.</li></ul>
