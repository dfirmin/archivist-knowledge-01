---
type: Runbook
title: Oncall Handoff
description: Weekly oncall handoff procedure run by the outgoing oncall person every Monday at 10am ET.
tags:
  - runbook
  - platform
status: draft
generated:
  by: archivist-author/1
  at: 2026-10-04T04:57:13Z
sources:
  - resource: sources/processed/slack-oncall-handoff.md
    title: "#platform-oncall — exported thread, Thu Oct 1 2026"
okfx_structure: routine-procedure
okfx_team: platform
okfx_on_call: "#platform-oncall"
okfx_gaps: []
okfx_confidence: 1.00
verified:
  - by: process:archivist-verifier/1
    at: 2026-10-04T04:58:54Z
  - by: process:archivist-verifier/1
    at: 2026-10-04T05:10:37Z
  - by: process:archivist-verifier/1
    at: 2026-10-04T05:27:54Z
---

## When To Use

This procedure is run every Monday at 10am ET by the outgoing oncall person to hand off oncall responsibilities to the incoming person. The handoff takes approximately 15 minutes.

*Source: [#platform-oncall — exported thread, Thu Oct 1 2026](sources/processed/slack-oncall-handoff.md), retrieved 2026-10-04*

## Prerequisites

Access to the following is required before beginning the handoff:
- The #platform-oncall Slack channel for posting the handoff note
- PagerDuty for reassigning the pager schedule override
- The SLO dashboard for checking error budget status

*Source: [#platform-oncall — exported thread, Thu Oct 1 2026](sources/processed/slack-oncall-handoff.md), retrieved 2026-10-04*

## Steps

1. Check the SLO dashboard and note anything burning error budget in the handoff note. This must be done before the call with the incoming person.
2. Post the handoff note in #platform-oncall using the template. The note should include open incidents, flaky alerts, and anything weird.
3. Reassign the pager schedule override in PagerDuty to the incoming person.
4. Walk through open tickets with the incoming person on a quick call.
5. The incoming person triggers a test page and acknowledges it to verify that paging works.
6. If the test page does not arrive, the incoming person must tell the platform lead before the outgoing person signs off.

*Source: [#platform-oncall — exported thread, Thu Oct 1 2026](sources/processed/slack-oncall-handoff.md), retrieved 2026-10-04*

## Verification

The incoming person triggers a test page and acknowledges it. If the test page arrives and is successfully acknowledged, paging is verified to be working.

*Source: [#platform-oncall — exported thread, Thu Oct 1 2026](sources/processed/slack-oncall-handoff.md), retrieved 2026-10-04*
