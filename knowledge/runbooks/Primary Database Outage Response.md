---
type: Runbook
title: Primary Database Outage Response
description: "Runbook changes agreed in the retro: the incident commander decides on replica promotion, and the DBA on-call is paged after 15 minutes."
tags: [runbook, platform]
status: draft
generated: {by: archivist-author/1, at: 2026-10-05T23:36:50Z}
verified: [{by: process:archivist-verifier/1, at: 2026-10-05T23:37:03Z}]
sources:
  - {resource: sources/processed/2026-10-02-db-outage-retro-call--primary-database-outage-response.md, title: "Primary Database Outage Response — promotion decision and DBA escalation timing"}
okfx_structure: incident-response
okfx_placement: {outcome: new}
okfx_team: platform
okfx_on_call: "#platform-oncall"
okfx_confidence: 0.75
okfx_gaps:
  - kind: missing_section
    origin: documentation
    description: The Symptoms, Impact, and Diagnosis sections hold only "Awaiting source material"
      stubs. The cited source does not provide this information.
---

# Primary Database Outage Response

## Symptoms

*[Awaiting source material.]*

## Impact

*[Awaiting source material.]*

## Immediate Actions

The runbook says to wait 10 minutes before promoting the replica. In the incident the team waited longer because nobody owned the call. The incident commander decides on promotion, not whoever is at the keyboard.

*Source: [Primary Database Outage Response — promotion decision and DBA escalation timing](sources/processed/2026-10-02-db-outage-retro-call--primary-database-outage-response.md), retrieved 2026-10-05*

## Diagnosis

*[Awaiting source material.]*

## Escalation

Page the DBA on-call if the primary is not back in 15 minutes. The DBA on-call is the #dba-oncall channel, not the platform one. The 15-minute threshold replaces the 30 minutes in the earlier draft, which was judged too long for a customer-facing outage.

*Source: [Primary Database Outage Response — promotion decision and DBA escalation timing](sources/processed/2026-10-02-db-outage-retro-call--primary-database-outage-response.md), retrieved 2026-10-05*
