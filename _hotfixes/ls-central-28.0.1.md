---
title: "LS Central hotfixes - 28.0.1, Release date April 14, 2026 - Hotfixes"
product: LS Central
version: "28.0.1"
subproduct: 
minor_version: "28.0"
date: 2026-04-14 00:00:00+00:00
order: 1
guid: 08f7cd4fae41145cc8c85ddfbedffdec6ac34225
---

<strong>79652 Suspend Transaction - Receipt No. on POS Not Incrementing Properly When Using Web Replication and Retrieving and Re-Suspending Previous Transactions</strong>
<ul><li>There was an issue where POS receipt numbers could collide when retrieving and re-suspending transactions with web replication (TS Susp./Retrieve) enabled.<ul><li>When a previously suspended transaction was retrieved and re-suspended, the POS receipt number counter could go backwards, causing the next transaction to reuse a receipt number already assigned to another suspended transaction on the remote company.</li><li><p>The LastSlipNo POS tag now only updates when the receipt number is higher than the current value, preventing it from being overwritten with a lower number.</p></li></ul></li><li>When a previously suspended transaction was retrieved and re-suspended, the POS receipt number counter could go backwards, causing the next transaction to reuse a receipt number already assigned to another suspended transaction on the remote company.</li><li><p>The LastSlipNo POS tag now only updates when the receipt number is higher than the current value, preventing it from being overwritten with a lower number.</p></li><li>
<p>This affects POS terminals using company-to-company web replication (TS Susp./Retrieve) that retrieve and re-suspend transactions.</p>
</li></ul>
