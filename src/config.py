"""Ultimate RAG Configuration

Combines: SurrealDB + LightRAG + RAG-Anything + RAGFlow
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Ultimate RAG Configuration."""
    
    # SurrealDB
    SURREALDB_URL = os.getenv("SURREALDB_URL", "ws://localhost:8000")
    SURREALDB_USER = os.getenv("SURREALDB_USER", "root")
    SURREALDB_PASSWORD = os.getenv("SURREALDB_PASSWORD", "root")
    SURREALDB_NAMESPACE = os.getenv("SURREALDB_NAMESPACE", "ultrarag")
    
    # Tables
    CHUNK_TABLE = "chunk"
    ENTITY_TABLE = "entity"
    RELATION_TABLE = "relation"
    
    # LightRAG features
    ENABLE_KG_EXTRACTION = os.getenv("ENABLE_KG_EXTRACTION", "true").lower() == "true"
    ENABLE_RERANKER = os.getenv("ENABLE_RERANKER", "true").lower() == "true"
    ENABLE_CITATIONS = os.getenv("ENABLE_CITATIONS", "true").lower() == "true"
    
    # RAG-Anything features
    PARSER = os.getenv("PARSER", "mineru")
    ENABLE_MULTIMODAL = os.getenv("ENABLE_MULTIMODAL", "false").lower() == "true"
    
    # RAGFlow features
    ENABLE_WEB_UI = os.getenv("ENABLE_WEB_UI", "true").lower() == "true"
    
    # LLM
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")
    LLM_MODEL = os.getenv("LLM_MODEL", "llama3.2")
    LLM_API_KEY = os.getenv("LLM_API_KEY", "")
    LLM_BASE_URL = os.getenv("LLM_BASE_URL", "http://localhost:11434")
    
    # Embeddings
    EMBED_PROVIDER = os.getenv("EMBED_PROVIDER", "ollama")
    EMBED_MODEL = os.getenv("EMBED_MODEL", "nomic-embed-text")
    EMBED_DIM = int(os.getenv("EMBED_DIM", "768"))
    
    # Chunking
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "1200"))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "100"))
    
    @classmethod
    def get_features(cls):
        """Get enabled features."""
        f = ["HNSW Vector Index", "Knowledge Graph"]
        if cls.ENABLE_KG_EXTRACTION:
            f.append("Entity Extraction")
        if cls.ENABLE_RERANKER:
            f.append("Reranker")
        if cls.ENABLE_CITATIONS:
            f.append("Citations")
        if cls.ENABLE_MULTIMODAL:
            f.append("Multimodal")
        if cls.ENABLE_WEB_UI:
            f.append("Web Dashboard")
        return f