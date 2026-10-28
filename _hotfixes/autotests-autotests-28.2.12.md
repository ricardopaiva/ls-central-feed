---
title: "Autotests hotfixes - 28.2.12 Autotests, Release date October 6, 2026 - Hotfixes"
product: Autotests
version: "28.2.12"
subproduct: Autotests
minor_version: "28.2"
date: 2026-10-06 00:00:00+00:00
order: 18
guid: 0bf7ee076fa13183b6231975e5993f9b33c104b4
---

<strong>87519 Returning a transaction can have incorrect VAT on items if the VAT group has changed since original order</strong>
<ul><li>You now get the correct VAT rate when refunding an item whose VAT group has changed since the original sale. Previously, a refund posted through a customer-account ("to account") sale could apply the item's current VAT rate instead of the rate that was actually charged at the time of the original sale.</li></ul>
