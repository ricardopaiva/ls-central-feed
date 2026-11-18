---
title: "Autotests hotfixes - 29.0.6 Autotests, Release date November 17, 2026 - Hotfixes"
product: Autotests
version: "29.0.6"
subproduct: Autotests
minor_version: "29.0"
date: 2026-11-17 00:00:00+00:00
order: 7
guid: ec13a21ac5ebcc1217087e5de6891238ccd4fa1e
---

<strong>90215 Fix rounding precision for Deposit Amount calculation</strong>
<ul><li>Deposit amounts in the Bookings deposit schedule now keep their decimals instead of being rounded to whole numbers. Percentage deposits from a deposit policy, and deposits you recalculate by changing the deposit percentage, now round to the currency's amount rounding precision, so the schedule adds up to the reservation total and the final invoice no longer shows a difference.</li><li><b>Action required by partners:</b></li><li>  ◦ None.</li></ul>
