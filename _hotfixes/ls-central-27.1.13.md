---
title: "LS Central hotfixes - 27.1.13, Release date March 10, 2026 - Hotfixes"
product: LS Central
version: "27.1.13"
subproduct: 
minor_version: "27.1"
date: 2026-03-10 00:00:00+00:00
order: 2
guid: 4dd06526f8f1e6e0914928465e2bacaa3de50fc3
---

<strong>79073 Location Code Error when posting Recipe Item</strong>
<ul><li>There was an issue with sales type Location Code. This was fixed. </li></ul>
<strong>78833 EventSubscriber needed for LSC POS Price Utility Codeunit - LS Central OnPrem Version 27.1</strong>
<ul><li>Six integration Event publishers were added to codeunit <b>LSC POS Price Utility</b> (99008906) for partner extensibility.<ul><li><b>OnBeforeIsPromotionForLoyaltyScheme</b></li><li><b>OnBeforeIsPromotionForMember</b></li><li><b>OnBeforeIsPromotionForCoupon</b></li><li><b>OnBeforeIsPromotionForCustDiscGroup</b> events with IsHandled/ReturnValue pattern, allowing subscribers to override the return value of each promotion check.</li></ul></li><li><b>OnBeforeIsPromotionForLoyaltyScheme</b></li><li><b>OnBeforeIsPromotionForMember</b></li><li><b>OnBeforeIsPromotionForCoupon</b></li><li><b>OnBeforeIsPromotionForCustDiscGroup</b> events with IsHandled/ReturnValue pattern, allowing subscribers to override the return value of each promotion check.</li><li><b>OnBeforeFindSetDiscOffer</b> and <b>OnBeforeFindSetPeriodicDiscount</b> events were added allowing subscribers to modify filters on the Offer and Periodic Discount records before they are queried in FindOfferPreMemberAttr and FindPeriodicDiscPreMemberAttr.</li><li>Partners extending promotion/discount logic in POS can now subscribe to these events to customize behavior without modifying the base codeunit.</li></ul>
<strong>73290 Return of a transaction from different store</strong>
<ul><li>Previously a transaction from a different store could not be returned when distribution location was configured. This was fixed.</li></ul>
