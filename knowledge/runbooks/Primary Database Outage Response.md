---
type: Runbook
title: Primary Database Outage Response
description: Who decides on replica promotion during a primary database outage, and when and where the DBA on-call is paged.
tags: [runbook, platform]
status: draft
generated: {by: archivist-author/1, at: 2026-10-05T23:55:21Z}
verified:
  - {by: process:archivist-verifier/1, at: 2026-10-05T23:55:32Z}
sources:
  - {resource: sources/processed/2026-10-02-db-outage-retro-call--primary-database-outage-runbook.md, title: "Primary Database Outage Runbook — promotion decision and DBA escalation changes"}
okfx_structure: incident-response
okfx_placement: {outcome: new}
okfx_team: platform
okfx_on_call: "#platform-oncall"
okfx_confidence: 0.75
okfx_gaps:
  - kind: missing_section
    origin: documentation
    description: Three required sections (Symptoms, Impact, Diagnosis) contain only "Awaiting
      source material" stubs with no substantive content. The cited source addresses only
      Immediate Actions and Escalation; Symptoms, Impact, and Diagnosis remain undocumented.
---

## Symptoms

*[Awaiting source material.]*

## Impact

*[Awaiting source material.]*

## Immediate Actions

The runbook says to wait 10 minutes before promoting. The incident commander decides on promotion, not whoever is at the keyboard. In the outage being reviewed, promotion waited longer than 10 minutes because nobody owned the call.

*Source: [Primary Database Outage Runbook — promotion decision and DBA escalation changes](sources/processed/2026-10-02-db-outage-retro-call--primary-database-outage-runbook.md), retrieved 2026-10-05*

## Diagnosis

*[Awaiting source material.]*

## Escalation

Page the DBA on-call if the primary is not back in 15 minutes. The draft said 30, but this was changed to 15 because 30 is too long for a customer-facing outage. The DBA on-call is the #dba-oncall channel, not the platform one.

*Source: [Primary Database Outage Runbook — promotion decision and DBA escalation changes](sources/processed/2026-10-02-db-outage-retro-call--primary-database-outage-runbook.md), retrieved 2026-10-05*
