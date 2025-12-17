---
title: "Hotels hotfixes - 27.0.3 Hotels, Release date November 4, 2025 - Hotfixes"
product: Hotels
version: "27.0.3"
subproduct: Hotels
minor_version: "27.0"
date: 2025-11-04 00:00:00+00:00
order: 33
guid: 7d1ad4cb3655c7f4883e8f276bca6d342dff0919
---

<strong>74062 Test issues on building hotfix candidate</strong>
<ul><li>Details not available.</li></ul>
<strong>73698 Move view filter on DRE to Actions and highlight description field if Res No and Paying Res no are not the same</strong>
<ul><li><b>The View Filter Relocation:</b>
<ul>
<li>The <b>View Filter</b> was moved to the <b>Actions</b> menu within the Revenue Entries list part. This change ensures that the filter remains accessible even when the list part is opened in <b>focus mode</b>, improving user experience and consistency across views.</li>
</ul>
</li><li>The <b>View Filter</b> was moved to the <b>Actions</b> menu within the Revenue Entries list part. This change ensures that the filter remains accessible even when the list part is opened in <b>focus mode</b>, improving user experience and consistency across views.</li><li>
<p><b>Enhanced Field Highlighting:</b>
</p>
<ul>
<li>The <b>Description</b> field in Revenue Entries is now highlighted when there is a mismatch between the <b>Reservation No.</b> and <b>Paying Reservation No.</b>. Previously, only the Reservation No. or Paying Res. No. fields were highlighted individually. This enhancement provides clearer visual cues to help users identify discrepancies more easily. </li>
<li>Additionally, when there is a mismatch between the <b>Reservation No.</b> and <b>Paying Reservation No.</b> the default View Mode is Standard, instead of the Simple which hides these columns. </li>
<li>The user can still switch to the Simple view manually.</li>
</ul>
</li><li>The <b>Description</b> field in Revenue Entries is now highlighted when there is a mismatch between the <b>Reservation No.</b> and <b>Paying Reservation No.</b>. Previously, only the Reservation No. or Paying Res. No. fields were highlighted individually. This enhancement provides clearer visual cues to help users identify discrepancies more easily. </li><li>Additionally, when there is a mismatch between the <b>Reservation No.</b> and <b>Paying Reservation No.</b> the default View Mode is Standard, instead of the Simple which hides these columns. </li><li>The user can still switch to the Simple view manually.</li></ul>
<strong>73666 Upgrade error in CreateLookupHtlMenu when default menu profile does not exist</strong>
<ul><li>An issue was fixed, with creating the new lookup menus if ##DEFAULT menu profile does not exist.</li></ul>
<strong>73633 Can not change date of confirmed reservation if the arrival date is in the past</strong>
<ul><li>For v27 onwards, the restriction was removed, that prevented moving reservations with arrival date in the past to a different date.</li><li>For v26.1, a message is shown prompting the user that he can not change Arrival Date in the past. Giving the option to open My Settings and change Work Date to be able to continue.</li></ul>
<strong>73560 Receipt printing 2 receipts</strong>
<ul><li>A bug was fixed, where printing a receipt in the POS would print all receipts from that folio, and not just the one selected.</li></ul>
<strong>73449 Error on changing rate codes on Hotel Group Reservations</strong>
<ul><li>An issue was fixed, where changing rate codes in a group reservation failed.</li></ul>
<strong>73388 Post sales invoice-remove checked out restriction</strong>
<ul><li>Posting a Sales Invoice no longer requires the Hotel reservation to be checked out.</li><li>A bug was fixed, where after selecting the action Post/Post Invoice and then saying NO when asked to confirm, an error message would be thrown.</li><li>New action <b>Preview Sales invoice</b> in Hotel Invoice Management page that creates a non-editable sales invoice that can be posted.</li><li>Action <b>Preview posting</b> no longer prompts the user if he wants to create a Sales Invoice.</li></ul>
<strong>73115 When new folio on a reservation in LS Hotels is created it is not possible to change invoice type</strong>
<ul><li>An issue was fixed, where creating a new folio would always trigger an error on the Reservation Folio Page, stating that the folio had already been created.</li></ul>
<strong>72958 No longer able to set routing rule "CPR" without setting a customer account</strong>
<ul><li>
<p>An error was fixed, when changing to routing rule with Company folios and no Customer set. Now it is possible.</p>
</li></ul>
<strong>72911 Reconciliation Tool Issues II - Errors in different processes</strong>
<ul><li>An issue was fixed, when running search in reconciliation page (Reservation Folio does not exist...) and also an issue in fixing process for duplicated charges ( Line was not allowed to be changed).</li></ul>
<strong>72792 Reservation Balance amount on Checkout confirmation window is different than Reservation Balance</strong>
<ul><li>A wrong balance amount was shown in Checkout confirmation. It did not include tax/vat. This was fixed. </li></ul>
<strong>72464 Error when changing Line Discount % on copied posted sales invoice from hotels</strong>
<ul><li>An issue was fixed on changing discount on copy invoice from posted sales invoice from Hotels. The user can apply discounts with limitations on lines with Acc. Tax Included In Rate.</li><li>Additionally, another issue was fixed on posting credit memo.</li></ul>
<strong>71541 Usability Enhancements to Reservation Extras</strong>
<ul><li>Introduced three views: <b>Simple</b>, <b>Standard</b>, and <b>Detailed</b>, allowing users to choose the level of detail for a cleaner and more customizable experience.</li><li>Added a new page: <b>Reservation Extras Worksheet</b>, accessible from the Reservation Extras subpage for easier management and overview.</li><li>Reservation Extras included in the rate are now <b>hidden by default</b> to reduce clutter. Users can toggle their visibility using the <b>Show/Hide Rate Lines</b> action.</li></ul>
<strong>71535 Dynamically show or hide columns DRE page for quick editing</strong>
<ul><li>A new filter <b>View Mode</b>, was added to the Hotel Invoice Management to enhance the usability of the Detailed Revenue Entries (DRE) in the invoice management page. The view modes are:<ul><li><b>Simple</b> - This only shows the Date, Description, Quantity, UOM, Unit Price, Line Disc% and Amount fields</li><li><b>Standard</b> - This also shows the Reservation No., Paying Res No. and Folio fields</li><li><b>Detailed</b> - This shows all the fields in the DRE</li></ul></li><li><b>Simple</b> - This only shows the Date, Description, Quantity, UOM, Unit Price, Line Disc% and Amount fields</li><li><b>Standard</b> - This also shows the Reservation No., Paying Res No. and Folio fields</li><li><b>Detailed</b> - This shows all the fields in the DRE</li></ul>
