---
title: "Hotels hotfixes - 27.0.13 Hotels, Release date February 10, 2026 - Hotfixes"
product: Hotels
version: "27.0.13"
subproduct: Hotels
minor_version: "27.0"
date: 2026-02-10 00:00:00+00:00
order: 44
guid: 6d87b4e63712b56fcb0820f177ea968605782800
---

<strong>77402 When Night Audit is run, then Paying Reservation No. is changed, the deactivated line is still included in the total amount due</strong>
<ul><li>There was an issue with <b>VAT incl. in rate</b>, when it was  set to off, and changing routing rule AFTER running night audit the paying reservation field was changed to original value. Now changing routing on a DRE line that was posted to finance keeps correct paying reservation.</li></ul>
