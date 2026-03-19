# x-intent Semantics

## operation_class

A stable semantic identifier for the API action. Use dot-separated naming:

```
billing.invoice.get_status
comms.email.create_draft_refund_notice
billing.refund.create_payout
```

## effects

Declarative, policy-relevant semantic effects of invoking this operation.

- **Cumulative and unordered.** The array represents all declared effects; order has no meaning.
- **Not an execution trace.** Effects describe semantic intent, not an exhaustive log of runtime behavior.

## effect.kind

Generic categories that apply across domains:

| Kind | Meaning |
|------|---------|
| `read` | Retrieves data |
| `mutate` | Creates or updates a resource |
| `delete` | Removes a resource |
| `notify` | Sends a notification |
| `external_call` | Invokes an external service |
| `financial_transfer` | Moves money |
| `provision` | Allocates infrastructure or capacity |
| `compute` | Executes significant computation |

Kinds are intentionally generic so policies can reason about effect categories without enumerating every possible operation.

## effect.target

The affected resource domain, subsystem, or external service in deployment-stable form.

- Use stable identifiers like `billing.invoice`, `payment.processor`, `crm.customer`
- **Not per-request instance IDs.** Target identifies the resource *type* or *domain*, not a specific record.

## Optional Fields

### effect.risk

Classifies potential impact: `low`, `medium`, `high`.

Useful for policies that enforce risk ceilings or require approval for high-risk operations.

### effect.data

Describes data sensitivity:

- `data.class`: `public`, `internal`, `confidential`, `restricted`
- `data.pii`: boolean

Useful for policies that restrict access to sensitive or PII data.
