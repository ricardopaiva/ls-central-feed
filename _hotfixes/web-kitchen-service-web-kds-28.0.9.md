---
title: "Web Kitchen Service hotfixes - 28.0.9 Web KDS, Release date June 16, 2026 - Hotfixes"
product: Web Kitchen Service
version: "28.0.9"
subproduct: Web KDS
minor_version: "28.0"
date: 2026-06-16 00:00:00+00:00
order: 138
guid: e7b56baad52e55accac73ce1ed11e9dfb9b5806b
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
<strong>81382 Making a better SetWebKDSRouting</strong>
<ul><li>Making the <b>SetWebKDSRouting</b> give us errors by order and not failling the whole order when one order on the batch fails.</li></ul>
<strong>81423 Adding KeepAlive on SignalR</strong>
<ul><li>Details not available.</li></ul>
<strong>82004 When a Order with a Item and a Deal is sold KDS it is printing the Deal even though it not routed</strong>
<ul><li>It should only print the items that are routed even when the sale has a Deal.</li></ul>
<strong>82047 WEB KDS password encryption issues</strong>
<ul><li>There was an issue with Web KDS <b>Test and Save Connection</b> failing with a wrong-credentials error when the saved connection had password encryption enabled. This was fixed. </li></ul>
<strong>82083 Expeditor only show item deals when Show Deal is on</strong>
<ul><li>The Show Deal Header was fixed. </li></ul>
<strong>82100 Items that are part of a deal, are not being color updated when they are bumped or started on the Chit/Expeditor</strong>
<ul><li>The Chit Lines are color updated.</li></ul>
<strong>82448 Web KDS - Captions missing on CHIT</strong>
<ul><li>
<p>Web KDS chit header and footer fields now display the configured caption (or field name) as a prefix in front of the value, restoring the pre-27.1.14 behavior.</p>
<ul>
<li>Caption rendering was lost when the chit margin component was rewritten in an internal refactor. Header and footer chit fields (for example "Bestilt:", "Afhentes:") rendered only the raw value with no label, making it difficult for kitchen staff to know what each value represented.</li>
<li>ChitMargins.vue now prepends the field caption when set, falls back to the field name when caption is empty, and renders the value alone when both are empty.</li>
<li>Caption text is HTML-escaped to prevent injection.</li>
<li>All Web KDS users using the Chit layout with captioned header or footer fields. <ul><li>The Card and Line layouts and the comment field within the chit are unaffected.</li></ul></li>
</ul>
</li></ul>
<strong>82586 Toggle button to turn on / off Web KDS server</strong>
<ul><li>The KDS Server toggle switch was fixed, to always appear in the ON state regardless of actual server status.<ul><li>The checkServer() function in Admin.vue was reading the entire IsServiceConfiguredResponse object instead of its isServiceRunning boolean property.</li><li>Since any JavaScript object is truthy, the toggle was permanently stuck in the ON position.</li><li>The fix correctly reads response.data.isServiceRunning.</li></ul></li><li>All Web KDS users who need to start/stop the KDS server from the Settings page.</li></ul>
<strong>82871 [CRONUS] Undo and Undo List Button Operation</strong>
<ul><li>The Undo List button was doing nothing on the Web KDS Expeditor station, this was fixed.</li><li>On Expeditor (Chit) stations the Undo List operation raised its open-modal event from the Chits component, but the event was not forwarded to the parent, so the popup never opened.</li><li>The Chits component now declares and StationBody now forwards the undo-list event, matching preparation-station behavior.</li><li>The popup now opens on the Expeditor and lists the previously-bumped orders that can be undone. Prep/line/chit-prep stations are unaffected; no server-side or data changes.</li></ul>
<strong>82995 Upcoming orders are not showing the orders</strong>
<ul><li>Fixed Upcoming Orders stations showing nothing on connect, and future (held) orders appearing prematurely on regular stations.</li><li>The station connect path now matches the periodic refresh: an Upcoming Orders station shows the held/future orders routed to it, and prep-line, prep-chit, expeditor, and customer-facing stations no longer receive future orders until they are due.</li></ul>
