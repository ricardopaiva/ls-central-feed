---
title: "Hotels hotfixes - 28.0.13 Hotels, Release date June 2, 2026 - Hotfixes"
product: Hotels
version: "28.0.13"
subproduct: Hotels
minor_version: "28.0"
date: 2026-06-02 00:00:00+00:00
order: 45
guid: 52104ee2ada96f87d9f3f6ecbec21b5f883eed2c
---

<strong>82706 POS Preview Invoice fails with 'string > 30 characters' when Room Type + Rate Code label exceeds 30 chars</strong>
<ul><li>Running <b>Preview Invoice</b> from a Hotel reservation in the POS no longer fails when the combined Room Type and Rate Code labels are long. <ul><li>Previously, if the formatted rate header (&lt;Room Type&gt; Room - &lt;Rate Code&gt; Rate) was longer than 30 characters — for example, Room Type EXECUTIVE PLUS with Rate Code 2026 — the report aborted with <b>The length of the string is 31, but it must be less than or equal to 30 characters</b>.</li><li> Both Preview Invoice and the equivalent Posted Invoice report now render successfully and show the full rate header label.</li></ul></li><li>Action required by partners:<ul><li>None. The fix is applied automatically with the version update; no setup or data migration is required.</li></ul></li></ul>
<strong>82676 Preview Posting Invoice on Group Reservation consumes Sales Invoice number series and may leave dangling Sales Header</strong>
<ul><li>The <b>Preview Posting Invoice</b> action on a Group Reservation is now properly read-only. Clicking it no longer increments the Sales Invoice number series, no longer creates a real Sales Header in the database, and no longer leaves any dangling unposted invoice behind if the preview screen errors out. <ul><li>Real (non-preview) invoice posting is unaffected and continues to consume one number per posted invoice as expected.</li></ul></li><li>Action required by partners:<ul><li>None for new transactions. Any Group Reservations where past Preview clicks left an unposted Sales Header behind should be reviewed and the orphaned headers deleted as a one-off cleanup — these will not be removed automatically by the upgrade.</li></ul></li></ul>
