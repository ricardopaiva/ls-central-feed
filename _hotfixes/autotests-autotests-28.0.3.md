---
title: "Autotests hotfixes - 28.0.3  Autotests, Release date April 21, 2026 - Hotfixes"
product: Autotests
version: "28.0.3"
subproduct: Autotests
minor_version: "28.0"
date: 2026-04-21 00:00:00+00:00
order: 25
guid: 0278cc8a9449b776f4b2d6bd525e980792e045a3
---

<strong>80599 Currency rounding issue and insufficient memory</strong>
<ul><li><b>SnapPaymentToBalanceOnCurrencyRounding</b> was added to snap payment amount to balance when the difference is within currency rounding tolerance during foreign-currency payments.</li></ul>
<strong>80042 When Fully Canceling an Order the "Receipt No." and "Transaction No." on the "LSC Customer Order Status Log" is blank</strong>
<ul><li>Receipt No. and Transaction No. were not populated in the Line Status Changes FactBox when a Customer Order was fully canceled on POS.</li><li>This only affected full order cancelations, while partial cancelations worked correctly. </li><li>LS Central now ensures these values are properly assigned, improving traceability for canceled orders.</li></ul>
<strong>79850 Receipt alignment mismatch - detecting the full-width characters wrongly</strong>
<ul><li>Details not available.</li></ul>
<strong>74340 Statement Batch Posting Problem</strong>
<ul><li>Validation was added, if a <b>Posted Statement</b> with the same number already exist.</li><li>The <b>Open Statement</b> page is closed after posting.</li></ul>
