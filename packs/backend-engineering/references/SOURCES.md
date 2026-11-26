# Sources and synthesis

The Practices are independently written synthesis under the Pack's CC-BY-4.0 license. No upstream code, examples, or prose were copied. Moving product documentation was consulted on 2026-11-18; a versioned reference documents that version, not a project's installed version or configuration.

## `backend-engineering.async.own-task-lifetimes`

- [Python 3.14 `asyncio` tasks](https://docs.python.org/3.14/library/asyncio-task.html): weak references for detached tasks, `TaskGroup` waits at exit and cancels siblings on non-cancellation failure (`TaskGroup` introduced in 3.11), and `shield` separates caller cancellation from inner cancellation. Check the deployed Python minor and whether the task cooperates with cancellation; a shield does not ensure completion or durability.
- [Go 1.25.0 `context` source](https://github.com/golang/go/blob/go1.25.0/src/context/context.go): `CancelFunc` asks work to stop and does not wait; `Done` is how cooperating code detects cancellation. This is not evidence that any particular dependency honors a context.
- [ECMAScript 2025 promise rejection tracking](https://tc39.es/ecma262/2025/multipage/executable-code-and-execution-contexts.html#sec-host-promise-rejection-tracker) and [Node.js 24.x `process` documentation](https://nodejs.org/docs/latest-v24.x/api/process.html#event-unhandledrejection): discarding a promise result is not observing rejection; handling an unobserved rejection depends on host policy and runtime settings. The shutdown sequence is design guidance, not a framework guarantee.

## `backend-engineering.concurrency.justify-locks-and-gates`

- [PostgreSQL 18 explicit locking](https://www.postgresql.org/docs/18/explicit-locking.html#LOCKING-ROWS), [`SELECT` locking clause](https://www.postgresql.org/docs/18/sql-select.html#SQL-FOR-UPDATE-SHARE), and [transaction isolation](https://www.postgresql.org/docs/18/transaction-iso.html): transaction lifetime bounds row-lock protection; rollback to a savepoint can release locks acquired after it. Lock targets depend on the emitted query, including `OF` in joins, and concurrency behavior depends on isolation. None of these establish gap/range locking in another engine or protection for a later independent write.
- [Redis distributed locks](https://redis.io/docs/latest/develop/clients/patterns/distributed-locks/): a lease expires, release must check ownership, and stale work may need fencing enforced by the protected resource. The guidance is not an endorsement of a specific lock algorithm or proof of guarantees under any Redis topology.

## `backend-engineering.delivery.align-effects-and-acknowledgements`

- [AWS transactional outbox guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html): atomically record the business write and the outbox event; relay delivery can repeat. The external-call/inbox crash windows are independent reasoning, not a provider guarantee of exactly-once effects.
- [Apache Kafka 4.1 Java `KafkaConsumer`](https://kafka.apache.org/41/javadoc/org/apache/kafka/clients/consumer/KafkaConsumer.html): consumed position and committed position differ; automatic commits, batches from `poll`, and group rebalancing matter when processing and committing offsets. Inspect the actual client, broker, group protocol, and settings; the Java API reference does not establish semantics of other clients.
- [Amazon SQS visibility timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html): a message can reappear if not deleted by the end of visibility, and Standard queues do not guarantee exclusive delivery within visibility. Extending visibility does not reset its documented 12-hour maximum from receipt. Check Standard versus FIFO and the actual receive, extension, and delete settings; visibility is not business-effect deduplication.

## `backend-engineering.llm.account-for-each-attempt`

- [OpenAI Chat Completions create](https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create), cross-checked against the [OpenAI Python generated Chat Completions request type](https://github.com/openai/openai-python/blob/main/src/openai/types/chat/chat_completion_stream_options_param.py): `stream_options.include_usage` requests an extra pre-`[DONE]` chunk that may not arrive on interruption. The type is from the moving `main` branch, not a released SDK pin; only this endpoint is covered, not Responses or third-party compatible endpoints.
- [Anthropic Messages streaming](https://platform.claude.com/docs/en/build-with-claude/streaming#event-types): `message_delta.usage` counts are cumulative. [Server-side fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#server-side-fallback) is separately documented under beta header `server-side-fallback-2026-07-01`; confirm scope at model boundaries rather than assuming one request maps to one model or assuming a particular SDK aggregates the events correctly. Claims concern the native Messages wire protocol, not an SDK release or hosted variant.
- Attempt identity, settlement, estimates and reconciliation are design guidance. No live provider calls, SDK behavior, pricing, currencies, invoices, or account-specific billing terms were verified. The availability and authority of usage or reconciliation records depend on the actual contract.

## `backend-engineering.side-effects.isolate-optional-work`

- [ECMAScript 2025 `Promise.all`](https://tc39.es/ecma262/2025/multipage/control-abstraction-objects.html#sec-promise.all): rejection of an input rejects the aggregate without a step to cancel remaining inputs. Cancellation and deadlines are separate mechanisms. The queue, exporter, and framework advice calls for inspecting configuration and guarantees; it asserts no product-specific defaults or delivery guarantees.

## `backend-engineering.state.guard-current-generation-writes`

- [PostgreSQL 18 `UPDATE`](https://www.postgresql.org/docs/18/sql-update.html) and [transaction isolation](https://www.postgresql.org/docs/18/transaction-iso.html): conditional writes and their results are database-specific. Zero updated rows is not a PostgreSQL error, and a `BEFORE UPDATE` trigger can suppress matching rows. At Read Committed a concurrent update can cause the condition to be evaluated again on the new row version. Check the actual database, isolation level, driver, and triggers before interpreting a row count. Non-reused incarnation identity and atomic multi-field transitions are design guidance.
