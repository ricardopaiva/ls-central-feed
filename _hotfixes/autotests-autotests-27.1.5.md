---
title: "Autotests hotfixes - 27.1.5  Autotests, Release date March 5, 2026 - Hotfixes"
product: Autotests
version: "27.1.5"
subproduct: Autotests
minor_version: "27.1"
date: 2026-03-05 00:00:00+00:00
order: 19
guid: dd0a519a86c77eb8ef385c63e5716c5cc4637707
---

<strong>78142 When invoicing a Sales Order connected to a Customer Order, and no Item lines are present, posting does not succeed: Interface not initialized</strong>
<ul><li>Do no try to process Member Point Offer Lines if there are no items at posting (only Income / Expense).</li></ul>
