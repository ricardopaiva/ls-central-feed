---
title: "LS Central hotfixes - 26.1.21, Release date August 28, 2025 - Hotfixes"
product: LS Central
version: "26.1.21"
date: 2025-08-28 00:00:00+00:00
---

<strong>70331 'tender Operation' and 'FLOAT_ENT' handling - event missing a parameter</strong>
<ul><li><li>A new parameter, <b>SafTenderDataTable</b> variable was added in existing event <b>OnBeforeInitMenuOnInitSafTenderPanel</b> in LSC Safe Denom. Panel Commands codeunit.</li></li></ul>
<strong>70115 SC-2688-Public Method Request - LSC TR: Store Credit voucher extra print slip required during returns</strong>
<ul><li><li><b>PrintExtraPayment</b> procedure made public in POS Print Utility.</li></li></ul>
<strong>70101 Refund issue in Offline POS_V2</strong>
<ul><li><li>Bugfix to not compress POS Sales Lines when returning items linked to parent lines.</li></li></ul>
<strong>70010 Suspend Transaction after marking lines as CO returns an Error</strong>
<ul><li><li>Now Customer Order transactions can be suspended. However, it is only possible <b>before</b> the Customer Order is created.</li></li></ul>
<strong>69925 Unable to change discount on discount offer products</strong>
<ul><li><li>Now it is possible to change discount on discount offer products.</li></li></ul>
<strong>69906 Insufficient Quantity on Receipt Item During Statement Posting - Recipe BOMs</strong>
<ul><li><li>Statement posting now works with excluded recipe/ingredients and Inventory Setup option <b>Prevent Negative Inventory</b>.</li></li></ul>
