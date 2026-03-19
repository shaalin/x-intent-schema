# Publishing the x-intent Schema

This document describes how to publish the x-intent schema at a stable URL.

## Schema URL Strategy

The schema `$id` should be a stable, resolvable URL that remains consistent across versions:

```
https://{your-domain}/schemas/x-intent/v1/schema.json
```

### Placeholder Domain

This repo uses `example.org` as a placeholder. Before publishing:

1. Choose your domain (e.g., `x-intent.dev`, `schemas.yourorg.com`)
2. Update the `$id` in `schemas/x-intent/v1/schema.json`
3. Update any documentation references

## Versioned Paths

Use versioned paths to allow breaking changes in future schema versions:

```
/schemas/x-intent/v1/schema.json   # Current stable
/schemas/x-intent/v2/schema.json   # Future breaking changes
```

The `ver` field inside documents indicates which schema version they target. Consumers can validate against the correct schema based on this field.

## Publishing via GitHub Pages

To serve the schema directly from this repo:

1. Enable GitHub Pages in repo settings (source: `main` branch, root `/`)
2. The schema will be available at:
   ```
   https://{org}.github.io/{repo}/schemas/x-intent/v1/schema.json
   ```
3. Optionally configure a custom domain for cleaner URLs

### Custom Domain Setup

1. Add a `CNAME` file to the repo root with your domain
2. Configure DNS to point to GitHub Pages
3. Update the schema `$id` to match the custom domain

## Validation

Consumers can validate x-intent documents by fetching the schema from the published URL:

```bash
# Fetch schema and validate locally
curl -O https://your-domain/schemas/x-intent/v1/schema.json
python validate.py
```

## Best Practices

1. **Keep URLs stable.** Once published, avoid changing the schema URL for a given version.
2. **Version for breaking changes.** Use `/v2/` paths for incompatible schema changes.
3. **Document the canonical URL.** Reference the published `$id` in integration guides.
