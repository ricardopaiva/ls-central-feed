---
title: "Autotests hotfixes - 28.2.8 Release date September 10, 2026 - Hotfixes"
product: Autotests
version: "28.2.8"
subproduct: 
minor_version: "28.2"
date: 2026-09-10 00:00:00+00:00
order: 14
guid: ba3e289adf83f060ea45ee0ad46fe46d01428dcf
---

<strong>87703  Issue when using a Coupon as a tender in a transaction</strong>
<ul><li>Coupons used as a payment tender, or scanned by their plain coupon code, now consistently redeem for the coupon's actual per-instance value instead of falling back to the coupon's default header value. This fixes payment lines and discount lines showing the wrong amount for coupons whose value is set per issued instance rather than as a single fixed amount on the coupon.</li></ul>
