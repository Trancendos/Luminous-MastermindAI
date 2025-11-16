# AI Orchestration Platform - API Specification

## Overview

The API is built using tRPC for type-safe, end-to-end TypeScript APIs with automatic client generation.

**Base URL**: `https://api.ai-orchestration.app/trpc`
**Authentication**: JWT Bearer tokens
**Rate Limiting**: 100 requests/minute (free tier), 1000 requests/minute (pro tier)

## Authentication

### POST /auth/register
Register a new user account.

**Request**:
```json
{
  "email": "user@example.com",
  "name": "John Doe",
  "password": "securePassword123"
}
```

**Response**:
```json
{
  "user": {
    "id": "uuid",
    "email": "user@example.com",
    "name": "John Doe",
    "role": "user",
    "subscriptionTier": "free"
  },
  "token": "jwt_token_here"
}
```

### POST /auth/login
Authenticate and receive JWT token.

**Request**:
```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

**Response**:
```json
{
  "user": { /* user object */ },
  "token": "jwt_token_here"
}
```

## AI Integrations

### GET /integrations.list
List all AI integrations for the authenticated user.

**Response**:
```json
{
  "integrations": [
    {
      "id": "uuid",
      "platform": "openai",
      "name": "My OpenAI Account",
      "status": "connected",
      "lastSyncAt": "2024-11-16T00:00:00Z",
      "usageStats": {
        "tokensUsed": 150000,
        "requestsMade": 450,
        "totalCost": 2.50
      }
    }
  ]
}
```

### POST /integrations.create
Add a new AI integration.

**Request**:
```json
{
  "platform": "openai",
  "name": "My OpenAI Account",
  "credentials": {
    "apiKey": "sk-..."
  },
  "config": {
    "defaultModel": "gpt-4o",
    "maxTokens": 4000
  }
}
```

**Response**:
```json
{
  "integration": { /* integration object */ }
}
```

### POST /integrations.test
Test connection to an AI integration.

**Request**:
```json
{
  "integrationId": "uuid"
}
```

**Response**:
```json
{
  "success": true,
  "message": "Connection successful",
  "latency": 245
}
```

### PUT /integrations.update
Update AI integration configuration.

**Request**:
```json
{
  "integrationId": "uuid",
  "name": "Updated Name",
  "config": { /* updated config */ }
}
```

### DELETE /integrations.delete
Remove an AI integration.

**Request**:
```json
{
  "integrationId": "uuid"
}
```

## Terminology Dictionary

### GET /terminology.list
List all terminology entries with optional filtering.

**Query Parameters**:
- `context`: Filter by context (technical, business, personal)
- `search`: Search term
- `limit`: Number of results (default: 50)
- `offset`: Pagination offset

**Response**:
```json
{
  "entries": [
    {
      "id": "uuid",
      "term": "Omni-Bridge",
      "definition": "Governance and compliance intelligence platform",
      "context": "technical",
      "usageExamples": ["Example sentence 1", "Example sentence 2"],
      "frequency": 42,
      "lastUsedAt": "2024-11-16T00:00:00Z",
      "tags": ["compliance", "governance"]
    }
  ],
  "total": 150
}
```

### POST /terminology.create
Add a new terminology entry.

**Request**:
```json
{
  "term": "AI Orchestration",
  "definition": "Managing multiple AI agents in coordination",
  "context": "technical",
  "usageExamples": ["I use AI orchestration to manage my workflows"],
  "tags": ["ai", "automation"]
}
```

### POST /terminology.search
Semantic search for terminology entries.

**Request**:
```json
{
  "query": "compliance management",
  "limit": 10
}
```

**Response**:
```json
{
  "results": [
    {
      "entry": { /* terminology entry */ },
      "similarity": 0.92
    }
  ]
}
```

### PUT /terminology.update
Update a terminology entry.

**Request**:
```json
{
  "entryId": "uuid",
  "definition": "Updated definition",
  "usageExamples": ["New example"]
}
```

### DELETE /terminology.delete
Delete a terminology entry.

**Request**:
```json
{
  "entryId": "uuid"
}
```

### POST /terminology.export
Export terminology dictionary for cross-AI sync.

**Request**:
```json
{
  "format": "json" // or "csv", "markdown"
}
```

**Response**:
```json
{
  "exportUrl": "https://cdn.ai-orchestration.app/exports/uuid.json",
  "expiresAt": "2024-11-17T00:00:00Z"
}
```

## AI Templates

### GET /templates.list
List AI templates with filtering.

**Query Parameters**:
- `isPublic`: Show public templates
- `isMarketplace`: Show marketplace templates
- `sortBy`: rating, usage, created
- `limit`, `offset`: Pagination

**Response**:
```json
{
  "templates": [
    {
      "id": "uuid",
      "name": "Compliance Analyst",
      "description": "Specialized in policy analysis",
      "avatarUrl": "https://...",
      "rating": 4.8,
      "usageCount": 1250,
      "price": 9.99,
      "isMarketplace": true
    }
  ]
}
```

### POST /templates.create
Create a new AI template.

**Request**:
```json
{
  "name": "My Custom Agent",
  "description": "A specialized agent for...",
  "systemPrompt": "You are an expert in...",
  "functions": [
    {
      "name": "analyze_document",
      "description": "Analyze a document for compliance",
      "parameters": { /* JSON schema */ }
    }
  ],
  "personalityConfig": {
    "tone": "professional",
    "expertise": "high",
    "verbosity": "concise"
  },
  "modelConfig": {
    "temperature": 0.7,
    "maxTokens": 2000
  }
}
```

### POST /templates.test
Test an AI template with a sample prompt.

**Request**:
```json
{
  "templateId": "uuid",
  "testPrompt": "Analyze this policy document...",
  "integrationId": "uuid"
}
```

**Response**:
```json
{
  "response": "Based on the policy document...",
  "tokensUsed": 450,
  "latency": 1200,
  "cost": 0.015
}
```

### POST /templates.purchase
Purchase a marketplace template.

**Request**:
```json
{
  "templateId": "uuid",
  "paymentMethod": "stripe_pm_..."
}
```

## Conversations

### GET /conversations.list
List user's conversations.

**Response**:
```json
{
  "conversations": [
    {
      "id": "uuid",
      "title": "Policy Analysis Discussion",
      "participants": ["openai-integration-id", "claude-integration-id"],
      "lastMessageAt": "2024-11-16T00:00:00Z",
      "totalTokensUsed": 5000,
      "totalCost": 0.25
    }
  ]
}
```

### POST /conversations.create
Start a new conversation.

**Request**:
```json
{
  "title": "New Discussion",
  "participants": ["integration-id-1", "integration-id-2"],
  "mode": "collaborative"
}
```

### POST /conversations.sendMessage
Send a message in a conversation.

**Request**:
```json
{
  "conversationId": "uuid",
  "content": "What are the key compliance requirements?",
  "attachments": ["file-id-1"]
}
```

**Response** (streaming):
```json
{
  "messageId": "uuid",
  "responses": [
    {
      "integrationId": "uuid",
      "content": "The key compliance requirements are...",
      "tokensUsed": 150,
      "cost": 0.005
    }
  ]
}
```

### GET /conversations.messages
Get messages in a conversation.

**Query Parameters**:
- `conversationId`: Required
- `limit`, `offset`: Pagination

## Workflows

### GET /workflows.list
List automation workflows.

**Response**:
```json
{
  "workflows": [
    {
      "id": "uuid",
      "name": "Daily Compliance Check",
      "status": "active",
      "lastRunAt": "2024-11-16T00:00:00Z",
      "lastRunStatus": "success",
      "runCount": 45,
      "successRate": 0.98
    }
  ]
}
```

### POST /workflows.create
Create a new workflow.

**Request**:
```json
{
  "name": "Policy Analysis Workflow",
  "description": "Automatically analyze new policies",
  "steps": [
    {
      "type": "ai_task",
      "integrationId": "uuid",
      "templateId": "uuid",
      "prompt": "Analyze this policy: {{input.policyUrl}}"
    },
    {
      "type": "condition",
      "condition": "{{step1.compliance_score}} < 0.8",
      "ifTrue": "step3",
      "ifFalse": "step4"
    }
  ],
  "triggers": [
    {
      "type": "schedule",
      "cron": "0 9 * * *"
    }
  ]
}
```

### POST /workflows.run
Manually trigger a workflow.

**Request**:
```json
{
  "workflowId": "uuid",
  "input": {
    "policyUrl": "https://..."
  }
}
```

## Learning Patterns

### GET /patterns.list
Get AI learning patterns for the user.

**Response**:
```json
{
  "patterns": [
    {
      "patternType": "ai_preference",
      "data": {
        "preferredAI": "claude",
        "preferredForTasks": ["analysis", "writing"]
      },
      "confidence": 0.87,
      "occurrences": 42
    }
  ]
}
```

## Admin APIs

### GET /admin.users.list
List all users (admin only).

### POST /admin.templates.moderate
Approve/reject marketplace templates.

### GET /admin.analytics
Get platform-wide analytics.

## WebSocket Events

### Connection
```javascript
const ws = new WebSocket('wss://api.ai-orchestration.app/ws?token=jwt_token');
```

### Events

**message.stream** - Real-time AI response streaming
```json
{
  "event": "message.stream",
  "data": {
    "messageId": "uuid",
    "chunk": "partial response text...",
    "done": false
  }
}
```

**integration.sync** - Integration sync status
```json
{
  "event": "integration.sync",
  "data": {
    "integrationId": "uuid",
    "status": "syncing",
    "progress": 0.45
  }
}
```

**workflow.status** - Workflow execution updates
```json
{
  "event": "workflow.status",
  "data": {
    "workflowRunId": "uuid",
    "status": "running",
    "currentStep": 2,
    "totalSteps": 5
  }
}
```

## Error Responses

All errors follow this format:
```json
{
  "error": {
    "code": "INVALID_INPUT",
    "message": "The provided API key is invalid",
    "details": { /* additional context */ }
  }
}
```

**Error Codes**:
- `UNAUTHORIZED`: Invalid or missing authentication
- `FORBIDDEN`: Insufficient permissions
- `NOT_FOUND`: Resource not found
- `INVALID_INPUT`: Validation error
- `RATE_LIMIT_EXCEEDED`: Too many requests
- `INTEGRATION_ERROR`: AI platform error
- `INTERNAL_ERROR`: Server error

## Rate Limiting

**Headers**:
- `X-RateLimit-Limit`: Maximum requests per window
- `X-RateLimit-Remaining`: Remaining requests
- `X-RateLimit-Reset`: Unix timestamp when limit resets

**Limits by Tier**:
- Free: 100 requests/minute
- Pro: 1000 requests/minute
- Enterprise: Custom limits
