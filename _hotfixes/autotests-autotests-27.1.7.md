---
title: "Autotests hotfixes - 27.1.7 Autotests, Release date March 14, 2026 - Hotfixes"
product: Autotests
version: "27.1.7"
subproduct: Autotests
minor_version: "27.1"
date: 2026-03-14 00:00:00+00:00
order: 23
guid: 016c6d79f880d11bde3b57db9e451742c94a25dc
---

<strong>77176 Void Posted transaction with DD Void creating entries in trans server work table</strong>
<ul><li>Retry entries in TS Work table for refund transactions are only created if the POS Functionality Profile has TS Send Transaction or DD Send Transactions active.  For example if transactions are replicated to HO.</li></ul>
<strong>76232 Discount Ledger entries not created when posting statement</strong>
<ul><li>Discount Ledger Entries are correctly calculated and updated when posting a Statement (so that Offer Statistics are updated).</li></ul>
