import chromadb


# Create a persistent ChromaDB client
client = chromadb.PersistentClient(path="data/chroma")


# Create or load our collection
collection = client.get_or_create_collection(
    name="study_documents",
    configuration={
        "hnsw": {
            "space": "cosine"
        }
    }
)


def add_chunks(chunks, embeddings):
    """
    Store chunks, embeddings, and metadata in ChromaDB.
    """

    ids = [f"chunk_{i}" for i in range(len(chunks))]

    documents = [chunk["text"] for chunk in chunks]

    metadatas = [
        {
            "source": chunk["source"],
            "page": chunk["page"]
        }
        for chunk in chunks
    ]

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )