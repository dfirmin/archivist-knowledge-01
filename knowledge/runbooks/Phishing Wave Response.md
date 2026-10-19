---
type: Runbook
title: Phishing Wave Response
description: Agreed actions, checks and escalation for a phishing wave that harvests credentials with a fake DocuSign payroll email.
tags: [runbook, security]
status: draft
generated: {by: archivist-author/1, at: 2026-10-05T23:38:41Z}
verified: [{by: process:archivist-verifier/1, at: 2026-10-05T23:38:57Z}]
sources:
  - {resource: sources/processed/phishing-incident-notes.md, title: "IR sync — phishing wave — notes (rough!!)"}
okfx_structure: incident-response
okfx_placement: {outcome: new}
okfx_team: security
okfx_on_call: "#security-incidents"
okfx_gaps: []
okfx_confidence: 1.0
---

# Phishing Wave Response

## Symptoms

Users report emails titled "DocuSign: review payroll change" that lead to a credential harvest page. About 40 reports came in since 8am, and 3 users confirmed they entered credentials.

*Source: [IR sync — phishing wave — notes (rough!!)](sources/processed/phishing-incident-notes.md), retrieved 2026-10-05*

## Impact

Payroll fraud is possible if credentials were used on the HR system. So far no access has been seen.

*Source: [IR sync — phishing wave — notes (rough!!)](sources/processed/phishing-incident-notes.md), retrieved 2026-10-05*

## Immediate Actions

- Block the sender domain and URL at the email gateway and proxy (Omar).
- Force a password reset and revoke sessions for the 3 users, and check MFA logs for new devices (Kat).
- Pull all copies of the email from mailboxes by purging them (Omar).
- Raj drafts an all-staff "don't click" message, and security reviews it.

*Source: [IR sync — phishing wave — notes (rough!!)](sources/processed/phishing-incident-notes.md), retrieved 2026-10-05*

## Diagnosis

In EDR, look for logins from new countries or devices for the affected accounts in the last 24 hours.

*Source: [IR sync — phishing wave — notes (rough!!)](sources/processed/phishing-incident-notes.md), retrieved 2026-10-05*

## Escalation

If any of the 3 users had admin rights, treat the incident as major and wake up the IC.

*Source: [IR sync — phishing wave — notes (rough!!)](sources/processed/phishing-incident-notes.md), retrieved 2026-10-05*

## Follow-up

After the incident, write up a timeline and lessons learned within 3 days (Lena). Who decides whether to notify the insurer is an open question to ask legal.

*Source: [IR sync — phishing wave — notes (rough!!)](sources/processed/phishing-incident-notes.md), retrieved 2026-10-05*
