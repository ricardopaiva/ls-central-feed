---
title: "LS Central hotfixes - 28.0.5, Release date April 23, 2026 - Hotfixes"
product: LS Central
version: "28.0.5"
subproduct: 
minor_version: "28.0"
date: 2026-04-23 00:00:00+00:00
order: 11
guid: ebbd1ebf7e2a2e952e4f429bea16402a14ea0b61
---

<strong>81025 AL: Wrong processing of CO Payments during CO Edit</strong>
<ul><li>There was an issue with <b>Customer Order Edit</b> with payment line to generate payment Transaction as done in Order Create. This was fixed. </li><li>There was an issue with <b>Shopify order edit</b> to expire pre-auth payment line when final payment is added to existing order.  This was fixed. </li></ul>
<strong>80953 Error when upgrading to version 28.0</strong>
<ul><li>There was an upgrade failure from version 27.1 to 28.0 caused by a new unique key on the LSC Wish List Line table. </li><li>The <b>ItemAndVariantUOM</b> key on table <b>LSC Wish List Line</b> was introduced in version 28.0 with <b>Unique = true</b>. </li><li>Business Central does not allow a new unique key to be added during an upgrade because existing data may contain duplicates, causing Sync-NAVApp to fail. </li><li>The Unique property was removed from the key so the upgrade completes successfully. </li><li>Customers upgrading from version 27.1 to 28.0 or later  no longer encounter a schema sync failure during the upgrade process.</li></ul>
<strong>80801 Need an onbeforeevent in codeunit 99001599 "LSC POS Transaction Impl</strong>
<ul><li>Event <b>OnBeforeOnCustomerOrderDeposit</b> was added in POS Transaction.</li></ul>
<strong>80618 Compressed should be active in all clients when version 28 is running on HO</strong>
<ul><li>Details not available.</li></ul>
<strong>80082 LSC NA - Issue with the incorrect tax amounts</strong>
<ul><li>Details not available.</li></ul>
<strong>79812 Fixed "LSC Delete Logs" job when deleting actions/preactions for subjobs with remote sources #638</strong>
<ul><li>The Delete Logs job now considers the <b>Last Source Counter</b> of the current Distribution Location.<ul><li>It uses this value to filter and delete records.</li></ul></li></ul>
