---
title: "Pharmacies hotfixes - 27.1.1 Norway, Release date March 3, 2026 - Hotfixes"
product: Pharmacies
version: "27.1.1"
subproduct: Norway
minor_version: "27.1"
date: 2026-03-03 00:00:00+00:00
order: 35
guid: 6539d9e70bfe3a05790aee46e8f1fa6cb5020571
---

<strong>65721 Problems with credit orders in posting queue - ISNULL missing</strong>
<ul><li>The missing IF NOT ISNULL(...) check was added.</li><li>This part of the code was refactored to improve readability.</li></ul>
<strong>74807 Need to port SplitStringFont function from CAL</strong>
<ul><li><b>Label Utilities DLLs</b> were added, and the <b>SplitStringFont</b> function as well.</li><li>The dose label codeunit was updated to utilize the newly added function.</li></ul>
<strong>77465 Not possible to credit PSD – Error message: "You can not cancel a PSD that was created from another pharmacy"</strong>
<ul><li>Functionality was fixed:<ul><li>System create credit order for posted prescription order where linked psd line exist.</li></ul></li><li>System create credit order for posted prescription order where linked psd line exist.</li></ul>
<strong>77643 Dose Labels were not being printed in AL</strong>
<ul><li><b>Dose Label</b> were not being printed in AL. This was fixed. </li></ul>
<strong>78340 Move Label fix to Hotfix/Latest</strong>
<ul><li>Details not available.</li></ul>
