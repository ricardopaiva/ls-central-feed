---
title: "LS Central hotfixes - 27.0.18, Release date December 4, 2025 - Hotfixes"
product: LS Central
version: "27.0.18"
subproduct: 
minor_version: "27.0"
date: 2025-12-04 00:00:00+00:00
order: 12
guid: 3082cf6ff93679fa7341b256a55736ae9c03ae9e
---

<strong>75308 Fix refunding on POS when collecting and some items have been shortaged or canceled.</strong>
<ul><li>When <b>Stortage and Cancel</b> is stored in picking, then these items are refunded on POS when the order is collected. In Backoffice, the Posted Order states that the refunding is pending, Type = <b>To be refunded</b>. The Type should be <b>Refunded on POS</b>. </li></ul>
<strong>75221 All instances cannot navigate from EOD statement to Customer Ledger Entries</strong>
<ul><li>Filter was changed to <b>setfilter</b> in BackOfficeExt codeunit.</li></ul>
<strong>74912 Searching for member name that include an apostrophe returns an error message on POS</strong>
<ul><li>Apostrophe filter was fixed on search member contact.</li></ul>
<strong>74544 Retail Receiving - Rules Conflict</strong>
<ul><li>Do not reset posting actions when return all items in a retail are receiving.</li></ul>
