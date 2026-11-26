---
id: backend-engineering.async.own-task-lifetimes
title: Give Every Background Task a Lifetime Owner
stage: implementation
severity: warn
tech_stack: [backend]
applies_when: starting or detaching backend tasks or changing cancellation, joining, error handling, or shutdown
anti_patterns:
  - id: backend-engineering.async.unowned-work
    name: Start work without an owner after the caller exits
    description: Work keeps using resources or fails after its caller exits without anyone responsible for observing, stopping, or joining it.
    severity: warn
---

## Decision

Name the owner before starting the task: the request, a job, a supervisor, or the process. Decide whether the task stops or continues when that owner finishes, fails, or receives cancellation. If the task must continue, transfer ownership explicitly. Identify who observes errors and who waits for the task to finish before its dependencies close.

## Follow cancellation through shutdown

A cancellation request is not proof that work has stopped. Check the paths through blocked I/O, loops, and cleanup, including how the owner observes completion. On shutdown, stop admitting work, then drain or request cancellation according to policy, join workers, and close dependencies they still use only after they have stopped. Define what happens if the shutdown deadline expires; do not report a clean drain while workers remain active.

- In Python `asyncio`, retain a strong reference to detached tasks until completion and observe their results; the event loop keeps weak references. Python 3.11+ `TaskGroup` awaits its tasks on exit and cancels siblings on a non-cancellation failure. `shield` prevents caller cancellation from propagating through that await to the inner task, but the caller still gets `CancelledError` and the inner task can still be cancelled directly. Arrange cleanup or hand ownership to a supervisor.
- In JavaScript, `void refresh()` does not observe a rejected promise. Attach a rejection handler that handles the failure, or submit the work to a supervisor that observes the result. Check the host's unhandled-rejection policy rather than assuming a request error handler will catch it.
- In Go, a `context.CancelFunc` signals cancellation and does not wait for work to stop. Pass the context to operations that honor it, check cancellation in loops and blocking paths, and join goroutines separately.

## Example and limits

A request shields a worker using its connection and then closes the connection on cancellation. If the worker must stop before cleanup, cancel and join it before closing the connection. A job intended to continue can instead run under a supervisor with its own resources, error handling, and shutdown policy. Neither arrangement makes the task durable across process loss or authorizes it to write stale results.
