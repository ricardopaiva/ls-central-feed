---
title: "LS Central hotfixes - 28.0.13, Release date May 13, 2026 - Hotfixes"
product: LS Central
version: "28.0.13"
subproduct: 
minor_version: "28.0"
date: 2026-05-13 00:00:00+00:00
order: 12
guid: 79f0339352c0a17e1c2482210df943a163ea4f9d
---

<strong>82275 POS fails on BC licenses without LS Activity object range (Total / Advanced Search)</strong>
<ul><li>There was an issue where POS failed with a <b>current permissions prevented the action</b> error on tenants whose BC license did not include the LS Activity object range. </li><li>Two Activity POS event subscribers, the unapplied-allowance prompt on <b>OnBeforeTotalPressed</b> and the Advanced Search modal panel handler in codeunit 10015920  are now skipped when the LS Activity license is missing, allowing POS to operate normally for non-Activity customers.</li></ul>
<strong>81838 Event require for Offer should run for any specific Customer Disc. Group</strong>
<ul><li>A new integration event was added to <b>Codeunit 99001574</b> (LSC POS Transaction Events):<ul><li><b>OnFindActiveOfferInStoreOnBeforeCustomerDiscGroupFilter. </b></li><li>This event fires for each enabled periodic discount during offer evaluation in FindActiveOfferInStore (<b>Codeunit 99001599</b>), before the standard Customer Disc. Group and Member Value filter is applied.</li></ul></li></ul>
