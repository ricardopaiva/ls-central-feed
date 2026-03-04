---
title: "Forecourt hotfixes - 27.1.1, Release date February 10, 2026 - Hotfixes"
product: Forecourt
version: "27.1.1"
subproduct: 
minor_version: "27.1"
date: 2026-02-10 00:00:00+00:00
order: 15
guid: e4c7675f69f678e806e2280314dc22cf93fda7ce
---

<strong>77335 Event Request: ErrorText should be by reference (var) in event OnProcessSuspensionByState_SecErrorChecking of codeunit 99001574 "LSC POS Transaction Events"</strong>
<ul><li><b>OnProcessSuspensionByState_SecErrorChecking</b> was obsoleted and new event <b>OnProcessSuspensionByState_SecErrorCheckingV2</b> was created with var on the ErrorText parameter.</li></ul>
