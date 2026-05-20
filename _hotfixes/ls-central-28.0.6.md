---
title: "LS Central hotfixes - 28.0.6, Release date April 24, 2026 - Hotfixes"
product: LS Central
version: "28.0.6"
subproduct: 
minor_version: "28.0"
date: 2026-04-24 00:00:00+00:00
order: 10
guid: 1d9c049d2d4dbb558593add6dbca26b15df7cf66
---

<strong>81368 AL: Critical: Locking error while posting the transaction</strong>
<ul><li>There was a critical locking error on table POS Data Entry that occurred randomly when multiple POS terminals posted transactions simultaneously.<ul><li>In codeunit LSC POS Post Utility (ProcessTransaction), a ModifyAll call on the POS Data Entry table was executed unconditionally without first checking whether matching records exist for the current receipt.</li><li>Under concurrent load (90+ terminals), Business Central acquired an UPDLOCK on the range even when no records existed, competing with other terminal transactions and causing deadlocks. </li><li>The fix adds an existence guard (IsEmpty check) before the ModifyAll so the lock is never acquired when there are no records. An integration event <b>OnBeforeModifyPOSDataEntry</b> is also added to allow external subscribers to bypass the operation if needed.</li><li>Impact: Hospitality and retail environments running online POS architectures with many concurrent terminals posting card transactions.</li></ul></li></ul>
<strong>81020 OnSendToWebServiceV2 extra parameter HttpRequest to be able to call Init #653</strong>
<ul><li>Signature in event publisher <b>OnSendToWebServiceV2</b> in codeunit Web Request Handler was changed.</li></ul>
<strong>80953 Error when upgrading to version 28.0</strong>
<ul><li>There was an upgrade failure from version 27.1 to 28.0 caused by a new unique key on the LSC Wish List Line table. </li><li>The <b>ItemAndVariantUOM</b> key on table <b>LSC Wish List Line</b> was introduced in version 28.0 with <b>Unique = true</b>. </li><li>Business Central does not allow a new unique key to be added during an upgrade because existing data may contain duplicates, causing Sync-NAVApp to fail. </li><li>The Unique property was removed from the key so the upgrade completes successfully. </li><li>Customers upgrading from version 27.1 to 28.0 or later  no longer encounter a schema sync failure during the upgrade process.</li></ul>
<strong>80541 DeviceID parameter to be VAR in "LSC POS Hardware Interface".LSN_POS_Devices_OnBeforeOpenDrawer Integration Event</strong>
<ul><li>Details not available.</li></ul>
