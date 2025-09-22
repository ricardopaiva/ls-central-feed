---
title: "Localization hotfixes - 26.1.6 Local Functionality Germany, Release date September 18, 2025 - Hotfixes"
product: Localization
version: "26.1.6 Local Functionality Germany"
date: 2025-09-18 00:00:00+00:00
---

<strong>69704 CashPointClosings do not work in Germany's Fiskaly implementation</strong>
<ul><li><li>Improved Cash Point Closing refresh processes.</li></li>
<li><li>Fixed Business date source.</li></li></ul>
<strong>70647 CashPointClosing - add non required objects</strong>
<ul><li><li>Included <b>non-required</b> fields, that are necessary to have a correct export.<ul><li>payment_types</li><li>amounts_per_vat_id</li><li>lines</li></ul></li></li>
<li><li>payment_types</li></li>
<li><li>amounts_per_vat_id</li></li>
<li><li>lines</li></li>
<li><li>New field on Tender Type Setup - Fiskaly Tender Type. Values:<ul><li>Bar</li><li>Unbar</li><li>ECKarte</li><li>Kreditkarte</li><li>ElZahlungsdienstleister</li><li>GuthabenKarte</li><li>Keine</li></ul></li></li>
<li><li>Bar</li></li>
<li><li>Unbar</li></li>
<li><li>ECKarte</li></li>
<li><li>Kreditkarte</li></li>
<li><li>ElZahlungsdienstleister</li></li>
<li><li>GuthabenKarte</li></li>
<li><li>Keine</li></li>
<li><li>Obsoleted: Store Card - <b>Update DSFinV-K VAT Definitions</b> action</li></li>
<li><li>Adjusted <b>LSCDE DSFinV-K Export ID</b> on <b>POS VAT Code</b> table<ul><li>Old Minimum value 1000, New minimum value 0<ul><li>This is for setting <b>default</b> Fiskaly defined IDs, custom IDs are from 1000-9999 as they were.</li></ul></li></ul></li></li>
<li><li>Old Minimum value 1000, New minimum value 0<ul><li>This is for setting <b>default</b> Fiskaly defined IDs, custom IDs are from 1000-9999 as they were.</li></ul></li></li>
<li><li>This is for setting <b>default</b> Fiskaly defined IDs, custom IDs are from 1000-9999 as they were.</li></li>
<li><li>
<p>On POS VAT Code page, the <b>Generate VAT Definitions</b> action updates every store with DSFINV-K enabled using the store's credentials.</p>
</li></li></ul>
<strong>70831 LSC DE - Error in Fiskaly Integration prevents statements from being posted</strong>
<ul><li><li>Details not available.</li></li></ul>
<strong>71488 LSC DE Localisation bring PopUp in POS</strong>
<ul><li><li>Details not available.</li></li></ul>
