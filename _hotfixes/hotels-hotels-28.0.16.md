---
title: "Hotels hotfixes - 28.0.16 Hotels, Release date June 16, 2026 - Hotfixes"
product: Hotels
version: "28.0.16"
subproduct: Hotels
minor_version: "28.0"
date: 2026-06-16 00:00:00+00:00
order: 59
guid: 02be576a2aa63c8200e80d875d91ba60b0689ea4
---

<strong>83498 Error during POS Return Transaction with the original sales transaction has discount</strong>
<ul><li>Return a Hotel POS transaction that has discounted lines and pay it with Room Charge. Previously, completing the return failed with the error "Line Discount % cannot be less than 0". Folio and line amounts are unchanged.</li><li><b>Action required by partners:</b> <ul><li>None — the fix applies automatically after upgrade.</li></ul><ul><li><b>Known limitation:</b><ul><li>On returns, the stored line discount percentage may differ slightly from the original (for example 5.03% vs 5.00%). This comes from LS Central and affects the displayed percentage only when we work with multiples lines and discounts— all amounts are exact.</li></ul></li></ul></li></ul>
<strong>83001 Populate Customer No. on hotel reservation deposit transaction (BO + POS)</strong>
<ul><li>Collect or refund a reservation deposit for a company payer, in the Back Office or at the POS, and the transaction now posts against that customer. The deposit lands in the customer's ledger instead of as an anonymous sale, so staff can see the company has already paid. At the POS, when a reservation has more than one folio, you pick the folio the deposit belongs to.</li><li><b>Action required by partners</b>:<ul><li>None. The fix applies automatically after upgrading.</li></ul></li></ul>
