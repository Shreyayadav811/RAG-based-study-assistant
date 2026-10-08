from services.pdf_loader import load_pdf
from services.chunker import chunk_documents
from services.embeddings import create_embeddings
from services.vector_store import add_chunks


# Path to our PDF
pdf_path = "data/documents/bigdata_unit1.pdf"


# Step 1: Load PDF and extract text
documents = load_pdf(pdf_path)


# Step 2: Split extracted text into chunks
chunks = chunk_documents(documents)


# Step 3: Create embeddings for each chunk
embeddings = create_embeddings(chunks)

#Step 4: Store chunks and embeddings in ChromaDB
add_chunks(chunks, embeddings)

print("\nChunks successfully stored in ChromaDB.")


# -----------------------------
# Print results
# -----------------------------

print("Total pages:", len(documents))
print("Total chunks:", len(chunks))
print("Number of embeddings:", len(embeddings))
print("Embedding dimensions:", len(embeddings[0]))


print("\n--- First chunk ---")
print(chunks[0]["text"])

print("\nSource:", chunks[0]["source"])
print("Page:", chunks[0]["page"])


print("\n--- First embedding ---")
print(embeddings[0])


print("\n--- Chunk sizes ---")

for i, chunk in enumerate(chunks):
    print(
        f"Chunk {i + 1}: "
        f"{len(chunk['text'])} chars | "
        f"Page {chunk['page']}"
    )