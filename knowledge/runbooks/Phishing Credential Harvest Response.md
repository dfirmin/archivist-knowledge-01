---
type: Runbook
title: Phishing Credential Harvest Response
description: How to respond when users report phishing emails that harvest credentials.
tags:
  - runbook
  - security
status: draft
generated:
  by: archivist-author/1
  at: 2026-10-04T04:43:57Z
sources:
  - resource: sources/processed/phishing-incident-notes.md
    title: IR sync — phishing wave — notes (rough!!)
verified:
  - by: process:archivist-verifier/1
    at: 2026-10-04T04:45:17Z
  - by: process:archivist-verifier/1
    at: 2026-10-04T05:07:35Z
  - by: process:archivist-verifier/1
    at: 2026-10-04T05:37:37Z
okfx_structure: incident-response
okfx_team: security
okfx_on_call: "#security-incidents"
okfx_gaps:
  - kind: missing_escalation
    origin: documentation
    description: The Escalation section provides no specific person, team, or channel to contact;
      it only states 'wake up the incident commander' without specifying how to reach them.
okfx_confidence: 0.60
---

## Symptoms

Users report emails with subject lines like "DocuSign: review payroll change" that link to credential harvest pages. Approximately 40 reports were received since 8am, with 3 users confirmed to have entered credentials.

*Source: [IR sync — phishing wave — notes (rough!!)](sources/processed/phishing-incident-notes.md), retrieved 2026-10-04*

## Impact

Possible payroll fraud if compromised credentials are used on the HR system. So far no unauthorized access has been observed.

*Source: [IR sync — phishing wave — notes (rough!!)](sources/processed/phishing-incident-notes.md), retrieved 2026-10-04*

## Immediate Actions

Block the sender domain and malicious URL at both the email gateway and web proxy. Force password reset and revoke active sessions for users who entered credentials, then check MFA logs for any new devices. Pull all copies of the phishing email from mailboxes (purge).

*Source: [IR sync — phishing wave — notes (rough!!)](sources/processed/phishing-incident-notes.md), retrieved 2026-10-04*

## Diagnosis

Use EDR to look for logins from new countries or devices for affected accounts in the last 24 hours. If any of the 3 affected users had admin rights, treat as a major incident and wake up the incident commander.

*Source: [IR sync — phishing wave — notes (rough!!)](sources/processed/phishing-incident-notes.md), retrieved 2026-10-04*

## Escalation

If any affected users had admin rights, treat as a major incident and wake up the incident commander.

*Source: [IR sync — phishing wave — notes (rough!!)](sources/processed/phishing-incident-notes.md), retrieved 2026-10-04*

## Follow-up

Have communications draft an all-staff "don't click" message for security review. Write up the timeline and lessons learned within 3 days of the incident. Determine with legal whether the insurer needs to be notified (ownership unclear—confirm with legal).

*Source: [IR sync — phishing wave — notes (rough!!)](sources/processed/phishing-incident-notes.md), retrieved 2026-10-04*
