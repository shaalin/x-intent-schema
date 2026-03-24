# x-intentops-semantics

JSON Schema for structured operation semantics in OpenAPI extensions.

This repository publishes JSON Schemas for incubating OpenAPI extension patterns. The extension provides machine-readable operation semantics such as operation classification, effects, data sensitivity, and risk levels for API policy and authorization decisions.

## Extension Names

| Extension | Status | Description |
|-----------|--------|-------------|
| `x-intentops-semantics` | **Preferred** | Current recommended extension name |
| `x-intent` | Legacy | Original prototype name (still supported) |

### Migration Note

- Existing users of `x-intent` can continue using it. The schema remains fully supported.
- New implementations should prefer `x-intentops-semantics`.

## Canonical URLs

**Preferred (x-intentops-semantics):**
```
https://shaalin.github.io/x-intent-schema/schemas/x-intentops-semantics/v1/schema.json
```

**Legacy (x-intent):**
```
https://shaalin.github.io/x-intent-schema/schemas/x-intent/v1/schema.json
```

## Key Semantics

- **Effects are declarative.** They describe policy-relevant semantics, not an exhaustive runtime trace.
- **Effects are cumulative and unordered.** The array has no sequence; order carries no meaning.
- **Target is a semantic boundary.** It identifies the resource domain (e.g., `billing.invoice`), not a runtime scope, IAM resource, or specific object ID.

See [docs/semantics.md](docs/semantics.md) for full details.

## Schemas

```
schemas/x-intentops-semantics/v1/schema.json   # Preferred
schemas/x-intent/v1/schema.json                # Legacy
```

## Examples

| File | Description |
|------|-------------|
| [minimal.json](examples/minimal.json) | Simplest valid operation semantics (read, no optional fields) |
| [read-only.json](examples/read-only.json) | Read with data classification |
| [draft-mutate.json](examples/draft-mutate.json) | Multi-effect: read + mutate |
| [external-financial-high-risk.json](examples/external-financial-high-risk.json) | High-risk financial transfer with external call |

### Usage in OpenAPI

```yaml
paths:
  /invoices/{id}:
    get:
      operationId: getInvoice
      x-intentops-semantics:
        ver: "1"
        operation_class: billing.invoice.get
        effects:
          - kind: read
            target: billing.invoice
            data:
              class: confidential
```

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

- [Overview](docs/overview.md) — What this extension is and isn't
- [Semantics](docs/semantics.md) — Field definitions and rules
- [Publishing](docs/publishing.md) — Hosting and versioning guidance

## Validate Examples

```bash
pip install -r requirements.txt
python validate.py
```

## Related

This repo defines only the operation semantics schema. It does not include runtime grants, policy engines, or implementation details.

## License

Apache 2.0
