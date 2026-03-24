# Operation Semantics Overview

This schema defines structured operation semantics for API policy and authorization.

## Extension Names

- **`x-intentops-semantics`** — Preferred extension name for new implementations
- **`x-intent`** — Original prototype name (legacy, still supported)

## What It Describes

- The stable semantic meaning of an API operation
- Policy-relevant effects of invoking that operation
- Data classification and risk levels for authorization decisions

## Intended Use

Operation semantics metadata is attached to API operations as an OpenAPI extension (`x-intentops-semantics` or `x-intent`). Policy engines consume this metadata to make authorization decisions.

## What It Is Not

- **Not runtime authorization.** This schema describes operations statically; it does not represent runtime decisions, tokens, or grants.
- **Not a workflow trace.** Effects are declarative semantic annotations, not an exhaustive record of what happens at execution time.
- **Not an API specification.** It augments OpenAPI; it does not replace it.
