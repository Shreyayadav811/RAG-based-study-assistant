from services.retriever import retrieve


query = "What are the 5 Vs of Big Data?"

results = retrieve(query, top_k=3)


print(f"Query: {query}\n")


for i, result in enumerate(results, start=1):

    print(f"--- Result {i} ---")
    print(f"Page: {result['page']}")
    print(f"Distance: {result['distance']}")
    print(result["text"])
    print()