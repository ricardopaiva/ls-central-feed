---
title: "LS Central hotfixes - 28.2.16, Release date October 21, 2026 - Hotfixes"
product: LS Central
version: "28.2.16"
subproduct: 
minor_version: "28.2"
date: 2026-10-21 00:00:00+00:00
order: 1
guid: 2f9929e788fec5d80b33c4350d48d45082bfbb3b
---

<strong>87527 Time Zone setting in user settings affect date displayed when booking activity product.</strong>
<ul><li>There was  an issue with the Date calendar picker in the Booking POS interface.  The picker results went through a time zone conversion based on the users time zone settings, which could cause the wrong date selection to be returned. <ul><li>This was fixed so that the date results do not go through any conversion.</li></ul></li></ul>
<strong>89215 Expose Internal Procedures and Integration Events for Add Items to Replen. Journal #714</strong>
<ul><li>The following public procedures and integration events have been created:<ul><li>Codeunit <b>LSC Item Creation</b><ul><li>New public codeunit "LSC Item Creation Public" exposes CreateExtraTables.</li></ul></li><li>Page <b>LSC Retail Item-Var-Loc.Avail</b><ul><li>New public procedure ItemInitPublic exposes ItemInit.</li></ul></li><li>Codeunit <b>LSC Replen. Create Transf. Ord</b><ul><li>New public codeunit <b>LSC Replen. Create Ord. Public</b> exposes CreateTOFromPlannedStockDemand.</li></ul></li><li>Report <b>LSC Add Items to Replen. Jrnl</b><ul><li>New integration events added:<ul><li>OnRecalculateOnAfterSetItemFilter</li><li>OnAfterSetReplenItemQuantityFilter</li><li>OnAfterCheckSkipReportProcess</li><li>OnAfterPostReport.</li></ul></li></ul></li></ul></li></ul>
<strong>90230 Reactivate Insert Job Queue Default Entries action on Kitchen Service Configuration</strong>
<ul><li>The <b>Insert Job Queue Default Entries</b> action on the Kitchen Service Configuration page works again. It creates the Web KDS job queue category and the <b>Update routing information for Kitchen Display Stations</b> job. If the job already exists, the action resets it to the default settings.</li><li><b>Action required by partners:</b>
<ul>
<li>After you run the action, the new job queue entry is On Hold. Set its status to Ready so the routing update starts running.</li>
</ul>
</li></ul>
