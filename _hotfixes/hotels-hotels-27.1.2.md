---
title: "Hotels hotfixes - 27.1.2 Hotels, Release date February 10, 2026 - Hotfixes"
product: Hotels
version: "27.1.2"
subproduct: Hotels
minor_version: "27.1"
date: 2026-02-10 00:00:00+00:00
order: 17
guid: 51078d5b153b043550fd4a926f6e1b9592f769fd
---

<strong>77402 When Night Audit is run, then Paying Reservation No. is changed, the deactivated line is still included in the total amount due</strong>
<ul><li>There was an issue with <b>VAT incl. in rate</b>, when it was  set to off, and changing routing rule AFTER running night audit the paying reservation field was changed to original value. Now changing routing on a DRE line that was posted to finance keeps correct paying reservation.</li></ul>
<strong>77397 Changing from Checkedout status to SoftCheckout status is not allowed</strong>
<ul><li>It is now possible to change between different Checked Out statuses.</li><li>There was an issue, where it was possible to change a Hotel Reservation from Checked Out to Confirmed. This was fixed. </li></ul>
