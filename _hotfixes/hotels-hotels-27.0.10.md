---
title: "Hotels hotfixes - 27.0.10 Hotels, Release date December 23, 2025 - Hotfixes"
product: Hotels
version: "27.0.10"
subproduct: Hotels
minor_version: "27.0"
date: 2025-12-23 00:00:00+00:00
order: 43
guid: 2bb2c996cd386cea03cda2624e47a5c2404ea48a
---

<strong>76158 Empty journal batch for Reconciliation fix for over consumed deposit</strong>
<ul><li>There was an issue with the deposit over consumption fixing process from Reconciliation page. It was showing empty batch list. Now, it  uses the property default batch for payments (Journal Batch set in HotelSetup + 'PAY') to create journal. Restriction was added to deposit consumption for posted lines, deposit cannot be consumed if it has a <b>Receipt No.</b></li></ul>
