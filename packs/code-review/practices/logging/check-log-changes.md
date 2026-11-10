---
id: code-review.logging.check-log-changes
title: Check What the Logs Reveal and What They Hide
stage: review
severity: warn
tech_stack: [code-review]
applies_when: a diff adds, removes, changes, or changes the handling of logs, error events, audit records, or logged request and response fields
anti_patterns:
  - id: code-review.logging.log-leaks-or-hides-the-failure
    name: Logs expose secrets or hide what failed
    description: A changed log exposes sensitive data or removes information required to investigate a real failure.
    severity: warn
---

## When to apply

A change writes a log or alters an existing error, audit, or diagnostic event. Check what operators and log readers will actually see when the affected path runs.

## Guidance

Trace the values into the log and where the log goes. Could it contain a credential, personal data, a prompt, or another value the project must not record? Check redaction at the actual sink, including structured fields and exception text, before reporting a leak.

Then follow the failure path. If the code catches an error, can operators still tell what operation failed and why when the project's diagnostics or audit requirements need that information? Check the actual log level, filters, sampling, request identifiers, and whether an upstream handler already records the error. Don't log the same exception at every layer just to increase volume.

Watch for changes that:

- Log an entire request, response, header map, or exception whose contents can include secrets; a safe field name does not make its value safe.
- Replace a useful error with a success message or discard an error before the only operator-visible record is written.
- Put required diagnostic or audit events behind a disabled level, sampling rule, or filter, or remove a required correlation identifier.
- Construct expensive log payloads on a hot path even when the selected level is disabled, or log unbounded payloads repeatedly.
- Log a success before the operation can still fail, making an incomplete operation appear complete to the people who rely on that event.

Report the reachable input or failure, the log sink and existing protections, and the concrete exposure or operational consequence. If logs are merely slow or unavailable and affect the primary request, also consider the separate side-effect Practice. Stop when the changed log and its consumers are accounted for.

## Anti-pattern

An HTTP handler logs the whole incoming header map to help diagnose an upstream failure. The production log stream is available to support staff, while the headers can include a bearer token. Unless the logger removes that field before storage, the change puts a credential in a broader-access system.

## Why

Logs are often read by people and systems other than the original caller. They need enough accurate information to diagnose a failure without exposing data those readers should not have.

## Exceptions and boundaries

Do not assume every error needs a new log, that logging an identifier is always unsafe, or that missing correlation is a bug without an actual requirement or operational consequence. An upstream handler, logger redaction, or restricted sink may already provide the needed protection; verify it. Audit records can be mandatory and durable even when ordinary diagnostic logs are best effort. Don't report logging style or level preferences as defects without a concrete effect.

## Example

A changed job runner catches a failed upload and returns a generic failure. Its only error log was removed; the deployment contract requires operators to know which upload failed, and no caller logs the error. Reporting the lost diagnostic is justified. If the caller already logs the job ID and underlying error at a retained level, removing the duplicate local log is not by itself a defect.
