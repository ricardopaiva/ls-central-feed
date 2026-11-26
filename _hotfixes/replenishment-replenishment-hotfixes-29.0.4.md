---
title: "Replenishment hotfixes - 29.0.4 Replenishment hotfixes, Release date November 24, 2026 - Hotfixes"
product: Replenishment
version: "29.0.4"
subproduct: Replenishment hotfixes
minor_version: "29.0"
date: 2026-11-24 00:00:00+00:00
order: 47
guid: e75b9bcaebecfa7665aa8af5b64807f53a98793a
---

<strong>91569 Transfer-from Code on Transfer Orders Created from the Replenishment Journal</strong>
<ul><li>When transfer orders are created from the Transfer Replenishment Journal, the Transfer-from Code now always uses the location from the replenishment template. Previously, <b>Create Transfer Orders</b> could fail with the error <b>Transfer-from Code and Transfer-to Code cannot be the same</b>.</li></ul>
<strong>92350 Integration Event to Check Skip0Lines</strong>
<ul><li>The integration event OnInsertJournalFromTempOnBeforeCheckSkip0LinesForTransfer was added to report "LSC REPL Add Items to Journal".</li></ul>
