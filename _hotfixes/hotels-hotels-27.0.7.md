---
title: "Hotels hotfixes - 27.0.7 Hotels, Release date December 2, 2025 - Hotfixes"
product: Hotels
version: "27.0.7"
subproduct: Hotels
minor_version: "27.0"
date: 2025-12-02 00:00:00+00:00
order: 46
guid: c2173a483f5e63c0adfc5f21d4f1f0b3f00a4065
---

<strong>75275 Service Charge (Retail Charge) from Stores - Charge to Room when settled on POS and after the posted statement is entered into a G/L account similar to the Accommodation Item No. (Gen Posting Setup - Sales Account)</strong>
<ul><li>Retail Charge was not posted to the correct G/L Account when Charging to Room. The Retail Charge is now posted to the <b>POS Transfer Account</b> in the Hotel Setup, NOT <b>Night Audit Temp Balance</b> as before.</li></ul>
<strong>75231 Add Posting No. series to folio invoice setup and add events for invoice management</strong>
<ul><li><b>Changes in Reservation Folio page</b>
<ul>
<li>A new field was added to <b>Posting No. Series</b>, to Reservation Folio page to custom posting series in invoice created from folio. </li>
<li>A new action was added to <b>Reset invoicing fields values</b>. </li>
<li>Some fields were regrouped in new groups (Payment and Posting).</li>
</ul>
</li><li>A new field was added to <b>Posting No. Series</b>, to Reservation Folio page to custom posting series in invoice created from folio. </li><li>A new action was added to <b>Reset invoicing fields values</b>. </li><li>Some fields were regrouped in new groups (Payment and Posting).</li><li><b>Changes in Invoice creation and posting flow</b>
<ul>
<li>Error handling was improved along posting process, now an error list is shown on page as standard and also opens the folio created to allow the customer to fix it manually.</li>
<li>A new event was added to allow customization of invoice creation process:<ul><li><b>HotelInvoiceMgt_OnAfterCreateSalesDoc</b>: It happens after any sales docs and lines are created.</li><li><b>HotelInvoiceMgt_OnBeforeCreateInvoiceHeader</b>: It happens before creating invoice header. It allows skipping standard process and sets a custom one.</li><li><b>HotelInvoiceMgt_OnBeforeCreateInvoiceLines</b>: It happens before creating invoice lines, after the header was created correctly. It allows you to override the process to create inv. lines or to  do any changes before because of that.</li></ul></li>
</ul>
</li><li>Error handling was improved along posting process, now an error list is shown on page as standard and also opens the folio created to allow the customer to fix it manually.</li><li>A new event was added to allow customization of invoice creation process:<ul><li><b>HotelInvoiceMgt_OnAfterCreateSalesDoc</b>: It happens after any sales docs and lines are created.</li><li><b>HotelInvoiceMgt_OnBeforeCreateInvoiceHeader</b>: It happens before creating invoice header. It allows skipping standard process and sets a custom one.</li><li><b>HotelInvoiceMgt_OnBeforeCreateInvoiceLines</b>: It happens before creating invoice lines, after the header was created correctly. It allows you to override the process to create inv. lines or to  do any changes before because of that.</li></ul></li><li><b>HotelInvoiceMgt_OnAfterCreateSalesDoc</b>: It happens after any sales docs and lines are created.</li><li><b>HotelInvoiceMgt_OnBeforeCreateInvoiceHeader</b>: It happens before creating invoice header. It allows skipping standard process and sets a custom one.</li><li><b>HotelInvoiceMgt_OnBeforeCreateInvoiceLines</b>: It happens before creating invoice lines, after the header was created correctly. It allows you to override the process to create inv. lines or to  do any changes before because of that.</li></ul>
<strong>75225 Invoice fix for charge2room lines</strong>
<ul><li>There was an issue with <b>charge2room</b> revenue lines, check was removed, that enforced use of GL/Account in invoice sales lines.</li></ul>
<strong>75136 Staging Import Process Improvements</strong>
<ul><li>Improvements were made to the staging import process to enhance guest identification and reservation numbering.<ul><li><b>Guest Identification and Linking:</b><ul><li><b>Existing Member Check:</b> The system now attempts to identify existing guests by matching the Guest Name and Email against Member Contacts.</li><li><b>Link to Member:</b> If a match is found, the imported reservation is correctly linked to the existing Member Contact No. </li></ul></li><li><b>Reservation Number Generation:</b> <ul><li><b>No. Series Integration:</b> The manual assignment of Reservation Numbers using a counte rwas removed. The import process now relies on standard No. Series generation, ensuring consistent and correct reservation numbering.</li></ul></li></ul></li><li><b>Guest Identification and Linking:</b><ul><li><b>Existing Member Check:</b> The system now attempts to identify existing guests by matching the Guest Name and Email against Member Contacts.</li><li><b>Link to Member:</b> If a match is found, the imported reservation is correctly linked to the existing Member Contact No. </li></ul></li><li><b>Existing Member Check:</b> The system now attempts to identify existing guests by matching the Guest Name and Email against Member Contacts.</li><li><b>Link to Member:</b> If a match is found, the imported reservation is correctly linked to the existing Member Contact No. </li><li><b>Reservation Number Generation:</b> <ul><li><b>No. Series Integration:</b> The manual assignment of Reservation Numbers using a counte rwas removed. The import process now relies on standard No. Series generation, ensuring consistent and correct reservation numbering.</li></ul></li><li><b>No. Series Integration:</b> The manual assignment of Reservation Numbers using a counte rwas removed. The import process now relies on standard No. Series generation, ensuring consistent and correct reservation numbering.</li></ul>
<strong>75134 Preview invoice blank lines</strong>
<ul><li>The Preview Invoice report was adapted to also work with Group Reservations.</li></ul>
<strong>73577 Not possible to change dates and room type at the same time</strong>
<ul><li>Fixed some issues when applying changes to the rates on the Rate Change Page.</li></ul>
