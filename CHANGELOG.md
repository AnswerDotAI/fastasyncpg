# .giRelease notes

<!-- do not remove -->

## 0.0.10

### Bugs Squashed

- Preserve `claim_one` status update when transaction aborts ([#14](https://github.com/AnswerDotAI/fastasyncpg/pull/14)), thanks to [@kafkasl](https://github.com/kafkasl)


## 0.0.9

### New Features

- Add audit events ([#12](https://github.com/AnswerDotAI/fastasyncpg/issues/12))

### Bugs Squashed

- Revert `claim_one` to yield before return ([#13](https://github.com/AnswerDotAI/fastasyncpg/pull/13)), thanks to [@curtis-allan](https://github.com/curtis-allan)


## 0.0.8

### Bugs Squashed

- p.evt check above yield in `claim_one` ([#11](https://github.com/AnswerDotAI/fastasyncpg/issues/11))


## 0.0.7

### New Features

- Add `Table.claim`/`claim_one` for `SELECT ... FOR UPDATE SKIP LOCKED` queue workers ([#10](https://github.com/AnswerDotAI/fastasyncpg/issues/10))


## 0.0.6

### New Features

- Add `Database.qone` method and refactor `item` to use it ([#9](https://github.com/AnswerDotAI/fastasyncpg/issues/9))


## 0.0.5

### New Features

- Add upserts, groupby methods; switch inserts/updates to executemany ([#8](https://github.com/AnswerDotAI/fastasyncpg/issues/8))


## 0.0.4

### New Features

- Add bulk inserts/updates methods with batched VALUES clauses ([#7](https://github.com/AnswerDotAI/fastasyncpg/issues/7))
- Add acquire/transaction context managers and `from_meta` for connection-scoped Database usage ([#6](https://github.com/AnswerDotAI/fastasyncpg/issues/6))


## 0.0.3

### New Features

- extract `create_from_schema` from create for raw SQL table creation ([#4](https://github.com/AnswerDotAI/fastasyncpg/issues/4))


## 0.0.2

### New Features

- Add named :param placeholders and attach `_db` to dataclass results ([#3](https://github.com/AnswerDotAI/fastasyncpg/issues/3))


## 0.0.1

### New Features

- Add ? placeholder support using sqlparse ([#2](https://github.com/AnswerDotAI/fastasyncpg/issues/2))
- Add `.count` and `.delete_where` to the Table class ([#1](https://github.com/AnswerDotAI/fastasyncpg/pull/1)), thanks to [@ncoop57](https://github.com/ncoop57)

