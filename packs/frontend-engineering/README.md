# Frontend Engineering

Two framework-independent Practices for designing and reviewing web, desktop, and terminal interfaces:

| Decision | Practice |
|---|---|
| An async completion may outlive an input, operation, or view | [Let Only the Current Operation Update UI State](./practices/async/preserve-result-ownership.md) |
| An interaction changes what must finish before users see a result | [Bound the Work Users Wait For](./practices/performance/bound-interaction-work.md) |

Use this Pack alongside `code-review` when reviewing UI changes. Use `react-web-craft` when the decision depends on React. Neither Pack is required to use these Practices. This is not a complete UI guide; keyboard, focus, and other interaction requirements still come from the application and platform.

See [Sources and synthesis](./SOURCES.md) for the platform and library contracts behind the Practices.
