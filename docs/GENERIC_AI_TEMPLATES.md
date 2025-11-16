"""
# NanoLeaf: Generic AI Generation Templates

**Version**: 1.0  
**Last Updated**: November 2025  

---

## 1. Overview

This document provides a collection of generic AI generation templates for use within the NanoLeaf repository. These templates are designed to be adaptable to a wide range of tasks and can be used as a starting point for creating more specific prompts.

## 2. Base Template

This is the fundamental template that should be used for all AI generation tasks. It includes the Framework Linking Code (FLC) and placeholders for the task-specific details.

```
[FLC PREAMBLE - NON-NEGOTIABLE]
You are operating within the Trancendos ecosystem.
You MUST adhere to:
- 0-Cost Mandate: Only suggest free/open-source solutions
- Security-First: Apply zero-trust principles
- Modular Design: Ensure swappability
[END FLC PREAMBLE]

**Your task is to:** [Specific, measurable objective]

**Context:** [Relevant background information]

**Constraints:** [Specific limitations or requirements]

**Expected Output:** [Format and structure of the desired output]
```

## 3. Code Generation Template

This template is designed for generating code in various programming languages.

```
[FLC PREAMBLE - NON-NEGOTIABLE]
...
[END FLC PREAMBLE]

**Your task is to:** Write a Python function that [specific functionality].

**Context:** The function will be part of a microservice that [service description]. It should be stateless and handle errors gracefully.

**Constraints:**
- Language: Python 3.11+
- Style: PEP 8 compliant, formatted with Black
- Dependencies: Only use libraries from the approved allowlist.
- Security: Sanitize all inputs and use parameterized queries.

**Expected Output:**
- A single Python file containing the function.
- Google-style docstrings explaining the function's purpose, arguments, and return value.
- A set of pytest unit tests with at least 80% coverage.
```

## 4. Documentation Generation Template

This template is for generating technical documentation.

```
[FLC PREAMBLE - NON-NEGOTIABLE]
...
[END FLC PREAMBLE]

**Your task is to:** Write the README.md file for a new microservice called "OrderService".

**Context:** The OrderService is responsible for managing customer orders. It has a REST API with endpoints for creating, retrieving, and updating orders.

**Constraints:**
- Format: Markdown
- Sections to include: Project Overview, Features, API Endpoints, Setup Instructions, Usage.

**Expected Output:**
- A single Markdown file containing the complete README.
```

---

These generic templates provide a solid foundation for creating more specific and powerful AI generation prompts within the NanoLeaf repository.
"""
