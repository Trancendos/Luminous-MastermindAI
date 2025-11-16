# AI Orchestration Platform - Database Schema

## Overview

The database schema is designed for a modular, scalable AI orchestration system with support for terminology learning, multi-AI integration, template generation, and workflow automation.

**Database Engine**: PostgreSQL 15+
**ORM**: Drizzle ORM
**Vector Database**: Qdrant or Chroma (for semantic search)

## Core Tables

### users
Stores user account information and preferences.

```sql
CREATE TABLE users (
  id VARCHAR(36) PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  name VARCHAR(255) NOT NULL,
  avatar_url TEXT,
  role VARCHAR(50) DEFAULT 'user', -- 'user', 'admin', 'enterprise'
  subscription_tier VARCHAR(50) DEFAULT 'free', -- 'free', 'pro', 'enterprise'
  subscription_status VARCHAR(50) DEFAULT 'active', -- 'active', 'cancelled', 'expired'
  subscription_expires_at TIMESTAMP,
  preferences JSON DEFAULT '{}', -- UI preferences, default AI, etc.
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  last_login_at TIMESTAMP
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_subscription_tier ON users(subscription_tier);
```

### ai_integrations
Stores AI platform connections and credentials.

```sql
CREATE TABLE ai_integrations (
  id VARCHAR(36) PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  platform VARCHAR(100) NOT NULL, -- 'openai', 'anthropic', 'google', 'xai', 'cohere', 'perplexity', 'ollama'
  name VARCHAR(255) NOT NULL, -- User-friendly name
  credentials_encrypted TEXT NOT NULL, -- AES-256 encrypted JSON
  status VARCHAR(50) DEFAULT 'disconnected', -- 'connected', 'disconnected', 'error'
  last_sync_at TIMESTAMP,
  last_error TEXT,
  usage_stats JSON DEFAULT '{}', -- { tokens_used, requests_made, cost, etc. }
  config JSON DEFAULT '{}', -- Platform-specific configuration
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_ai_integrations_user_id ON ai_integrations(user_id);
CREATE INDEX idx_ai_integrations_platform ON ai_integrations(platform);
CREATE INDEX idx_ai_integrations_status ON ai_integrations(status);
```

### terminology_entries
Stores personal terminology dictionary entries.

```sql
CREATE TABLE terminology_entries (
  id VARCHAR(36) PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  term VARCHAR(500) NOT NULL,
  definition TEXT NOT NULL,
  context VARCHAR(100), -- 'technical', 'business', 'personal', 'casual'
  usage_examples JSON DEFAULT '[]', -- Array of example sentences
  related_terms JSON DEFAULT '[]', -- Array of related term IDs
  frequency INT DEFAULT 1, -- How often this term is used
  last_used_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  tags JSON DEFAULT '[]', -- Array of tags
  is_public BOOLEAN DEFAULT FALSE, -- Can other users see this?
  embedding_id VARCHAR(100), -- Reference to vector DB
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_terminology_user_id ON terminology_entries(user_id);
CREATE INDEX idx_terminology_term ON terminology_entries(term);
CREATE INDEX idx_terminology_context ON terminology_entries(context);
CREATE INDEX idx_terminology_frequency ON terminology_entries(frequency DESC);
```

### ai_templates
Stores custom AI agent templates.

```sql
CREATE TABLE ai_templates (
  id VARCHAR(36) PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  avatar_url TEXT,
  system_prompt TEXT NOT NULL, -- The personality/instructions
  functions JSON DEFAULT '[]', -- Array of available functions/tools
  personality_config JSON DEFAULT '{}', -- { tone, expertise, style, etc. }
  knowledge_sources JSON DEFAULT '[]', -- Array of attached documents/URLs
  model_config JSON DEFAULT '{}', -- { temperature, top_p, max_tokens, etc. }
  allowed_integrations JSON DEFAULT '[]', -- Which AI platforms can use this template
  cost_limit_per_request DECIMAL(10, 2), -- Max cost per request
  version INT DEFAULT 1,
  is_public BOOLEAN DEFAULT FALSE,
  is_marketplace BOOLEAN DEFAULT FALSE, -- Available for sale?
  price DECIMAL(10, 2), -- If marketplace template
  usage_count INT DEFAULT 0,
  rating DECIMAL(3, 2) DEFAULT 0.00, -- Average rating (0-5)
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_ai_templates_user_id ON ai_templates(user_id);
CREATE INDEX idx_ai_templates_is_public ON ai_templates(is_public);
CREATE INDEX idx_ai_templates_is_marketplace ON ai_templates(is_marketplace);
CREATE INDEX idx_ai_templates_rating ON ai_templates(rating DESC);
```

### conversations
Stores multi-AI conversation sessions.

```sql
CREATE TABLE conversations (
  id VARCHAR(36) PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  title VARCHAR(500),
  participants JSON NOT NULL, -- Array of AI integration IDs
  mode VARCHAR(50) DEFAULT 'single', -- 'single', 'multi', 'collaborative'
  context JSON DEFAULT '{}', -- Shared context for all AIs
  metadata JSON DEFAULT '{}', -- Workflow info, routing decisions, etc.
  total_tokens_used INT DEFAULT 0,
  total_cost DECIMAL(10, 4) DEFAULT 0.0000,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  last_message_at TIMESTAMP
);

CREATE INDEX idx_conversations_user_id ON conversations(user_id);
CREATE INDEX idx_conversations_last_message_at ON conversations(last_message_at DESC);
```

### messages
Stores individual messages within conversations.

```sql
CREATE TABLE messages (
  id VARCHAR(36) PRIMARY KEY DEFAULT gen_random_uuid(),
  conversation_id VARCHAR(36) NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
  sender_type VARCHAR(50) NOT NULL, -- 'user', 'ai'
  sender_id VARCHAR(36), -- User ID or AI integration ID
  content TEXT NOT NULL,
  metadata JSON DEFAULT '{}', -- Model used, latency, confidence, etc.
  tokens_used INT DEFAULT 0,
  cost DECIMAL(10, 4) DEFAULT 0.0000,
  attachments JSON DEFAULT '[]', -- Array of file references
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_messages_conversation_id ON messages(conversation_id);
CREATE INDEX idx_messages_created_at ON messages(created_at DESC);
```

### workflows
Stores automation workflows.

```sql
CREATE TABLE workflows (
  id VARCHAR(36) PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  steps JSON NOT NULL, -- Array of workflow steps
  triggers JSON NOT NULL, -- Array of trigger conditions
  status VARCHAR(50) DEFAULT 'active', -- 'active', 'paused', 'archived'
  last_run_at TIMESTAMP,
  last_run_status VARCHAR(50), -- 'success', 'failed', 'partial'
  run_count INT DEFAULT 0,
  success_count INT DEFAULT 0,
  error_count INT DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_workflows_user_id ON workflows(user_id);
CREATE INDEX idx_workflows_status ON workflows(status);
```

### workflow_runs
Stores individual workflow execution logs.

```sql
CREATE TABLE workflow_runs (
  id VARCHAR(36) PRIMARY KEY DEFAULT gen_random_uuid(),
  workflow_id VARCHAR(36) NOT NULL REFERENCES workflows(id) ON DELETE CASCADE,
  trigger_type VARCHAR(100), -- 'manual', 'scheduled', 'webhook', etc.
  trigger_data JSON,
  status VARCHAR(50) DEFAULT 'running', -- 'running', 'success', 'failed'
  steps_completed INT DEFAULT 0,
  steps_total INT,
  output JSON,
  error_message TEXT,
  started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  completed_at TIMESTAMP
);

CREATE INDEX idx_workflow_runs_workflow_id ON workflow_runs(workflow_id);
CREATE INDEX idx_workflow_runs_started_at ON workflow_runs(started_at DESC);
```

### learning_patterns
Stores AI learning patterns and insights.

```sql
CREATE TABLE learning_patterns (
  id VARCHAR(36) PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  pattern_type VARCHAR(100) NOT NULL, -- 'terminology_usage', 'ai_preference', 'workflow_pattern', etc.
  data JSON NOT NULL, -- Pattern-specific data
  confidence DECIMAL(5, 4) DEFAULT 0.0000, -- 0.0000 to 1.0000
  occurrences INT DEFAULT 1,
  last_seen_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_learning_patterns_user_id ON learning_patterns(user_id);
CREATE INDEX idx_learning_patterns_type ON learning_patterns(pattern_type);
CREATE INDEX idx_learning_patterns_confidence ON learning_patterns(confidence DESC);
```

### audit_logs
Stores comprehensive audit trail.

```sql
CREATE TABLE audit_logs (
  id VARCHAR(36) PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id VARCHAR(36) REFERENCES users(id) ON DELETE SET NULL,
  entity_type VARCHAR(100) NOT NULL, -- 'user', 'ai_integration', 'template', etc.
  entity_id VARCHAR(36),
  action VARCHAR(100) NOT NULL, -- 'created', 'updated', 'deleted', 'accessed'
  changes JSON, -- Before/after values
  ip_address VARCHAR(45),
  user_agent TEXT,
  metadata JSON DEFAULT '{}',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_audit_logs_user_id ON audit_logs(user_id);
CREATE INDEX idx_audit_logs_entity_type ON audit_logs(entity_type);
CREATE INDEX idx_audit_logs_created_at ON audit_logs(created_at DESC);
```

### api_keys
Stores user-generated API keys for platform access.

```sql
CREATE TABLE api_keys (
  id VARCHAR(36) PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  name VARCHAR(255) NOT NULL,
  key_hash VARCHAR(255) UNIQUE NOT NULL, -- Hashed API key
  key_prefix VARCHAR(20) NOT NULL, -- First few chars for identification
  scopes JSON DEFAULT '[]', -- Array of allowed scopes
  rate_limit INT DEFAULT 100, -- Requests per minute
  last_used_at TIMESTAMP,
  expires_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_api_keys_user_id ON api_keys(user_id);
CREATE INDEX idx_api_keys_key_hash ON api_keys(key_hash);
```

### template_purchases
Stores marketplace template purchases.

```sql
CREATE TABLE template_purchases (
  id VARCHAR(36) PRIMARY KEY DEFAULT gen_random_uuid(),
  buyer_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  template_id VARCHAR(36) NOT NULL REFERENCES ai_templates(id) ON DELETE CASCADE,
  seller_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  price DECIMAL(10, 2) NOT NULL,
  platform_fee DECIMAL(10, 2) NOT NULL, -- 30% commission
  seller_payout DECIMAL(10, 2) NOT NULL,
  payment_status VARCHAR(50) DEFAULT 'pending', -- 'pending', 'completed', 'refunded'
  payment_method VARCHAR(50),
  transaction_id VARCHAR(255),
  purchased_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_template_purchases_buyer_id ON template_purchases(buyer_id);
CREATE INDEX idx_template_purchases_seller_id ON template_purchases(seller_id);
CREATE INDEX idx_template_purchases_template_id ON template_purchases(template_id);
```

### template_ratings
Stores user ratings for templates.

```sql
CREATE TABLE template_ratings (
  id VARCHAR(36) PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  template_id VARCHAR(36) NOT NULL REFERENCES ai_templates(id) ON DELETE CASCADE,
  rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5),
  review TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(user_id, template_id)
);

CREATE INDEX idx_template_ratings_template_id ON template_ratings(template_id);
```

### omni_bridge_sync
Stores synchronization state with Omni-Bridge Enterprise.

```sql
CREATE TABLE omni_bridge_sync (
  id VARCHAR(36) PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  omni_bridge_url TEXT NOT NULL,
  api_key_encrypted TEXT NOT NULL,
  sync_enabled BOOLEAN DEFAULT TRUE,
  last_sync_at TIMESTAMP,
  sync_status VARCHAR(50) DEFAULT 'pending', -- 'pending', 'success', 'failed'
  sync_data JSON DEFAULT '{}', -- What data to sync
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_omni_bridge_sync_user_id ON omni_bridge_sync(user_id);
```

## Vector Database Schema (Qdrant/Chroma)

### terminology_embeddings
Stores vector embeddings for semantic search of terminology.

```python
# Collection schema for Qdrant
{
  "collection_name": "terminology_embeddings",
  "vectors": {
    "size": 1536,  # OpenAI text-embedding-3-small
    "distance": "Cosine"
  },
  "payload_schema": {
    "entry_id": "string",  # References terminology_entries.id
    "user_id": "string",
    "term": "string",
    "definition": "string",
    "context": "string",
    "frequency": "integer"
  }
}
```

### conversation_embeddings
Stores vector embeddings for semantic search of conversations.

```python
{
  "collection_name": "conversation_embeddings",
  "vectors": {
    "size": 1536,
    "distance": "Cosine"
  },
  "payload_schema": {
    "message_id": "string",  # References messages.id
    "conversation_id": "string",
    "user_id": "string",
    "content": "string",
    "created_at": "datetime"
  }
}
```

## Relationships Diagram

```
users (1) ----< (many) ai_integrations
users (1) ----< (many) terminology_entries
users (1) ----< (many) ai_templates
users (1) ----< (many) conversations
users (1) ----< (many) workflows
users (1) ----< (many) learning_patterns
users (1) ----< (many) api_keys
users (1) ----< (many) omni_bridge_sync

conversations (1) ----< (many) messages
workflows (1) ----< (many) workflow_runs
ai_templates (1) ----< (many) template_purchases
ai_templates (1) ----< (many) template_ratings
```

## Data Migration Strategy

1. **Initial Schema**: Deploy all tables in Phase 1
2. **Seed Data**: Pre-populate with example templates and terminology
3. **Versioning**: Use Drizzle migrations for schema changes
4. **Backups**: Daily automated backups to S3-compatible storage
5. **Rollback**: Keep last 7 days of backups for emergency rollback

## Performance Optimizations

- **Indexes**: All foreign keys and frequently queried columns indexed
- **Partitioning**: Partition `messages` and `audit_logs` by month for large datasets
- **Caching**: Redis cache for frequently accessed data (user preferences, AI configs)
- **Read Replicas**: Use read replicas for analytics queries
- **Connection Pooling**: PgBouncer for efficient connection management

## Security Measures

- **Encryption at Rest**: All sensitive fields encrypted (credentials, API keys)
- **Encryption in Transit**: TLS 1.3 for all database connections
- **Row-Level Security**: PostgreSQL RLS for multi-tenant isolation
- **Audit Logging**: All data access logged in `audit_logs`
- **Key Rotation**: Automatic encryption key rotation every 90 days
