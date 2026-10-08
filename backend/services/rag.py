from services.retriever import retrieve
from services.llm import generate_answer


def build_context(query: str, top_k: int = 5):

    results = retrieve(query, top_k)

    context_parts = []

    for result in results:

        context_parts.append(
            f"[Page {result['page']}]\n"
            f"{result['text']}"
        )

    context = "\n\n".join(context_parts)

    return context


def ask_question(question: str, top_k: int = 5):

    context = build_context(question, top_k)

    answer = generate_answer(context, question)

    return answer