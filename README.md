# x-intent

Operation-level semantic metadata schema for API authorization.

## Schema

```
schemas/x-intent/v1/schema.json
```

## Examples

```
examples/minimal.json
examples/read-only.json
examples/draft-mutate.json
examples/external-financial-high-risk.json
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

## Validate Examples

```bash
pip install -r requirements.txt
python validate.py
```

## Related

This repo defines only the x-intent schema. It does not include runtime grants, policy engines, or implementation details.

## License

Apache 2.0
