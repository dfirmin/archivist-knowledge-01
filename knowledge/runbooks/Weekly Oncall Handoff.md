---
type: Runbook
title: Weekly Oncall Handoff
description: How the outgoing oncall person hands over to the incoming person every Monday at 10am ET.
tags: [runbook, platform]
status: draft
generated: {by: archivist-author/1, at: 2026-10-05T23:40:20Z}
verified: [{by: process:archivist-verifier/1, at: 2026-10-05T23:40:36Z}]
sources:
  - {resource: sources/processed/slack-oncall-handoff.md, title: "#platform-oncall exported thread, Thu Oct 1 2026"}
okfx_structure: routine-procedure
okfx_placement: {outcome: new}
okfx_team: platform
okfx_on_call: "#platform-oncall"
okfx_confidence: 0.80
okfx_gaps:
  - kind: missing_section
    origin: documentation
    description: The Prerequisites section contains only a stub ('Awaiting source material'),
      and the cited source (sources/processed/slack-oncall-handoff.md) does not mention any
      prerequisites or preconditions needed for the handoff.
---

## When To Use

The outgoing person runs the handoff every Monday at 10am ET. It takes about 15 minutes.

*Source: [#platform-oncall exported thread, Thu Oct 1 2026](sources/processed/slack-oncall-handoff.md), retrieved 2026-10-05*

## Prerequisites

*[Awaiting source material.]*

## Steps

1. Check the SLO dashboard and note anything burning error budget in the handoff note. Do this before the call.
2. Post the handoff note in #platform-oncall using the template (open incidents, flaky alerts, anything weird).
3. Reassign the pager schedule override in PagerDuty to the incoming person.
4. Walk through open tickets with the incoming person on a quick call.
5. Last step: the incoming person triggers a test page and acks it.

*Source: [#platform-oncall exported thread, Thu Oct 1 2026](sources/processed/slack-oncall-handoff.md), retrieved 2026-10-05*

## Verification

The test page and its ack show that paging works. If the test page does not arrive, tell the platform lead before the outgoing person signs off.

*Source: [#platform-oncall exported thread, Thu Oct 1 2026](sources/processed/slack-oncall-handoff.md), retrieved 2026-10-05*
