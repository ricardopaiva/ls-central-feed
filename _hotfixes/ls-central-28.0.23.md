---
title: "LS Central hotfixes - 28.0.23, Release date July 7, 2026 - Hotfixes"
product: LS Central
version: "28.0.23"
subproduct: 
minor_version: "28.0"
date: 2026-07-07 00:00:00+00:00
order: 3
guid: c7056a3316283ab51f64be01db5ccc760e549a4a
---

<strong>83715 Store Inventory Journal - Duplicate Purchase Orders when posting, when journal contains “Import Incomplete” lines</strong>
<ul><li>Post a Store Inventory journal that still holds lines imported from the Mobile Inventory app but not yet fully received, and you do not get duplicate purchase orders anymore.</li><li>Posting now skips those incomplete lines until the mobile import finishes, and processes them on a later post once they are received.</li></ul>
<strong>83221 EFT Card Printing "Print Buffer" does not have correct Transaction No.</strong>
<ul><li>Details not available.</li></ul>
<strong>83144 Resend Kots that were send giving a duplication error</strong>
<ul><li>When the push Kot was being used, the success was, to never send the Touched to false, making the next push send old kots too.</li></ul>
<strong>82960 SC-3929-V25 | POS data entry not found issue</strong>
<ul><li>Web requests GetDataEntryBalance and GetVoutcherEntries have been backported to versions 26.1 to 25.0.</li></ul>
<strong>80717 POS : SalesPerson Selection Modify Record and Update instead of Multiple Insert</strong>
<ul><li>When a Sales Person is selected the current sales person line is updated instead of adding a new line.</li></ul>
