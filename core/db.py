"""
SurrealDB Client - Native HNSW + Graph + KV
"""

import os
from surrealdb import Surreal
from surrealdb.engine import RemoteEngine


class UltraDB:
    """Unified SurrealDB client for vectors, graph, and documents."""
    
    def __init__(self, url: str = None, user: str = None, password: str = None):
        self.url = url or os.getenv("SURREALDB_URL", "ws://localhost:8000")
        self.user = user or os.getenv("SURREALDB_USER", "root")
        self.password = password or os.getenv("SURREALDB_PASSWORD", "root")
        self.namespace = os.getenv("SURREALDB_NAMESPACE", "ultrarag")
        self.database = os.getenv("SURREALDB_DATABASE", "ultrarag")
        self._db = None
    
    async def connect(self):
        """Connect to SurrealDB."""
        self._db = Surreal(RemoteEngine(self.url))
        await self._db.connect()
        await self._db.use(self.namespace, self.database)
        await self._db.authenticate(self.user, self.password)
        return self
    
    async def close(self):
        """Close connection."""
        if self._db:
            await self._db.close()
    
    # ============ Vector (HNSW) ============
    
    async def create_vector_table(self, table: str, dim: int = 768):
        """Create table with HNSW vector index."""
        await self._db.query(f"""
            DEFINE TABLE {table} SCHEMAFULL;
            DEFINE FIELD content ON {table} TYPE string;
            DEFINE FIELD embedding ON {table} TYPE floatarray({dim});
            DEFINE FIELD metadata ON {table} TYPE object;
            DEFINE INDEX emb_idx ON {table} FIELDS embedding HNSW DIMENSION {dim} DISTANCE COSINE;
        """)
    
    async def insert_chunk(self, table: str, content: str, embedding: list, metadata: dict = None):
        """Insert chunk with vector."""
        return await self._db.create(table, {
            "content": content,
            "embedding": embedding,
            "metadata": metadata or {}
        })
    
    async def search_vectors(self, table: str, query_embedding: list, limit: int = 10):
        """HNSW vector search."""
        return await self._db.query(f"""
            SELECT * FROM {table}
            ORDER BY embedding <-> $embedding
            LIMIT {limit}
        """, {"embedding": query_embedding})
    
    # ============ Graph (Relations) ============
    
    async def create_entity_table(self):
        """Create entity table for knowledge graph."""
        await self._db.query("""
            DEFINE TABLE entity SCHEMAFULL;
            DEFINE FIELD name ON entity TYPE string;
            DEFINE FIELD type ON entity TYPE string;
            DEFINE FIELD properties ON entity TYPE object;
        """)
    
    async def create_relation_table(self):
        """Create relation edges table."""
        await self._db.query("""
            DEFINE TABLE relation SCHEMAFULL;
            DEFINE FIELD from ON relation TYPE record(entity);
            DEFINE FIELD to ON relation TYPE record(entity);
            DEFINE FIELD type ON relation TYPE string;
            DEFINE FIELD weight ON relation TYPE float;
        """)
    
    async def create_entity(self, name: str, entity_type: str, properties: dict = None):
        """Create entity node."""
        return await self._db.create("entity", {
            "name": name,
            "type": entity_type,
            "properties": properties or {}
        })
    
    async def create_relation(self, from_id: str, to_id: str, rel_type: str, weight: float = 1.0):
        """Create relation edge."""
        return await self._db.create("relation", {
            "from": from_id,
            "to": to_id,
            "type": rel_type,
            "weight": weight
        })
    
    async def get_graph(self, entity_id: str, depth: int = 2):
        """Get subgraph around entity."""
        return await self._db.query(f"""
            SELECT * FROM relation
            WHERE from = $entity_id OR to = $entity_id
        """, {"entity_id": entity_id})
    
    # ============ Documents (KV) ============
    
    async def create_document_table(self):
        """Create document table."""
        await self._db.query("""
            DEFINE TABLE document SCHEMAFULL;
            DEFINE FIELD title ON document TYPE string;
            DEFINE FIELD content ON document TYPE string;
            DEFINE FIELD source ON document TYPE string;
            DEFINE FIELD metadata ON document TYPE object;
            DEFINE FIELD created_at ON document TYPE datetime;
        """)
    
    async def insert_document(self, title: str, content: str, source: str = None, metadata: dict = None):
        """Insert document."""
        return await self._db.create("document", {
            "title": title,
            "content": content,
            "source": source,
            "metadata": metadata or {},
            "created_at": await self._db.query("time::now()")
        })
    
    async def search_fulltext(self, table: str, query: str, limit: int = 10):
        """Full-text search."""
        return await self._db.query(f"""
            SELECT * FROM {table}
            WHERE content @1@ $query
            LIMIT {limit}
        """, {"query": query})
    
    # ============ Chats ============
    
    async def create_chat_table(self):
        """Create chat history table."""
        await self._db.query("""
            DEFINE TABLE chat SCHEMAFULL;
            DEFINE FIELD messages ON chat TYPE array;
            DEFINE FIELD context ON chat TYPE object;
            DEFINE FIELD created_at ON chat TYPE datetime;
        """)
    
    async def create_chat(self):
        """Create new chat session."""
        return await self._db.create("chat", {
            "messages": [],
            "context": {},
            "created_at": await self._db.query("time::now()")
        })
    
    async def add_message(self, chat_id: str, role: str, content: str, sources: list = None):
        """Add message to chat."""
        return await self._db.update(chat_id, {
            "messages": {
                "role": role,
                "content": content,
                "sources": sources or []
            }
        })
    
    # ============ Init ============
    
    async def init_all(self):
        """Initialize all tables."""
        await self.create_vector_table("chunk")
        await self.create_entity_table()
        await self.create_relation_table()
        await self.create_document_table()
        await self.create_chat_table()
        return "Initialized all tables"