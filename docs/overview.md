# x-intent Overview

**x-intent** is an operation-level semantic metadata schema.

## What It Describes

- The stable semantic meaning of an API operation
- Policy-relevant effects of invoking that operation
- Data classification and risk levels for authorization decisions

## Intended Use

x-intent metadata is attached to API operations—for example, as an OpenAPI extension (`x-intent`). Policy engines consume this metadata to make authorization decisions.

## What It Is Not

- **Not runtime authorization.** x-intent describes operations statically; it does not represent runtime decisions, tokens, or grants.
- **Not a workflow trace.** Effects are declarative semantic annotations, not an exhaustive record of what happens at execution time.
- **Not an API specification.** It augments OpenAPI; it does not replace it.
