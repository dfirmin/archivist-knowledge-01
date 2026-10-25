# Scripts

Scripts bring documents in or keep documents up to date, on GitHub Actions. Each script is a folder
here with two files. Scripts created in the knodex app and scripts an engineer adds here by hand
look the same, and both show up in the app.

```
scripts/<name>/
  script.yaml   what it is, when it runs, its inputs and the secrets it needs
  main.py       the code; `import knodex` for the helpers
```

**Two kinds**

- `connector` brings documents in: `knodex.inbox.add(name, text)`. They're dropped in
  `sources/inbox/` and the Engine processes them.
- `updater` edits documents directly and deterministically: `knodex.docs.find(type=..., where=...)`,
  then `doc.set_field`, `doc.replace_section` or `doc.replace_table`, then `doc.save(note=...)`. Every
  change goes into one pull request for review, and only the changed lines show.

A connector may only add files to `sources/inbox/`, and an updater may only change Markdown under
`knowledge/`. Anything else a script touches is undone and reported.

**script.yaml**

```yaml
name: PokéAPI base stats
description: What it does, in a sentence or two.
kind: updater                 # connector | updater
schedule: "0 6 * * 1"         # optional, UTC cron; checked hourly
inputs:                       # shown as fields when it's run from the app
  region: {description: Only this region, default: kanto}
secrets: [SOME_API_KEY]       # repository secrets it reads with knodex.secret("SOME_API_KEY")
requirements: [requests==2.32.3]
```

**Running one**

From the app (Build → Scripts → Run), from the Actions tab (knodex-scripts → Run workflow), or on
its schedule. Locally: `KNODEX_INPUTS='{"region": "kanto"}' PYTHONPATH=<knodex>/engine/scripts python scripts/<name>/main.py`.
