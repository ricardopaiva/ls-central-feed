---
title: "LS Central hotfixes - 27.1.11, Release date March 5, 2026 - Hotfixes"
product: LS Central
version: "27.1.11"
subproduct: 
minor_version: "27.1"
date: 2026-03-05 00:00:00+00:00
order: 10
guid: 53c468fdeafb0307035c018b17b7150a4c53c747
---

<strong>78830 ASAP Remove Customer modification after GetCustomer in POS</strong>
<ul><li>When Custmer is validated on POS and balance information retrieved from HeadOffice, then only balance information is updated on Customer record on POS (extension information is not cleared).</li></ul>
<strong>78142 When invoicing a Sales Order connected to a Customer Order, and no Item lines are present, posting does not succeed: Interface not initialized</strong>
<ul><li>Do no try to process Member Point Offer Lines if there are no items at posting (only Income / Expense).</li></ul>
<strong>68830 POS Discount % Display</strong>
<ul><li>Previously POS could not display Discount % when Amount Rounding To is setup to large number. This is now fixed.</li></ul>
