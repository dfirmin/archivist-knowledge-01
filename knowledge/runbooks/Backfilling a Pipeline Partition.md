---
type: Runbook
title: Backfilling a Pipeline Partition
description: How to rebuild a daily partition of a warehouse table when it is missing or loaded with bad data.
tags: [runbook, data-engineering]
status: draft
generated:
  by: archivist-author/1
  at: 2026-10-04T04:29:21Z
sources:
  - resource: sources/processed/backfill-pipeline-partition.md
    title: Backfilling a Pipeline Partition
okfx_structure: routine-procedure
okfx_team: data-engineering
okfx_on_call: "#data-eng-oncall"
okfx_gaps: []
okfx_confidence: 1.0
verified:
  - by: process:archivist-verifier/1
    at: 2026-10-04T04:30:32Z
---

## When To Use

Use this when a daily partition of a warehouse table is missing or loaded with bad data and must be rebuilt.

*Source: [Backfilling a Pipeline Partition](sources/processed/backfill-pipeline-partition.md), retrieved 2026-10-04*

## Prerequisites

You have the `de-operator` role in the orchestrator. The upstream source data for that day is available.

*Source: [Backfilling a Pipeline Partition](sources/processed/backfill-pipeline-partition.md), retrieved 2026-10-04*

## Steps

1. Pause the table's scheduled DAG so it does not overwrite your backfill.
2. Run the backfill job for the partition date: `backfill --table <name> --date <YYYY-MM-DD>`.
3. Compare the row count with the source system's count for that day.
4. Unpause the DAG.

*Source: [Backfilling a Pipeline Partition](sources/processed/backfill-pipeline-partition.md), retrieved 2026-10-04*

## Verification

Row counts match within 0.1% and the data quality checks for the partition pass.

*Source: [Backfilling a Pipeline Partition](sources/processed/backfill-pipeline-partition.md), retrieved 2026-10-04*

## Rollback

If the backfill loads bad data, restore the partition from the previous night's snapshot with `restore --table <name> --date <YYYY-MM-DD>` and unpause the DAG.

*Source: [Backfilling a Pipeline Partition](sources/processed/backfill-pipeline-partition.md), retrieved 2026-10-04*
