# NB: this file is designed for an LLM reader, not a human. Add it to your LLM's context and ask it to explain.
r"""Use fastasyncpg's async table helpers and SQL API.

Read `nbs/00_core.ipynb` for executable examples. Inspect `doc(fastasyncpg.core)` and bound table methods before use.

- module-global `db = Database()`; `await db.connect(...)` at startup creates a pool per event loop. `await db.close()` closes that loop's pool.
- `t = db.t.user`: cached Table; `t.cols`, `t.pks` are schema metadata. `await t(where, args)` returns a list, not a lazy query.
- `await t[pk]`: row or `NotFoundError`; `await t.get(pk)`: row or `None`. These use the first primary-key column.
- `await t.selectone(where, args)` / `await db.qone(sql, ...)`: exactly one row; zero -> `NotFoundError`, multiple -> `ValueError`. Prefer these over `first(await ...)`.
- `await db.item(sql, ...)`: exactly one row and field. `await t.count`: async property.
- `db.q`: `$1`, `?`, or `:name` placeholders; named values as kwargs. Delegated asyncpg methods (`fetch`, `execute`, etc.) and `count_where` require `$1`. Table `where_args` are positional values. `order_by` is SQL, e.g. `'name DESC'`, not `'-name'`.
- interpolate `t` and `t.c.name` for quoted identifiers; parameterize values
- `t.dataclass()` binds future reads to that class. Dataclass `UNSET` fields are omitted on writes; `None` writes NULL. Single-row writes return rows; `inserts`/`updates`/`upserts` return `None`. Missing bulk columns become NULL.
- `async with db.transaction()`: all helpers join through task-local context; no connection/session passing. Nested transactions are savepoints. Spawn background tasks outside transaction/acquire blocks.
- `t.xtra(...)` mutates the shared cached Table; `t.xtra()` clears it. Never use for request-local filters in concurrent code.
- `upsert` updates supplied fields on primary-key conflict; it is not get-or-create
- `claim` requires a transaction. `claim_one` manages status and catches processing exceptions; inspect its result's `failed` field.
"""
