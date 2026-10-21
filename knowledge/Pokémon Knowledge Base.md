---
type: Reference
title: "Pokémon Knowledge Base"
description: "Entry point to the Pokémon knowledge base: what it covers, how it is organised by region and then primary type, and where to start."
tags: [pokemon, overview, entry-point]
status: draft
verified:
  - {by: "human:Dee", at: 2026-10-21T21:40:01Z}
---

# Pokémon Knowledge Base

## What this is

This is a Pokédex: one document for every Pokémon species (its default form), covering its types, base stats, type matchups, abilities, size and evolution. It follows the Open Knowledge Format, so every document is Markdown with YAML frontmatter, and every fact traces back to a source in `sources/processed/`, mostly the PokéAPI data extracts for each region.

## How it is organised

Documents are sorted first by the region where the Pokémon was first found, then by its primary type. A Pokémon's path looks like `knowledge/{region}/{primary type}/{Name}.md`, so Mewtwo lives at `knowledge/kanto/psychic/Mewtwo.md`. Regional forms belong to the same species document.

Each region also has an overview document that lists every Pokémon found there, grouped by primary type, with National Pokédex numbers and base stat totals. Those overviews are the best place to start browsing.

## Regions

| Region | Generation | Pokémon | Start here |
|---|---|---|---|
| Kanto | I | 151 | [Kanto Overview](kanto/Kanto%20Overview.md) |
| Johto | II | 100 | [Johto Overview](johto/Johto%20Overview.md) |
| Hoenn | III | 135 | [Hoenn Overview](hoenn/Hoenn%20Overview.md) |
| Sinnoh | IV | 107 | [Sinnoh Overview](sinnoh/Sinnoh%20Overview.md) |
| Unova | V | 156 | [Unova Overview](unova/Unova%20Overview.md) |
| Kalos | VI | 72 | [Kalos Overview](kalos/Kalos%20Overview.md) |
| Alola | VII | 88 | [Alola Overview](alola/Alola%20Overview.md) |
| Galar | VIII | 96 | [Galar Overview](galar/Galar%20Overview.md) |
| Paldea | IX | 120 | [Paldea Overview](paldea/Paldea%20Overview.md) |

## What each Pokémon document contains

Every Pokémon document has an Overview, Base Stats, Type Matchups, Abilities, Size and Evolution section, and an Open Questions section where review questions are collected. Some also have Where to Find and Strategy Notes sections, when a source provides them.

## Known gaps

Some documents are still missing information, such as strategy notes, habitat details or confirmed stats. Documents whose status is verified have had their facts confirmed by a person; documents marked draft have not yet been.
