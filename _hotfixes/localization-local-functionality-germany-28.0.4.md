---
title: "Localization hotfixes - 28.0.4 Local Functionality Germany, Release date June 16, 2026 - Hotfixes"
product: Localization
version: "28.0.4"
subproduct: Local Functionality Germany
minor_version: "28.0"
date: 2026-06-16 00:00:00+00:00
order: 82
guid: c51374b3abed930d069cdc7894a3fb8d7275250c
---

<strong>79439 LSC de-DE - Fiskaly Transactions</strong>
<ul><li>Fiskaly sales transactions now move to <b>FINISHED</b> status correctly when payment goes to a customer account.</li><li>Previously, any transaction settled by customer account (such as bank transfer or charge-to-account) stayed <b>ACTIVE</b> indefinitely—because the completion check excluded customer account tenders from its calculation.</li><li>After upgrading, existing transactions stuck in ACTIVE are automatically flagged as Requires Update, ready for bulk resubmission.</li></ul>
<strong>79745 Local Functionality Cashpoint Closing Error</strong>
<ul><li>Submitting a cash point closing no longer fails with a duplicate record error when income or expense accounts have a <b>Business Case Type</b> configured. The Business Case field is part of the composite key in the internal VAT buffer—it was previously cleared on refresh, causing a duplicate key error on the second insert attempt.</li></ul>
<strong>82749 LSC DE - Issues with Fiskaly Cashpoint Closures: Correction Status Sync, Missing Business Dates, and Transaction Mapping Errors</strong>
<ul><li>Three cash point closing errors are now resolved:<ol><li value="1"><b>Correction closure does not update the original</b><ul><li>After an E_CASH_REGISTER_NOT_FOUND error, the system creates a Correction Closure that completes successfully, but the original closure stayed in Error. </li><li>The original’s status is now updated correctly once the correction succeeds.</li></ul></li><li value="2"><b>Could not determine business date</b><ul><li>The business date lookup for retried closures now works correctly in all error-recovery scenarios.</li></ul></li><li value="3"><b>No fiskaly transactions found for this statement</b><ul><li>The statement number mapping is now correct so transactions are always found.</li></ul></li></ol></li></ul>
