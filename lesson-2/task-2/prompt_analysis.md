# Prompt Analysis

## Existing Problems

### Performance Issues

* Dynamic values are included in every request.
* Leave policies are repeatedly injected into the prompt.
* Poor cache utilization increases latency and token usage.

### Security Issues

* Employee password is exposed inside the prompt.
* Users may attempt prompt injection attacks.
* Sensitive information should never be accessible to the language model.

### Maintainability Issues

* Static instructions and dynamic employee information are mixed together.
* Difficult to update company policies independently.
