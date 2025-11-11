---
title: "LS Central hotfixes - 27.0.5, Release date October 28, 2025 - Hotfixes"
product: LS Central
version: "27.0.5"
subproduct: 
minor_version: "27.0"
date: 2025-10-28 00:00:00+00:00
order: 3
guid: e9d3e2439b5ea7590282035e509ce31028e67f26
---

<strong>73637 ADD 3 EVENTS</strong>
<ul><li>New events were added to <b>LSC Item Variants Functions</b> codeunit.</li></ul>
<strong>73491 Voiding POS lines with package activity does not delete the activity (using SellProduct)</strong>
<ul><li>An issue was fixed, related to using the SELLPRODUCT POS command to sell activity package products.  This process was previously not confirming the <b>base</b> product in a manner that would make it void correctly if the POS journal was then later voided using the void transaction POS command or void line.</li><li>
<p>The voided activity on the POS was not removed from the reservation tables. This was fixed. </p>
</li></ul>
<strong>73286 New event publishers to handle POS Devices (Drawer + EFT)</strong>
<ul><li>Details not available.</li></ul>
<strong>73257 Discounts added to an activity allowance package are not applied to the allowance items when consumed in the POS</strong>
<ul><li>The Package/Item allowances was changed, to use unit price, including discount when enforcing allowances on POS and to keep track of consumption.</li></ul>
