---
title: "Web Kitchen Service hotfixes - 28.0.4 Web KDS, Release date May 12, 2026 - Hotfixes"
product: Web Kitchen Service
version: "28.0.4"
subproduct: Web KDS
minor_version: "28.0"
date: 2026-05-12 00:00:00+00:00
order: 62
guid: 685ff0bdb5c9eba870a3f2430f1046db4d2eac2c
---

<strong>79538 Removing fallback to files when no connection is configured</strong>
<ul><li>The fallback files were removed when connection to LS Central is not configured.</li></ul>
<strong>80487 When CFD Has more than one page and you bump an order form there it gets glitch with pages with only 2 orders</strong>
<ul><li>There was an error on CFD, when the station has more than one page. This was fixed. </li><li>Bumping from station was also broken but was fixed.</li></ul>
<strong>80739 Print as Expeditor in the middle of the line</strong>
<ul><li>It should only print once on this scenario, as the Printer is an Expeditor that sends to another expeditor.</li></ul>
<strong>80983 House Keeping on git flows all branch</strong>
<ul><li>Details not available.</li></ul>
<strong>80999 Orders count does not count old orders</strong>
<ul><li>The orders count, now counts all, not finished orders.</li></ul>
<strong>81024 Adding logs on Request fails</strong>
<ul><li>More precise log to get errors was added. </li></ul>
<strong>81062 When the Line has scrolls, and we bump the last item, it goes back to the first line, but it does not show the Header anymore</strong>
<ul><li>The header of lines, now shows.</li></ul>
<strong>81155 House Keeping build</strong>
<ul><li>Details not available.</li></ul>
<strong>81315 Not considering CFD times to time last today and time last</strong>
<ul><li>Not Counting the time on CFD for statistics.</li></ul>
<strong>81317 Force reconnection on SignalR</strong>
<ul><li>Using reconnection from the SignalR.</li></ul>
<strong>81363 Remove need of CTRL+F5 when updating WebKDS</strong>
<ul><li>The need to do a CTRL+F5 on WebKDS after update was removed. </li></ul>
<strong>81423 Adding KeepAlive on SignalR</strong>
<ul><li>Details not available.</li></ul>
<strong>82004 When a Order with a Item and a Deal is sold KDS it is printing the Deal even though it not routed</strong>
<ul><li>It should only print the items that are routed even when the sale has a Deal.</li></ul>
