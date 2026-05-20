# Repository Instructions

This repository contains a FastAPI backend for family-tree APIs.

## Type Safety
- Treat all Python implementation as strict type-checked code.
- Prefer explicit type annotations for functions, methods, attributes, and module-level constants.
- Avoid `Any` unless there is no practical alternative, and explain the boundary when it is necessary.
- Avoid untyped dictionaries for domain data; use Pydantic models, dataclasses, `TypedDict`, or concrete protocol-based abstractions instead.
- Use precise return types and narrow parameter types for public functions and service methods.
- Keep route handlers, schemas, services, and repositories fully typed end to end.
- Do not add code that would obviously fail under strict mypy or pyright settings.

## FastAPI and Pydantic
- Prefer Pydantic models for request and response contracts.
- Keep endpoint handlers thin and delegate business logic to typed services.
- Use dependency injection with explicit types for auth, settings, database clients, and service objects.
- Define stable response shapes and avoid ad hoc response payloads.

## Implementation Expectations
- Preserve compatibility with existing code unless a breaking change is explicitly requested.
- Add or update tests when behavior changes.
- Favor small, readable, production-oriented changes over generic scaffolding.
