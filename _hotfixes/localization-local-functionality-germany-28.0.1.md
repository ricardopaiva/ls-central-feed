---
title: "Localization hotfixes - 28.0.1 Local Functionality Germany, Release date April 14, 2026 - Hotfixes"
product: Localization
version: "28.0.1"
subproduct: Local Functionality Germany
minor_version: "28.0"
date: 2026-04-14 00:00:00+00:00
order: 31
guid: 0bad2be6930de69a72c2c10d88e6143c2af66098
---

<strong>80547 Fiskaly Transaction - Invalid User Credentials</strong>
<ul><li>There was an issue where the Fiskaly client ID could be lost after a TSS refresh.</li><li>The system now automatically recovers the client ID from the Cash Register record during TSS refresh, preventing clients from being re-created unnecessarily.</li></ul>
