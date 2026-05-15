# Ultimate RAG Framework

**Core:** SurrealDB (HNSW + Graph + KV) - Unified Backend

Inspired by best features from:

| Project | Source | Stars |
|---------|--------|------|
| **SurrealDB** | https://surrealdb.com | - |
| **LightRAG** | https://github.com/MiniMaxAI/LightRAG | 35k |
| **RAG-Anything** | https://github.com/AnyGPU/RAG-Anything | 20k |
| **RAGFlow** | https://github.com/infiniflow/ragflow | 80k |
| **Glean** | https://github.com/Glean-dev/glean | 1.3k |
| **Onyx** | https://github.com/onyx-hr/onyx | 29k |
| **Open Notebook** | https://github.com/lfnovo/open-notebook | 23k |

## Features Summary (Consolidated)

### Core Storage (SurrealDB)
- **HNSW Vector Index** - Fast similarity search
- **Graph Relations** - Multi-hop queries  
- **Full-text Search** - Keyword retrieval
- **Hybrid Queries** - Vector + graph fusion
- **Unified Tables** - document, chunk, entity, relation, notebook, source, chat, agent

### Retrieval (LightRAG)
- **Dual-level Retrieval** - Low-level (entities/relations) + High-level (semantic)
- **Reranker** - Mixed query boost

### Multimodal I/O
- **Input** (RAG-Anything): PDF, Office, images, tables, equations
- **Input** (Open Notebook): Videos, audio, web pages
- **Output** (Open Notebook): Audio/podcast with multi-speaker voices

### Agents & Tools (Onyx + RAGFlow)
- **Agentic RAG** - Hybrid index + AI Agents
- **Deep Research** - Multi-step research flow
- **Web Search** - Serper, Google, Brave, SearXNG, Firecrawl
- **Code Execution** - Sandbox for data analysis
- **Connectors** - 50+ data source connectors

### Code Intelligence (Glean)
- **Symbol Facts** - Location, type, relationships
- **Cross-references** - Function calls, method calls
- **Call/Type Hierarchies** - Inheritance trees
- **SCIP/LSIF** - Rust, Go, TypeScript, Java support

### UI/UX (RAGFlow + Open Notebook)
- **Web Dashboard** - Visual management
- **Template Chunking** - Intelligent templates
- **Multi-Notebook** - Organize research projects
- **Multi-Lingual** - UI in 8+ languages
- **Cross-Language Query** - Query in any language

### Enterprise (Onyx)
- **SSO** - Google OAuth, OIDC, SAML
- **RBAC** - Role-based access control
- **Analytics** - Usage metrics
- **Whitelabeling** - Custom branding

### Integrations
- **18+ AI Providers** - OpenAI, Anthropic, Ollama, LM Studio, etc.
- **MCP** - Claude Desktop, VS Code support
- **REST API** - Full programmatic access
- **Data Sync** - S3, Notion, Confluence, GDrive

## Architecture - Canvas Mindmap

```
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                         ULTIMATE RAG FRAMEWORK                                        ║
║                                    🗄️  Core: SurrealDB (HNSW + Graph + KV)  🗄️                        ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════╝
                                                    │
         ┌───────────────────────────────────────────┼───────────────────────────────────────────┐
         │                                           │                                           │
         ▼                                           ▼                                           ▼
╔════════════════════╗                   ╔════════════════════╗                   ╔════════════════════╗
║    USER LAYER    ║                   ║    LLM LAYER      ║                   ║   AGENT LAYER     ║
╠════════════════════╣                   ╠════════════════════╣                   ╠════════════════════╣
║ ┌───────────────┐ ║                   ║ ┌───────────────┐ ║                   ║ ┌───────────────┐ ║
║ │ 🖥️ Web UI    │ ║                   ║ │ 🤖 OpenAI     │ ║                   ║ │ ⚡ Agentic RAG │ ║
║ │ 🌐 REST API   │ ║                   ║ │ 🧠 Anthropic  │ ║                   ║ │ 🔍 Deep Search│ ║
║ │ 💻 CLI        │ ║                   ║ │ 🦙 Ollama     │ ║                   ║ │ 🔧 Tools/MCP  │ ║
║ │ 🎙️ Voice     │ ║                   ║ │ 🌐 18+ more  │ ║                   ║ │ 🔌 Connectors │ ║
║ │ 🔌 MCP        │ ║                   ║ └───────────────┘ ║                   ║ └───────────────┘ ║
║ └───────────────┘ ║                                           │                   │
╚════════════════════╝                                           │                   │
         │                                                       │                   │
         └───────────────────────────────┬───────────────────────┘                   │
                                         ▼
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                     📦 SURRERALDB STORAGE LAYER                                        ║
╠══════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                                      ║
║    ┌─────────────────────────────────────────────────────────────────────────────────────────────┐        ║
║    │                              📊 KNOWLEDGE GRAPH                                         │        ║
║    │   ┌─────────┐         ┌─────────┐         ┌─────────┐         ┌─────────┐        │        ║
║    │   │ Entity  │◄───────►│Relation │◄───────►│ Concept │◄───────►│  Tool  │        │        ║
║    │   │  Node   │         │  Edge   │         │  Node   │         │  Node  │        │        ║
║    │   └─────────┘         └─────────┘         └─────────┘         └─────────┘        │        ║
║    │                                                                                     │        ║
║    │    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │        ║
║    │    │ PART_OF      │    │MENTIONS_IN  │    │RELATED_TO   │    │    CALLS    │  │        ║
║    │    └──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘  │        ║
║    └─────────────────────────────────────────────────────────────────────────────────────────────┘        ║
║                                                                                                      ║
║    ┌────────────────┐  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐                     ║
║    │  📐 VECTOR     │  │  🔗 GRAPH     │  │  📄 DOCUMENT  │  │  💬 CHAT      │                     ║
║    │  (HNSW Index) │  │ (Relations)   │  │    (KV/JSON) │  │    (History)  │                     ║
║    │                │  │                │  │                │  │                │                     ║
║    │ • Semantic    │  │ • Multi-hop   │  │ • Raw text   │  │ • Messages    │                     ║
║    │ • Similarity   │  │ • Traversal   │  │ • Metadata   │  │ • Context    │                     ║
║    │ • Re-ranking  │  │ • Reasoning   │  │ • Embeddings │  │ • Citations   │                     ║
║    └────────────────┘  └────────────────┘  └────────────────┘  └────────────────┘                     ║
║                                                                                                      ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════╝
                                                    │
                                                    ▼
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                     📤 OUTPUT LAYER                                                ║
╠══════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐             ║
║  │    💬      │  │   🎙️      │  │    🖼️     │  │   📄       │  │   📊       │             ║
║  │   Chat     │  │  Podcast   │  │  Images    │  │ Artifacts  │  │ Citations  │             ║
║  └────────────┘  └────────────┘  └────────────┘  └────────────┘  └────────────┘             ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════╝
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Start SurrealDB
```bash
docker run -p 8000:8000 surrealdb/surrealdb:latest start
```

### Index Documents
```bash
python main.py index --path ./docs/
```

### Query
```bash
python main.py query "Your question?"
```

### API Server
```bash
python main.py serve --port 8001
```

## Tech Stack

### Own Code + SurrealDB

No SDKs from RAGFlow/OpenNotebook - we write everything ourselves:

| Component | Native SurrealDB / Custom |
|-----------|-------------------|
| **Database** | ✅ Custom SurrealDB client |
| **Retrieval** | ✅ Custom dual-level |
| **Multimodal** | ✅ Custom ETL |
| **UI** | ✅ Custom FastAPI + React |
| **LLM** | ✅ Custom orchestrator |
| **Chat** | ✅ Custom WebSocket |
| **Everything** | ✅ Own code |

### SurrealDB Native Capabilities
- **HNSW** - Native vector indexing
- **Graph** - Native relations/edges
- **KV/JSON** - Native document storage
- **Full-text** - Native search

### App Layer (Custom UI - Astro Full Stack)
- **Full UI** - Astro (Chat + Graph + Editor + Search)
- **Canvas** - fabric.js (knowledge graph viz)
- **Editor** - tiptap (inline edit AI output + save)
- **Backend** - FastAPI (Python)
- **WebSocket** - Real-time chat

### Libraries Used
- `surrealdb` - Database driver
- `langchain` - LLM abstraction
- `llamaindex` - Document indexing
- `sentence-transformers` - Embeddings

### Not Used (inspiration only)
- RAGFlow SDK
- Open Notebook SDK

## Additional Features

### Caching & Performance
- **LLM Response Cache** - Token optimization
- **Embedding Cache** - Skip re-embedding
- **Result Cache** - Skip repeated queries

### Operations
- **Rate Limiting** - Per-user limits
- **Auth** - API keys, OAuth
- **Analytics** - Usage tracking
- **Monitoring** - Health checks, metrics

### Deployment
- **Docker** - Single container
- **Docker Compose** - Full stack
- **Kubernetes** - Production

### Configuration
- **Environment** - .env files
- **Secrets** - API keys management

### Missing from Originals?
- Video understanding (from VideoRAG)
- Mini/small models (from MiniRAG)
- OpenSearch backend (from LightRAG)
- MongoDB/PostgreSQL backends

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-----------|
| `/health` | GET | Health check |
| `/index` | POST | Index documents |
| `/query` | POST | Query RAG |
| `/chat` | POST | Chat with RAG |
| `/graph` | GET | Knowledge graph |

---

Built with: SurrealDB + LightRAG + RAG-Anything + RAGFlow