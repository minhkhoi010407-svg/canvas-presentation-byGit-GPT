# Validate this repository

Run the local validator from the repository root:

```powershell
node .\09-TOOLS\validate-repository\validate.mjs
```

The script uses Node built-ins only. It parses local JSON, checks that the source registry contains exactly the requested 12 unique repositories with valid commit SHAs, verifies each source guide/license and Playwright's notice, checks Lucide's dual-license text, resolves inline local Markdown links, and rejects dependency/cache/build directories and selected sensitive-file patterns. A clean validation checks repository structure, not the correctness of upstream projects or the visual quality of generated presentations.

