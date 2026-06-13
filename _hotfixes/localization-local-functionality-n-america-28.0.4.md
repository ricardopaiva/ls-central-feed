---
title: "Localization hotfixes - 28.0.4 Local Functionality N-America, Release date May 5, 2026 - Hotfixes"
product: Localization
version: "28.0.4"
subproduct: Local Functionality N-America
minor_version: "28.0"
date: 2026-05-05 00:00:00+00:00
order: 65
guid: 858da51ac9a3a85ff6d49ff7b9ecc1055174db7f
---

<strong>81445 Quantity showing difference after recent LSC upgrade</strong>
<ul><li>There was an issue where POS item quantities were displayed with forced decimal places (such as, <b>1.00</b> instead of <b>1</b>) after an LSC upgrade.</li><li>The scale rounding format logic in the localized ScaleUtility codeunit was corrected to respect integer quantities.</li></ul>
<strong>81015 LSC NA - Penny Rounding Customer Order</strong>
<ul><li>There was an issue where penny rounding on Customer Order deposits was calculated incorrectly per payment line, causing pre-approved payment amounts to not match the order total.</li><li>This also caused order cancelation to incorrectly generate a spurious small negative deposit refund line on the POS.</li></ul>
<strong>79090 LSC NA - scale/receipt certification Canada</strong>
<ul><li>The currency symbol display on customer receipts can now be configured to print the symbol inline with each amount, fulfilling Canadian scale and receipt certification requirements.</li><li>A new <b>Print Currency Symbol with Amounts</b> setting on the Functionality Profile replaces the previous on/off toggle with three options: <ol><li value="1">No symbol.</li><li value="2">Symbol in the amount column header, or</li><li value="3">symbol printed with every amount.</li></ol></li></ul>
