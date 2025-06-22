"""import chromadb
import os
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

embedding_function = OpenAIEmbeddingFunction(
    api_key=os.getenv("OPENAI_API_KEY")  # Load real OpenAI key
)

client = chromadb.Client()
collection = client.get_or_create_collection(name="chapter_versions", embedding_function=embedding_function)

def add_version(id, text, metadata):
    collection.add(documents=[text], ids=[id], metadatas=[metadata])

def query_versions(query_text):
    results = collection.query(query_texts=[query_text], n_results=3)
    return results
"""
"""import chromadb           CHALL
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
import uuid

# ✅ Load HuggingFace embedding model locally
embedding_function = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# ✅ Initialize ChromaDB client with HuggingFace embedding function
client = chromadb.Client()
collection = client.get_or_create_collection(
    name="book_versions",
    embedding_function=embedding_function
)

# ✅ Store rewritten content with version info
def add_version(version_name: str, text: str, metadata: dict):
    id = str(uuid.uuid4())  # unique ID for this version
    collection.add(
        documents=[text],
        ids=[id],
        metadatas=[metadata]
    )"""
"""import chromadb

# Initialize Chroma client and collection
client = chromadb.Client()
collection = client.get_or_create_collection(name="ai_writer_v1")

# ✅ Function to add a new version

def add_version(id: str, text: str, metadata: dict):
    collection.add(documents=[text], ids=[id], metadatas=[metadata])

# ✅ Function to fetch the latest version
def get_latest_version(id: str) -> str:
    results = collection.get(ids=[id])
    if results and "documents" in results and results["documents"]:
        return results["documents"][0]
    return "⚠️ No chapter found in ChromaDB."""
from chromadb import PersistentClient
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
import chromadb
import uuid
import os

client = PersistentClient(path="chromadb")

from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
embedding_function = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

collection = client.get_or_create_collection(
    name="ai_writer_v1",
    embedding_function=embedding_function,
)

"""def add_version(text, metadata=None):
    if metadata is None:
        metadata = {}
    id = str(uuid.uuid4())
    collection.add(documents=[text], ids=[id], metadatas=[metadata])
    print(f"✅ Added to ChromaDB with ID: {id}")"""

def add_version(collection_name, text, metadata=None):
    if metadata is None:
        metadata = {}

    client = chromadb.PersistentClient(path="chromadb_store")
    from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
    embedding_function = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

    collection = client.get_or_create_collection(
        name=collection_name,
        embedding_function=embedding_function,
    )

    id = str(uuid.uuid4())
    collection.add(documents=[text], ids=[id], metadatas=[metadata])
    print(f"✅ Added to ChromaDB with ID: {id}")

"""def get_latest_version():
    results = collection.get()
    if not results["documents"]:
        return None
    return results["documents"][-1]  # last added document"""

"""def get_latest_version():
    client = chromadb.PersistentClient(path="chromadb_store")
    collection = client.get_or_create_collection(name="ai_writer_v1")
    
    results = collection.get(limit=1)
    if results["documents"]:
        return results["documents"][0]
    return None"""

def get_latest_version(collection_name):
    client = chromadb.PersistentClient(path="chromadb_store")
    collection = client.get_or_create_collection(name=collection_name)

    results = collection.get(limit=1)
    if results["documents"]:
        return results["documents"][0]
    return None