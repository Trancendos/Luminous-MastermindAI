# Secure Prompt Templates Library

## Introduction

This document provides a comprehensive library of secure prompt templates designed to guide AI code generation towards production-ready, secure, and maintainable code. These templates emphasize explicit security, compliance, testing, and best-practice instructions to reduce risks and enhance output quality.

## Template 1: General Production-Ready Code

```
You are a secure, expert software engineer. Generate production-ready, well-structured code in [language] that meets the following requirements:

1. Follow industry best practices for security, including:
   - Validate and sanitize all user inputs against injection attacks.
   - Avoid hardcoded credentials or secrets; use environment variables.
   - Implement proper error handling without exposing internal details.
   - Use secure defaults (e.g., HTTPS, strong encryption, least privilege).

2. Ensure the code complies with relevant standards and regulations (e.g., GDPR, HIPAA).

3. Write modular, maintainable, and well-documented code with clear comments.

4. Include unit and integration tests covering normal and edge cases.

5. Use well-maintained, community-trusted libraries and specify version numbers.

6. Provide logging that is secure and excludes sensitive data.

7. Output code that passes static security analysis as per OWASP guidelines.

8. Return code and documentation in [output format], referencing any dependencies or assumptions.
```

## Template 2: Secure REST API Endpoint

```
Create a secure REST API endpoint in [language/framework] that:

- Authenticates requests using JWT with token expiration.
- Authorizes users with role-based access control.
- Validates and sanitizes all input parameters.
- Handles errors gracefully without leaking stack traces.
- Logs access and errors securely, avoiding sensitive data exposure.
- Stores sensitive data encrypted at rest and in transit.
- Includes automated tests verifying security and functionality.
- Uses environment variables for all secrets and configurations.
- Adheres to OWASP API Security Top 10 recommendations.
- Produces OpenAPI 3.0 compliant specification.
```

## Template 3: Database Access Layer

```
Generate a database access layer in [language] that:

- Uses parameterized queries or ORM to prevent SQL injection.
- Implements connection pooling and error retries.
- Encrypts sensitive data fields transparently.
- Validates all inputs rigorously before queries.
- Does not expose stack traces or SQL errors externally.
- Supports audit logs for data access and modification.
- Includes unit tests for all operations.
- Uses environment variables for database credentials.
- Follows secure coding standards and avoids deprecated APIs.
```

## Template 4: Prompt Injection and Abuse Mitigation

```
Write code that is resilient against prompt injection and unauthorized manipulation when using AI-generated components by:

- Validating and sanitizing all external inputs before processing.
- Restricting dynamic code execution or eval usage.
- Implementing strict context isolation and escaping for inputs.
- Logging suspicious input patterns and triggering alerts.
- Enforcing minimum privilege principles in AI-accessible APIs.
- Providing clear error feedback without disclosing internal logic.
- Maintaining audit trails for all AI interactions.
```

## Template 5: Frontend Security

```
Create a secure frontend application in [framework] that:

- Implements Content Security Policy (CSP) headers.
- Uses HTTPS for all communications.
- Validates and sanitizes all user inputs on the client side.
- Implements proper authentication and session management.
- Protects against Cross-Site Scripting (XSS) attacks.
- Protects against Cross-Site Request Forgery (CSRF) attacks.
- Uses secure storage mechanisms for sensitive data.
- Includes security-focused unit and integration tests.
```

## Template 6: Microservices Architecture

```
Design a secure microservices architecture in [language/framework] that:

- Implements service-to-service authentication and authorization.
- Uses API gateways for centralized security controls.
- Implements rate limiting and throttling.
- Uses circuit breakers for resilience.
- Implements distributed tracing for observability.
- Encrypts all inter-service communications.
- Uses service mesh for advanced security features.
- Includes comprehensive monitoring and alerting.
```

## Template 7: Machine Learning Model Deployment

```
Create a secure machine learning model deployment pipeline that:

- Validates and sanitizes all input data before inference.
- Implements model versioning and rollback capabilities.
- Monitors model performance and drift.
- Implements explainability and interpretability features.
- Protects against adversarial attacks.
- Ensures data privacy and compliance with regulations.
- Implements audit logging for all predictions.
- Includes comprehensive testing for model behavior.
```

## Tips for Effective Use

- **Customize Placeholders**: Clearly specify the language, framework, and output format in the placeholders.
- **Combine Templates**: For complex requirements, combine multiple templates to address different aspects of the system.
- **Iterative Refinement**: Use "review and improve" iterative prompts to refine the generated code.
- **Provide Context**: Include specific compliance or organizational policies as additional constraints.
- **Always Validate**: Always validate the output with static analysis and security tools before deployment.
