---
title: "LS Central hotfixes - 28.0.4, Release date April 21, 2026 - Hotfixes"
product: LS Central
version: "28.0.4"
subproduct: 
minor_version: "28.0"
date: 2026-04-21 00:00:00+00:00
order: 12
guid: 55c58e5eedef48dea9dd9b665fb5804a3c9d6421
---

<strong>81025 AL: Wrong processing of CO Payments during CO Edit</strong>
<ul><li>There was an issue with <b>Customer Order Edit</b> with payment line to generate payment Transaction as done in Order Create. This was fixed. </li><li>There was an issue with <b>Shopify order edit</b> to expire pre-auth payment line when final payment is added to existing order.  This was fixed. </li></ul>
<strong>80953 Error when upgrading to version 28.0</strong>
<ul><li>There was an upgrade failure from version 27.1 to 28.0 caused by a new unique key on the LSC Wish List Line table. </li><li>The <b>ItemAndVariantUOM</b> key on table <b>LSC Wish List Line</b> was introduced in version 28.0 with <b>Unique = true</b>. </li><li>Business Central does not allow a new unique key to be added during an upgrade because existing data may contain duplicates, causing Sync-NAVApp to fail. </li><li>The Unique property was removed from the key so the upgrade completes successfully. </li><li>Customers upgrading from version 27.1 to 28.0 or later  no longer encounter a schema sync failure during the upgrade process.</li></ul>
<strong>80621 Keep original Interval type when date zooming in POS framework Matrix, and fix activity/reservation filters on the lookup from resource/date to include the full date range</strong>
<ul><li>The Zoom to date feature in the POS matrix (which opens up the selected date in a new matrix view) was changed, to keep existing interval type assignment for the zoom view.</li><li>  There was also an issue with clicking on either Resource Cell or Interval Time cell when the template setting was to show the related list of reservations or list of activities.  <ul><li>Now those lists should show correctly the related activity or reservation entries depending on the cell clicked settings in the matrix template.</li></ul></li></ul>
