# codapact-ynab

The **YNAB coda**: a typed Python client and `ynab` command-line tool for the
[YNAB API](https://api.ynab.com/), generated from YNAB's OpenAPI contract by
[Codapact](https://github.com/mikejhill/codapact).

Replaces `ynab-api-cli`, which is no longer maintained.

## Install

```console
uv tool install codapact-ynab     # or: pipx install codapact-ynab
ynab --help
```

Requires Python 3.13+.

## Credentials

Create a personal access token under YNAB **Account Settings → Developer Settings**, then either:

```console
ynab auth login        # saves it in the OS keyring
ynab doctor            # checks settings, credentials, and connectivity
```

or set `YNAB_BEARER` in the environment. `YNAB_BEARER_COMMAND` runs a command that prints
the token (for example a password manager).

## Use

```console
ynab plans list
ynab accounts list -o table
ynab transactions list --since-date 2026-01-01 --query 'data.transactions[].payee_name'
ynab describe --brief  # every command, for scripts and agents
```

`--plan-id` defaults to `last-used`. `--dry-run` prints the HTTP request without sending it;
commands that delete ask for confirmation (or `--yes`).

As a library:

```python
from codapact_ynab import Client

client = Client()
```

## How this repository works

| Path | What it is |
| --- | --- |
| `openapi.yaml` | YNAB's contract, pinned (currently API 1.91.0) |
| `codapact.yaml` | Codapact project file: shaping rules and targets |
| `gen/python/` | Generated code and tests. Do not edit; regenerate |
| `pyproject.toml` | Hand-written packaging: PyPI metadata and the release version |

```console
uvx codapact==0.8.0 sync --check   # has YNAB published a new contract?
uvx codapact==0.8.0 sync           # pull it into openapi.yaml
uvx codapact==0.8.0 generate       # regenerate gen/python
uv run pytest                      # offline tests
```

CI fails if `gen/python` differs from what the pinned Codapact produces. Releases are cut by
release-please and published to PyPI through trusted publishing.
