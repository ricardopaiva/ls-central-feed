---
title: "Hotels BEC hotfixes - 28.0.8 Hotels, Release date June 5, 2026 - Hotfixes"
product: Hotels BEC
version: "28.0.8"
subproduct: Hotels
minor_version: "28.0"
date: 2026-06-05 00:00:00+00:00
order: 57
guid: fe6de4009c7ef3882eb5b17083f26045064af45e
---

<strong>83267 Channex rate sync only publishes occupancy prices for 2 guests — extend to 5 to match LS Hotels</strong>
<ul><li>Channex now receives occupancy-based prices for stays of up to five guests, matching what LS Hotels already supports. Previously, only two occupancy prices reached Channex, so any rate you would have set for three or more guests was dropped and those stays showed no price on the channel. The integration now sends one price per occupancy level, up to the number of guests the rate code allows.</li><li><b>Action required by partners:</b>
<ul>
<li>None, existing occupancy prices sync automatically after upgrade. If you price by occupancy, check that each rate code’s guest count (Pax), is set correctly so the intended number of prices is published.</li>
<li>The job should pick up the delta to send over to Channex.</li>
</ul>
</li></ul>
