---
title: "Primary Database Outage Runbook — promotion decision and DBA escalation changes"
extracted_from: sources/processed/2026-10-02-db-outage-retro-call.md
---

About: The primary database outage response runbook (Platform): who decides on replica promotion, and when and where the DBA on-call is paged.

> [00:00:46] Priya Raman: which honestly was too late. the runbook says wait 10 minutes before promoting and we waited longer because nobody owned the call
> [00:00:58] Dana Ruiz: right so that's change number one. the incident commander decides on promotion, not whoever's at the keyboard
> [00:01:05] Lev Sato: +1

> [00:01:10] Dana Ruiz: and change two. we page the DBA on-call if the primary isn't back in 15 minutes
> [00:01:16] Priya Raman: wait I thought we said 30 last time
> [00:01:19] Dana Ruiz: we did say 30 in the draft, but no, it's 15. 30 is way too long for a customer-facing outage
> [00:01:26] Priya Raman: ok 15, got it
> [00:01:28] Lev Sato: DBA on-call is the #dba-oncall channel right, not the platform one
> [00:01:32] Dana Ruiz: yes #dba-oncall
