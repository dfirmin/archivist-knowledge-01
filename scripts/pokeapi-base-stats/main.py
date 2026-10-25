"""Update each Pokémon's Base Stats table from PokéAPI (https://pokeapi.co), deterministically."""
import time

import requests

import knodex

ORDER = [("hp", "HP"), ("attack", "Attack"), ("defense", "Defense"),
         ("special-attack", "Sp. Atk"), ("special-defense", "Sp. Def"), ("speed", "Speed")]

region = knodex.inputs.get("region")
limit = int(knodex.inputs.get("limit", "0") or 0)
checked = updated = 0
for doc in knodex.docs.find(type="Pokemon", where={"okfx_region": region} if region else None):
    number = doc.frontmatter.get("okfx_dex_number")
    if not number or doc.section("Base Stats") is None:
        continue
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{int(number)}", timeout=30)
    if r.status_code == 404:
        knodex.log(f"{doc.rel}: PokéAPI has no Pokémon #{number}")
        continue
    r.raise_for_status()
    stats = {s["stat"]["name"]: s["base_stat"] for s in r.json()["stats"]}
    rows = [[label, stats[key]] for key, label in ORDER]
    rows.append(["**Total**", f"**{sum(stats[k] for k, _ in ORDER)}**"])
    doc.replace_table("Base Stats", ["Stat", "Base"], rows)
    if doc.save(note=f"base stats from PokéAPI #{number}"):
        updated += 1
    checked += 1
    if limit and checked >= limit:
        break
    time.sleep(0.2)   # PokéAPI asks for light use
knodex.log(f"Checked {checked} Pokémon, updated {updated}.")
