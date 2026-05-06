---
title: "Autotests hotfixes - 28.0.7  Autotests, Release date May 5, 2026 - Hotfixes"
product: Autotests
version: "28.0.7"
subproduct: Autotests
minor_version: "28.0"
date: 2026-05-05 00:00:00+00:00
order: 10
guid: 4c01b0acd8ef1f597c08305bc4d5c8cca85eaaa2
---

<strong>81019 Fix CO Payment LineNo duplication on cancel order</strong>
<ul><li>There was an issue where canceling a Customer Order that included a service item together with two payment lines (loyalty points and card payment) caused an error:<ul><li>The record in table Customer Order Payment already exists. </li><li>The error was due to a <b>Line Number collision</b> on the Customer Order Payment table during the cancel flow, where multiple code paths attempted to insert a new payment entry with the same computed Line Number.</li></ul></li><li>The record in table Customer Order Payment already exists. </li><li>The error was due to a <b>Line Number collision</b> on the Customer Order Payment table during the cancel flow, where multiple code paths attempted to insert a new payment entry with the same computed Line Number.</li></ul>
