---
title: "Autotests hotfixes - 28.0.17 Autotests, Release date August 25, 2026 - Hotfixes"
product: Autotests
version: "28.0.17"
subproduct: Autotests
minor_version: "28.0"
date: 2026-08-25 00:00:00+00:00
order: 28
guid: 69672809c1fbae2428037a5c7904e874e6a19bf2
---

<strong>86874 Bonia Malaysia - Membership upgrade/downgrade batch job upgrades members with zero points</strong>
<ul><li>Membership upgrades and downgrades now count only the award points a member earns within the tier calculation period. Points earned outside that period — including points that have expired — no longer push a member into a higher tier.</li><li>Date range filters on member statistics work correctly too, so point totals match the range you set.</li><li><b>Action required by partners</b>:<ul><li>None. Run the Upgrade/Downgrade batch job (or wait for the scheduled run) to re-evaluate members on the corrected logic.</li></ul></li></ul>
<strong>85193 Member account downgraded with sufficient point balance</strong>
<ul><li>Members are no longer moved to a lower scheme by the upgrade/downgrade job when their points still meet the downgrade limit. The member's scheme now stays unchanged.</li></ul>
