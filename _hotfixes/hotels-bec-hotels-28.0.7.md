---
title: "Hotels BEC hotfixes - 28.0.7 Hotels, Release date June 2, 2026 - Hotfixes"
product: Hotels BEC
version: "28.0.7"
subproduct: Hotels
minor_version: "28.0"
date: 2026-06-02 00:00:00+00:00
order: 57
guid: c7b9bf9a2c8c696f4804317e33dd46a98b35e0fc
---

<strong>82957 When using RMS system, allow user to select which derived rate to publish</strong>
<ul><li>Selective derived rate publishing for Atomize (RMS) integration:<ul><li>You can now choose exactly which derived rate codes should be updated when Atomize pushes a new base rate. Open any Rate-type BEC Mapping with Publish Derived Rates enabled and use the new <b>Derived Rates to Publish</b> action to list the derived rate codes that should receive the recalculated price. <ul><li>Derived rates not on the list are left untouched, neither the Daily Room Rate price nor any outbound channel-manager push happens for them.</li></ul></li><li>Leave the list empty to keep today's behavior (all BEC-Enabled derived rates of the base are published).</li><li>Manual edits to Daily Room Rate, and updates from any source other than the Atomize webhook, are not affected.</li></ul></li></ul>
