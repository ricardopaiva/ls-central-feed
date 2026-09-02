---
title: "LS Central hotfixes - 28.0.28, Release date September 1, 2026 - Hotfixes"
product: LS Central
version: "28.0.28"
subproduct: 
minor_version: "28.0"
date: 2026-09-01 00:00:00+00:00
order: 1
guid: f94fbae3f065c3891c1840ae9e510bc7f9ffd1b0
---

<strong>86807 PrintExtraSlip Error After Upgrade to BC/LS28</strong>
<ul><li>Extra Print now works again for negative-amount lines that are not linked to a data entry, such as ordinary return items.</li><li>After upgrading to LS Central v. 28 these lines showed an error instead of printing; they now print as before.</li><li>Voucher and gift card remaining-balance details introduced in LS Central 28 still work for the lines that have them.</li></ul>
<strong>86165 SC-4636-Events needed in LS Central v25</strong>
<ul><li>The OnBeforePrintLineFormatString event has new SectionID and NodeName parameters.</li><li>New overload procedure PrintLine with SectionID and NodeName parameters.</li><li>PrintTenderDeclSlip, PrintTenderDeclLines and PrintRemoveAddTenderLines now trigger new PrintLine overload.</li><li>The OnBeforePrintInfoCodeLine event has new ICode and ISubCode parameters.</li></ul>
<strong>85285 Mobile POS replicates wrong staff permissions after full device resync (manager privileges denied)</strong>
<ul><li>Staff with manager privileges can once again void transactions, process returns, and complete sales on Mobile POS. Previously, on a device that cleared its database and did a full resync, everyone in a store could be replicated with the wrong permissions — copied from a single staff record — so managers were wrongly told they don't have manager privileges. Now each staff member's own permissions replicate to the device correctly.</li><li><b>Action required by partners</b>
<ul>
<li>Update to a build that includes this fix, then let devices replicate. Corrected permissions apply on the next sync — no manual cleanup needed.</li>
<li>If a device was worked around by manually deleting rows from its local permission table, no further action is needed.</li>
<li>Affected versions: 28.0 and 28.1 (also in latest).</li>
</ul>
</li></ul>
<strong>84501 Bugfix: do not use ItemUOMBuffer.Code when generating item labels</strong>
<ul><li>Generating item labels through the scheduler no longer fails for items that lack the unit of measure last used during shelf label generation.</li></ul>
