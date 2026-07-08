---
title: "Autotests hotfixes - 28.0.4  Autotests, Release date April 21, 2026 - Hotfixes"
product: Autotests
version: "28.0.4"
subproduct: Autotests
minor_version: "28.0"
date: 2026-04-21 00:00:00+00:00
order: 34
guid: fe8584db2218b348c0c6d2c68340ba57a63ee574
---

<strong>80953 Error when upgrading to version 28.0</strong>
<ul><li>There was an upgrade failure from version 27.1 to 28.0 caused by a new unique key on the LSC Wish List Line table. </li><li>The <b>ItemAndVariantUOM</b> key on table <b>LSC Wish List Line</b> was introduced in version 28.0 with <b>Unique = true</b>. </li><li>Business Central does not allow a new unique key to be added during an upgrade because existing data may contain duplicates, causing Sync-NAVApp to fail. </li><li>The Unique property was removed from the key so the upgrade completes successfully. </li><li>Customers upgrading from version 27.1 to 28.0 or later  no longer encounter a schema sync failure during the upgrade process.</li></ul>
