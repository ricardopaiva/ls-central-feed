---
title: "Localization hotfixes - 26.1.2 Local Functionality Germany, Release date July 22, 2025 - Hotfixes"
product: Localization
version: "26.1.2 Local Functionality Germany"
date: 2025-07-22 00:00:00+00:00
---

<strong>68239 LSC DE - Fiskaly Error: E_TX_NOT_FOUND Transaction not found in SIGN DE (In Local Functionality DE)</strong>
<ul><li><li>Fixed an issue where if a partner disabled their TSS and  managed to create a new one and a new master cash register, the cash point closings would not work because we would still try to use the old cash point closings.</li></li>
<li><li>Fixed related issues such as client registering behavior and some procedures related to creating cash point closings such as fetching fiskaly transactions to create the API request.</li></li></ul>
