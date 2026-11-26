---
title: "Pharmacies hotfixes - 29.0.3 Pharmacies Autotest, Release date November 24, 2026 - Hotfixes"
product: Pharmacies
version: "29.0.3"
subproduct: Pharmacies Autotest
minor_version: "29.0"
date: 2026-11-24 00:00:00+00:00
order: 37
guid: 734b0db47d341892bf3c7b1cd9d142dc1f1e543b
---

<strong>92534 Request: W1 - Supported way to run dispense production for a single card from AL (LS Central for pharmacies)</strong>
<ul><li>Run dispense production for a single dispense order without a user present. A new public procedure, <b>ProcessSingleOrderWithoutUI</b> in codeunit 10015650 LSC PH Disp.</li><li>  ◦ Worksh. Functions, takes a dispense order and a period. It shows no dialogs, messages, confirmations, or pages, so a job queue entry or web service can call it.</li><li>Before calling <b>ProcessSingleOrderWithoutUI</b> in codeunit LSC PH Disp. Worksh. Functions, log in a pharmacy user in codeunit LSC PH Session.</li><li>  ◦ A background session has no pharmacy user, store or terminal, and without them production can fail, for example with <b>Store Pharmacy Details for Store is missing.</b></li><li>  ◦ For example, to use the user and terminal set in Pharmacy Setup (Scheduler Pharmacy User and Scheduler Terminal No.), the procedure LoginSchedulerUserFromSetup() can be called.</li><li>The procedure returns whether production succeeded, the production batch number, the first production order number, and a result text.</li><li>  ◦ It returns false with a reason when the order is not confirmed, when the period is not valid, or when the order is already produced through the end date.</li><li>  ◦ Dispense dates are updated according to Production Date Update in Dispense Setup, as in batch production. Production from the user interface works as before.</li></ul>
