# Contributing

Thanks for helping this knowledge base evolve. Contributions of all sizes are welcome:
a sharper trigger, a better reply option, a new topic, a translation fix, a tool improvement.

## Quick start

1. **Fork** the repo, then clone your fork.
2. Create a branch: `git checkout -b feat/short-description`.
3. Make a focused change — one concern per pull request.
4. Run the health check (below) until green.
5. Commit with a **Conventional Commit** message.
6. Push and open a Pull Request describing **what** and **why**.

## Health check (must be green)

```bash
bash tools/check.sh
```

It runs: lint (structure, entry floors, sources) → recall smoke test → resolver end-to-end →
freshness. All must pass. If you changed any `triggers`, add a recall case to
`qa/router-smoke.py` for the phrasing you fixed.

## Adding or improving a topic

Follow the schema in `AGENTS.md`; the full procedure is in
`wiki/synthesis/updating-the-kb.md`. In short:

- A topic folder `wiki/<cluster>/<id>/` needs `core.md`, `zh.md`, `en.md`, `ms.md`.
- The three lanes are **authored natively, not translated** (each carries the lane header).
- Every wiki file ends with `## Sources` citing ≥ 3 URLs.
- Register the topic in `router.json` via a `router-patch.json`, then run
  `python3 tools/lint_kb.py reindex` and `python3 tools/build_router_index.py`.

> This public repo omits `raw/` (licensed third-party captures). Cite source URLs directly in
> `## Sources`; note that lint skips the raw-capture check here.

## Commit style

Conventional Commits: `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`.

## Security

- **Never commit secrets.** Run the leak-guard before committing if you add tooling.
- Report security issues **privately** to the maintainer — do not open a public issue.

## License

By contributing, you agree your work is licensed under this repository's MIT `LICENSE`.
