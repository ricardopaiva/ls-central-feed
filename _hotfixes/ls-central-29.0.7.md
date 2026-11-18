---
title: "LS Central hotfixes - 29.0.7, Release date November 17, 2026 - Hotfixes"
product: LS Central
version: "29.0.7"
subproduct: 
minor_version: "29.0"
date: 2026-11-17 00:00:00+00:00
order: 1
guid: e3871e9552534b4789e809bb793953eb3d54de03
---

<strong>92184 When upgrading to LSC v29 an error on UpgradeEFTConfigurations is thrown</strong>
<ul><li>When upgrading to LSC v29 an error on UpgradeEFTConfigurations is thrown. This has been fixed.</li><li><b>Action required by partners:</b></li><li>  ◦ When upgrading from version 24 or older and the customer has specific configurations on EFT devices for:</li><li>    ▪ <b>Slip Print Order</b></li><li>    ▪ <b>Skip Customer Receipt</b></li><li>    ▪ <b>Skip Merchant Receipt</b></li><li>    ▪ <b>Use Numpad</b></li><li>    ▪ <b>Tips handling</b></li><li>    ▪ <b>Disable Void Card Prompt</b> or</li><li>    ▪ <b>Post Transaction after Void</b>.</li><li>    ▪ These configurations will now need to be manually moved to the configurations on the POS Terminal Card.</li></ul>
<strong>91863 Integration Event for Replenishment Calculation</strong>
<ul></ul>
<strong>90215 Fix rounding precision for Deposit Amount calculation</strong>
<ul><li>Deposit amounts in the Bookings deposit schedule now keep their decimals instead of being rounded to whole numbers. Percentage deposits from a deposit policy, and deposits you recalculate by changing the deposit percentage, now round to the currency's amount rounding precision, so the schedule adds up to the reservation total and the final invoice no longer shows a difference.</li><li><b>Action required by partners:</b></li><li>  ◦ None.</li></ul>
