---
title: "Autotests hotfixes - 28.2.14 Autotests, Release date October 27, 2026 - Hotfixes"
product: Autotests
version: "28.2.14"
subproduct: Autotests
minor_version: "28.2"
date: 2026-10-27 00:00:00+00:00
order: 16
guid: 3f5d8be7a327e3bedaed8e49dabbe5320a2bf1da
---

<strong>90230 Reactivate Insert Job Queue Default Entries action on Kitchen Service Configuration</strong>
<ul><li>The <b>Insert Job Queue Default Entries</b> action on the Kitchen Service Configuration page works again. It creates the Web KDS job queue category and the <b>Update routing information for Kitchen Display Stations</b> job. If the job already exists, the action resets it to the default settings.</li><li><b>Action required by partners:</b>
<ul>
<li>After you run the action, the new job queue entry is On Hold. Set its status to Ready so the routing update starts running.</li>
</ul>
</li></ul>
