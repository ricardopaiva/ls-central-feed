---
title: "Hotels hotfixes - 28.0.8 Hotels, Release date May 19, 2026 - Hotfixes"
product: Hotels
version: "28.0.8"
subproduct: Hotels
minor_version: "28.0"
date: 2026-05-19 00:00:00+00:00
order: 50
guid: 6268ddf5b17ab5e1399f1f6302acba237e76a6a2
---

<strong>81687 POS refunds to a customer account does not populate Hotel Reservation Number on Customer Ledger Entries</strong>
<ul><li>Hotel Reservation Number is now populated on Customer Ledger Entries for POS charges and refunds to a customer account.<ul><li>Added subscribers on Statement Post that propagate the Hotel Reservation No. from the source transaction to the resulting customer ledger entry lines.</li><li>Includes a one-time data upgrade that fills the Hotel Res. No. on existing entries (Invoice, Payment, Credit Memo and Refund) created since the regression was introduced.</li></ul></li></ul>
