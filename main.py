#!/usr/bin/env python3
"""
Ultimate RAG CLI
Combines: SurrealDB + LightRAG + RAG-Anything + RAGFlow
"""

import argparse
import asyncio
import sys

from src import Config


async def init_db():
    """Initialize SurrealDB schema."""
    print("Initializing SurrealDB...")
    print(f"Namespace: {Config.SURREALDB_NAMESPACE}")
    print(f"Tables: {Config.CHUNK_TABLE}, {Config.ENTITY_TABLE}, {Config.RELATION_TABLE}")
    print("Done!")


async def index_docs(path: str):
    """Index documents."""
    print(f"Indexing: {path}")
    print("Features:", ", ".join(Config.get_features()))


async def query(q: str):
    """Query the RAG system."""
    print(f"Query: {q}")


async def chat():
    """Interactive chat."""
    print("Ultimate RAG Chat")
    print("Type 'quit' to exit\n")
    
    while True:
        q = input("You: ")
        if q.lower() in ("quit", "q"):
            break
        await query(q)


def main():
    parser = argparse.ArgumentParser(description="Ultimate RAG CLI")
    subparsers = parser.add_subparsers(dest="command")
    
    subparsers.add_parser("init", help="Initialize database")
    
    idx = subparsers.add_parser("index", help="Index documents")
    idx.add_argument("--path", required=True)
    
    q = subparsers.add_parser("query", help="Query")
    q.add_argument("query", help="Query string")
    
    subparsers.add_parser("chat", help="Interactive chat")
    
    serve = subparsers.add_parser("serve", help="Start API server")
    serve.add_argument("--port", type=int, default=8001)
    
    args = parser.parse_args()
    
    if args.command == "init":
        asyncio.run(init_db())
    elif args.command == "index":
        asyncio.run(index_docs(args.path))
    elif args.command == "query":
        asyncio.run(query(args.query))
    elif args.command == "chat":
        asyncio.run(chat())
    elif args.command == "serve":
        print(f"Starting API on port {args.port}...")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()