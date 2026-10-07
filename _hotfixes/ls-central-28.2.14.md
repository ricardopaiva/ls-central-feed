---
title: "LS Central hotfixes - 28.2.14, Release date October 6, 2026 - Hotfixes"
product: LS Central
version: "28.2.14"
subproduct: 
minor_version: "28.2"
date: 2026-10-06 00:00:00+00:00
order: 1
guid: 49d5d32d9c786c260801745f81c4dd64dd159be6
---

<strong>89321 Sales History - start date Calculation</strong>
<ul><li>New event OnBeforeGetFirstSalesDate on page LSC Sales History allows a start date to be set.</li></ul>
<strong>89147 on before show printer error event added</strong>
<ul><li>Added the new event OnBeforeShowPrinterError_OnIsPrinterActive to codeunit <b>LSC POS Transaction Events</b>. It is raised before the <b>No Printer is configured in Hardware profile</b> error is shown in the POS (<b>LSC POS Transaction Print</b> codeunit).</li></ul>
<strong>89130 Make_SetBlockPromotionPrice_External</strong>
<ul><li>Procedure SetBlockPromotionPrice in LSC Retail Price Utils codeunit is now public.</li></ul>
<strong>87583 Add an event to intercept item and shelf label printing</strong>
<ul><li>You can now hook into item and shelf label printing with a new event, <b>OnBeforeRunCodeunitItemLabel</b>. Subscribe to it to run your own logic instead of the standard label codeunit — for a specific label code, or for all of them — without changing standard objects. If nothing subscribes, labels print exactly as before.</li><li>Partners previously had to change the codeunit assigned to a label code to fully replace its logic. This event lets a subscriber intercept printing per label code, side by side with the standard fallback, so custom label logic can be layered in without redesigning the label function itself.<ul><li><b>Affected components:</b> Item Label Print page (Print action), Item Label Quick Printing page, Shelf Label Quick Printing page, Store Inventory Management codeunit</li><li><b>Integration touch points:</b> New publisher event OnBeforeRunCodeunitItemLabel (parameters: label function, item label, IsHandled), raised before CODEUNIT.RUN on the label code's assigned codeunit</li><li><b>Configuration / setup changes:</b> None</li><li><b>Breaking changes / upgrade impact:</b> None — when no subscriber sets IsHandled, printing runs exactly as before. Also fixes a related issue where, in the two Quick Printing pages, one label code's IsHandled result could leak into the next label code printed in the same batch — each label code now evaluates independently</li></ul></li><li><b>Action required by partners:</b>
<ul>
<li>None to keep current behavior. To intercept printing, subscribe to OnBeforeRunCodeunitItemLabel and set IsHandled := true.</li>
</ul>
</li></ul>
<strong>87519 Returning a transaction can have incorrect VAT on items if the VAT group has changed since original order</strong>
<ul><li>You now get the correct VAT rate when refunding an item whose VAT group has changed since the original sale. Previously, a refund posted through a customer-account ("to account") sale could apply the item's current VAT rate instead of the rate that was actually charged at the time of the original sale.</li></ul>
<strong>84080 LineDisplay functions can have empty DeviceID</strong>
<ul><li>Details not available.</li></ul>
<strong>83640 Scale with "Live Weight" Disabled should not be load into POS Add-in</strong>
<ul><li>Details not available.</li></ul>
