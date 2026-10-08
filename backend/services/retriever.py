from services.vector_store import collection
from services.embeddings import model


QUERY_PREFIX = "Represent this sentence for searching relevant passages: "


def retrieve(query: str, top_k: int = 5):

    # Convert query into embedding
    query_text = QUERY_PREFIX + query

    query_embedding = model.encode(
        query_text,
        normalize_embeddings=True
    )

    # Search ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )

    retrieved_chunks = []

    for i in range(len(results["documents"][0])):

        retrieved_chunks.append({
            "text": results["documents"][0][i],
            "source": results["metadatas"][0][i]["source"],
            "page": results["metadatas"][0][i]["page"],
            "distance": results["distances"][0][i]
        })

    return retrieved_chunks