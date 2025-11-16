# Centrous-Core: Microservice Architecture Templates

**Version**: 1.0  
**Last Updated**: November 2025  

---

## 1. Overview

This document provides standardized templates for creating new microservices within the Centrous-Core hub. These templates ensure that all services are built with a consistent structure, adhere to The Foundation principles, and can be seamlessly integrated into the Infinity-Trancendos Ecosphere.

## 2. Standard Microservice Template

This is the base template for all new microservices. It follows the Hexagonal Architecture (Ports and Adapters) pattern.

### 2.1 Directory Structure

```
/service-name
|-- /src
|   |-- /core
|   |   |-- /domain
|   |   |   |-- models.py
|   |   |   `-- services.py
|   |   `-- ports.py
|   |-- /adapters
|   |   |-- /api
|   |   |   |-- routes.py
|   |   |   `-- schemas.py
|   |   |-- /db
|   |   |   |-- models.py
|   |   |   `-- repositories.py
|   |   `-- /messaging
|   |       `-- publishers.py
|   `-- main.py
|-- /tests
|-- Dockerfile
|-- pyproject.toml
`-- README.md
```

### 2.2 Component Descriptions

- **`src/core/domain`**: Contains the core business logic and domain models. This code is completely independent of any external frameworks.
- **`src/core/ports.py`**: Defines the interfaces for interacting with the core logic (driving and driven ports).
- **`src/adapters`**: Implements the ports and connects them to specific technologies.
- **`src/adapters/api`**: Implements the driving API port (e.g., using FastAPI).
- **`src/adapters/db`**: Implements the driven database port (e.g., using SQLAlchemy).
- **`src/adapters/messaging`**: Implements the driven messaging port (e.g., using Pika for RabbitMQ).
- **`main.py`**: The entry point of the application, responsible for wiring together the adapters and the core.

## 3. API Specification Template

All APIs must be documented using the OpenAPI 3.0 specification.

```yaml
openapi: 3.0.0
info:
  title: "Service Name API"
  version: "1.0.0"
  description: "Description of the service."
paths:
  /resource:
    get:
      summary: "Get a list of resources."
      responses:
        '200':
          description: "A list of resources."
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Resource'
components:
  schemas:
    Resource:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
```

## 4. Shared Service Libraries

Centrous-Core provides a set of shared libraries to avoid code duplication and ensure consistency across services.

### 4.1 `trancendos-logging`

A standardized logging library that provides structured JSON logging and integration with the central logging service.

### 4.2 `trancendos-auth`

A library for handling authentication and authorization, including JWT validation and RBAC.

### 4.3 `trancendos-db`

Provides common database utilities, such as connection pooling and base repository classes.

## 5. Integration Patterns

### 5.1 Synchronous Communication

For synchronous requests, services should communicate via REST APIs through the API Gateway.

### 5.2 Asynchronous Communication

For asynchronous communication, services should use a message broker (e.g., RabbitMQ) and follow the publish/subscribe pattern.

---

By using these templates and shared libraries, developers can quickly create new microservices that are consistent, maintainable, and fully integrated into the Trancendos ecosystem.
