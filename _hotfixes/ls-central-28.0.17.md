---
title: "LS Central hotfixes - 28.0.17, Release date May 27, 2026 - Hotfixes"
product: LS Central
version: "28.0.17"
subproduct: 
minor_version: "28.0"
date: 2026-05-27 00:00:00+00:00
order: 8
guid: 7459e28c42649c4191652a5a07b798708e515a50
---

<strong>82590 AL: Discount does not include non variant products</strong>
<ul><li>There were issues with discount that were sent to Shopify where item was without discount, and item with discount on one dimension were not sent correctly to shopify. This was fixed. </li></ul>
<strong>82583 AL: Business Central Currency & Shopify Order import - Best practice</strong>
<ul><li>The way that currency handling is done was changed, during Customer Order create from Shopify order, if order is in local currency and no currency entry exist for LCY.</li></ul>
<strong>82333 WS language issue when using birthday discount</strong>
<ul><li>Details not available.</li></ul>
<strong>81984 Improve rental activity creation and linking flow in LS Central for Bookings</strong>
<ul><li><b>Create a new client without leaving the booking screen</b>
<ul>
<li>It is now possible to create a new member account and contact directly from the Client No. field on both the Reservation Card and the Activity Card. When the Client No. field is empty, clicking the assist-edit button (...) opens a guided New Client form where you enter the client's personal details, contact information, and address. On confirmation the new client is created and immediately linked to the booking.</li>
<li>If the client field already contains a value, the assist-edit button opens the existing client's contact card as before.</li>
</ul>
</li><li><b>New Client form</b>
<ul>
<li>A new <b>New Client Card</b> form collects the following information before creating the member record:<ul><li>Personal information: First name, middle name, last name, gender, date of birth</li><li>Contact information: Email, phone, mobile phone, receipt preference</li><li>Address: Address lines, house/apartment number, post code, city, state/province, country, territory code</li></ul></li>
</ul>
</li><li><b>Improved "New Client" action in Activity Client Search</b>
<ul>
<li>The New Client action on the Activity Client Search page now uses the same guided New Client form, replacing the previous flow that opened the full Member Account page.</li>
</ul>
</li><li><b>Resource Status — booking linked to current reservation and client</b>
<ul>
<li>When adding an activity from the Resource Status page opened within a Reservation, the new booking is now automatically associated with the correct reservation number and client. <ul><li>Previously, these values were not passed through.</li></ul></li>
<li>The Resource Status page now opens as a modal dialog so the reservation card refreshes correctly after a resource is selected.</li>
</ul>
</li><li><b>Activity Contact Card — additional address fields</b>
<ul>
<li>The Post Code and Country/Region Code fields are now visible on the Activity Contact Card, making it possible to view and edit the full address without navigating to the full member contact record.</li>
</ul>
</li></ul>
