---
title: "SCO hotfixes - 28.2.1 Self-Checkout Connector, Release date August 25, 2026 - Hotfixes"
product: SCO
version: "28.2.1"
subproduct: Self-Checkout Connector
minor_version: "28.2"
date: 2026-08-25 00:00:00+00:00
order: 11
guid: 27efc9b41f8491a4caca3c9810763af0b5cc471a
---

<strong>86733 SCO Databar processing functionality not demanding keys 10, 17 and 21</strong>
<ul><li>Scanning a GS1 barcode at the Self-Checkout POS could raise a runtime error when the parsed GS1 data did not contain the expected key or value.</li><li>The value is now read safely and returns blank when the data is missing, so the scan completes without an error.</li></ul>
