from services.rag import ask_question


question = "What are the 5 Vs of Big Data?"

answer = ask_question(question, top_k=3)

print("\n--- Answer ---\n")
print(answer)