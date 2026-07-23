---
title: "Hotels BEC hotfixes - 28.0.5 Hotels BEC, Release date May 12, 2026 - Hotfixes"
product: Hotels BEC
version: "28.0.5"
subproduct: Hotels BEC
minor_version: "28.0"
date: 2026-05-12 00:00:00+00:00
order: 81
guid: f89517b6333f294b5d45b431eb8fb4cb86f32113
---

<strong>81995 BEC - minor fix on how empty rate_plan_id is handled</strong>
<ul><li>There was an issue in the Channex/Travia reservation flow where they are sent to the PMS without a rate_plan_id.</li><li>A filtering bug was corrected, that was caused by using the wrong value during processing.</li><li>The filtering logic was moved to the correct location to ensure variables are fetched before being used.</li></ul>
