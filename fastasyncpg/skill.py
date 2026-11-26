r"""Use fastasyncpg's API idiomatically. Always read before using the lib.

Examples: `nbs/00_core.ipynb`; `doc(fastasyncpg.core)` and table methods before use.

- lifecycle: module-global `db = Database()`; `await db.connect(...)` creates one pool per event loop; `await db.close()` closes that loop's pool
- tables: `t = db.t.user` (cached `Table`); schema metadata `t.cols`, `t.pks`; `await t(where, args)` returns list, not lazy query
- by pk (first pk col): `await t[pk]` returns row or raises `NotFoundError`; `await t.get(pk)` returns row or `None`
- single row: `await t.one(where, args)` and `await db.one(sql, ...)` return one row (0: `NotFoundError`, >1: `ValueError`); `one_or_none` returns row or `None` (>1: `ValueError`); prefer over `first(await ...)`
- scalars and predicates: `await db.scalar_one(sql, ...)` returns single field of single row; `await t.exists(where, args)` and `await db.exists(sql, ...)` return `bool` (`SELECT EXISTS`); `await t.count` (async prop) and `await t.count_where(where, args)` return counts
- permissive single: `await db.fetchrow(sql, ...)` returns first row or `None`; `await db.fetchval(sql, ...)` returns first value or `None` (`column=`, `timeout=`)
- placeholders: `?`, `:name` (kwargs), or `$1` on `db.{q,one,one_or_none,scalar_one,exists,fetchrow,fetchval}` and table helpers (`where_args` positional, incl. `count_where`, `exists`); other delegated `asyncpg` methods (`fetch`, `execute`, ...) require `$1`; `order_by` is SQL (`'name DESC'`, not `'-name'`)
- identifiers: interpolate `t` and `t.c.name` for quoted identifiers; parameterize values
- dataclasses: `t.dataclass()` binds future reads; `UNSET` omitted on writes, `None` writes NULL; single-row writes return rows, bulk `inserts`/`updates`/`upserts` return `None` with missing columns as NULL
- transactions: `async with db.transaction()` joins all helpers via task-local context (no handle passing); nested = savepoints; spawn background tasks outside transaction/acquire blocks
- xtra: `t.xtra(...)` mutates shared cached `Table`, `t.xtra()` clears; never use for request-local filters in concurrent code
- upsert: updates supplied fields on pk conflict, not get-or-create
- queues: `claim` requires transaction; `claim_one` manages status and catches handler exceptions (check `result.failed`)
- listen: `await listen(channel, on_notify, *, on_connect=None, on_disconnect=None, retry=1, **kwargs)` holds dedicated `asyncpg` conn with auto-reconnect, sync or async callbacks, handler errors logged, `on_connect(reconnected)` after `add_listener`
"""
