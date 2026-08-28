---
title: "LS Central hotfixes - 28.0.27, Release date August 25, 2026 - Hotfixes"
product: LS Central
version: "28.0.27"
subproduct: 
minor_version: "28.0"
date: 2026-08-25 00:00:00+00:00
order: 1
guid: 884dc15fe9cb5da9199ac6d0c2d5c730917e85ef
---

<strong>86874 Membership upgrade/downgrade batch job upgrades members with zero points</strong>
<ul><li>Membership upgrades and downgrades now count only the award points a member earns within the tier calculation period. Points earned outside that period — including points that have expired — no longer push a member into a higher tier.</li><li>Date range filters on member statistics work correctly too, so point totals match the range you set.</li><li><b>Action required by partners</b>:<ul><li>None. Run the Upgrade/Downgrade batch job (or wait for the scheduled run) to re-evaluate members on the corrected logic.</li></ul></li></ul>
<strong>86807 PrintExtraSlip Error After Upgrade to BC/LS28</strong>
<ul><li>Extra Print now works again for negative-amount lines that are not linked to a data entry, such as ordinary return items.</li><li>After upgrading to LS Central v.28 these lines showed an error instead of printing; they now print as before.<ul><li>Voucher and gift card remaining-balance details introduced in LS Central 28 still work for the lines that have them</li></ul></li></ul>
<strong>85193 Member account downgraded with sufficient point balance</strong>
<ul><li>Members are no longer moved to a lower scheme by the upgrade/downgrade job when their points still meet the downgrade limit. The member's scheme now stays unchanged.</li></ul>
<strong>84177 Scale Item is conflicting with UOM and asking for weigh when the UOM does not require it</strong>
<ul><li>Details not available.</li></ul>
<strong>83315 Bug: POS Web Templates "brick" price ignores the UoM configured on the Retail Hierarchy node</strong>
<ul><li>Details not available.</li></ul>
