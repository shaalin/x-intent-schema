# x-intent

Operation-level semantic metadata schema for API authorization.

## Canonical URL

```
https://shaalin.github.io/x-intent-schema/schemas/x-intent/v1/schema.json
```

## Key Semantics

- **Effects are declarative.** They describe policy-relevant intent, not an exhaustive runtime trace.
- **Effects are cumulative and unordered.** The array has no sequence; order carries no meaning.
- **Target is a semantic boundary.** It identifies the resource domain (e.g., `billing.invoice`), not a runtime scope, IAM resource, or specific object ID.

See [docs/semantics.md](docs/semantics.md) for full details.

## Schema

```
schemas/x-intent/v1/schema.json
```

## Examples

| File | Description |
|------|-------------|
| [minimal.json](examples/minimal.json) | Simplest valid intent (read, no optional fields) |
| [read-only.json](examples/read-only.json) | Read with data classification |
| [draft-mutate.json](examples/draft-mutate.json) | Multi-effect: read + mutate |
| [external-financial-high-risk.json](examples/external-financial-high-risk.json) | High-risk financial transfer with external call |

## Fields

| Field | Required | Description |
|-------|----------|-------------|
| `ver` | yes | Schema version (`"1"`) |
| `operation_class` | yes | Stable semantic identifier for the operation |
| `effects` | yes | Declarative policy-relevant effects (array) |
| `effects[].kind` | yes | Effect category (read, mutate, delete, etc.) |
| `effects[].target` | no | Affected domain/subsystem |
| `effects[].risk` | no | Risk level (low, medium, high) |
| `effects[].data.class` | no | Data classification |
| `effects[].data.pii` | no | PII indicator |

## Documentation

- [Overview](docs/overview.md) — What x-intent is and isn't
- [Semantics](docs/semantics.md) — Field definitions and rules
- [Publishing](docs/publishing.md) — Hosting and versioning guidance

## Validate Examples

```bash
pip install -r requirements.txt
python validate.py
```

## Related

This repo defines only the x-intent schema. It does not include runtime grants, policy engines, or implementation details.

## License

Apache 2.0
