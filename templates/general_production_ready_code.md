Here are secure prompt templates designed to guide AI code generation towards production-ready, secure, and maintainable code. These templates emphasize explicit security, compliance, testing, and best-practice instructions to reduce risks and enhance output quality.Secure Prompt Template: General Production-Ready CodeYou are a secure, expert software engineer. Generate production-ready, well-structured code in [language] that meets the following requirements:

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
8. Return code and documentation in [output format], referencing any dependencies or assumptions.Secure Prompt Template: API Endpoint (Example)Create a secure REST API endpoint in [language/framework] that:

- Authenticates requests using JWT with token expiration.
- Authorizes users with role-based access control.
- Validates and sanitizes all input parameters.
- Handles errors gracefully without leaking stack traces.
- Logs access and errors securely, avoiding sensitive data exposure.
- Stores sensitive data encrypted at rest and in transit.
- Includes automated tests verifying security and functionality.
- Uses environment variables for all secrets and configurations.
- Adheres to OWASP API Security Top 10 recommendations.
- Produces OpenAPI 3.0 compliant specification.Secure Prompt Template: Database Access LayerGenerate a database access layer in [language] that:

- Uses parameterized queries or ORM to prevent SQL injection.
- Implements connection pooling and error retries.
- Encrypts sensitive data fields transparently.
- Validates all inputs rigorously before queries.
- Does not expose stack traces or SQL errors externally.
- Supports audit logs for data access and modification.
- Includes unit tests for all operations.
- Uses environment variables for database credentials.
- Follows secure coding standards and avoids deprecated APIs.Secure Prompt Template: Prompt Injection and Abuse MitigationWrite code that is resilient against prompt injection and unauthorized manipulation when using AI-generated components by:

- Validating and sanitizing all external inputs before processing.
- Restricting dynamic code execution or eval usage.
- Implementing strict context isolation and escaping for inputs.
- Logging suspicious input patterns and triggering alerts.
- Enforcing minimum privilege principles in AI-accessible APIs.
- Providing clear error feedback without disclosing internal logic.
- Maintaining audit trails for all AI interactions.Tips for Using These Templates EffectivelyCustomize prompt placeholders (e.g., [language], [framework]) clearly.Combine multiple templates for complex requirements.Use “review and improve” iterative prompts: e.g., “Review the generated code for security flaws and improve it.”Provide specific compliance or organizational policies as additional constraints.Always validate output with static analysis and security tools before deployment.These templates embed explicit instructions that encourage secure, compliant, tested, and maintainable code generation, improving the chances AI outputs meet production standards. If needed, sample prompt executions or prompt engineering best practices can be shared.