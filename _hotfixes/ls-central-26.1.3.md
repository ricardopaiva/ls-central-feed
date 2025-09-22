---
title: "LS Central hotfixes - 26.1.3, Release date July 1, 2025 - Hotfixes"
product: LS Central
version: "26.1.3"
date: 2025-07-01 00:00:00+00:00
---

<strong>68644 Public Methods in Periodic Discounts #531</strong>
<ul><li><li>Made three procedures publicly available in Periodic discount.</li></li></ul>
<strong>68622 New Events in Statement-Calculate #529</strong>
<ul><li><li>New Event <b>OnBeforeFindLastTenderDecl</b> in Statement-Calculate codeunit.</li></li></ul>
<strong>68578 Bug in Posted Statement - Navigate code</strong>
<ul><li><li>Fixed overflow issue in <b>Find Entries code</b> when using long values in External Document number.</li></li></ul>
<strong>68533 Logo printing when set on POS Terminal card does not work</strong>
<ul><li><li>Details not available.</li></li></ul>
<strong>68521 Rounding error when only part of voided line was refunded</strong>
<ul><li><li>Rounding error occurs in <b>Edit Customer order</b> when voiding single line, and only refunds part of the amount. This was fixed.</li></li></ul>
<strong>68492 Gift card issue Error</strong>
<ul><li><li>Details not available.</li></li></ul>
<strong>68433 Reprice on refund when member added - HF</strong>
<ul><li><li>Reprice on refund skipped. This was fixed.</li></li></ul>
<strong>68155 Creating membership card with more than 20 characteres at POS</strong>
<ul><li><li>Prevented overflow error on POS when Member Card length exceeds twenty characters.</li></li></ul>
<strong>68036 Error Message The member coupon buffer does not exist</strong>
<ul><li><li>Details not available.</li></li></ul>
<strong>67938 TestCurrentInput should return InputValue for Dynamic Query #516</strong>
<ul><li><li><b>TestCurrentInput</b> returns <b>InputValue</b> for Dynamic Query.</li></li></ul>
<strong>67894 Creating Retail Item Barcode from Mask using Item number fails</strong>
<ul><li><li>It is now possible to create a barcode from a barcode mask, including item number.</li></li></ul>
<strong>67601 Printer shows infinite "Opening drawer" when paper empty</strong>
<ul><li><li>Details not available.</li></li></ul>
<strong>67568 Retrieve valid price from closed price list #507</strong>
<ul><li><li>Details not available.</li></li></ul>
<strong>67285 Customer Order Refund incorrect Refund Status</strong>
<ul><li><li>Wrong Refund status was displayed on Customer Order. This was fixed. If not refunded on POS, <b>Payment Pending</b> should be displayed.</li></li></ul>
<strong>66098 Serial Number handling on the POS</strong>
<ul><li><li>New option was added in Retail item card <b>LSC Assign SerialNo/LotNo In CO Picking</b>, which specifies whether to delay assigning SerialNo/LotNo until the picking of the item in the Customer Order. If this field is selected, the SerialNo/LotNo is assigned when the item is picked in the CO. If this field is not selected, the SerialNo/LotNo is assigned when the item is added to POS.</li></li></ul>
<strong>64466 Reprice on refund when member added</strong>
<ul><li><li>Reprice on refund skipped. This was fixed.</li></li></ul>
