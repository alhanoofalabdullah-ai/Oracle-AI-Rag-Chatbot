from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
)

from langchain_openai import ChatOpenAI

from app.config import get_settings
from app.database.repository import (
    SearchResult,
)


SYSTEM_PROMPT = """
You are an enterprise knowledge assistant.

Your task is to answer questions using only
the information contained in the retrieved
enterprise document context.

Rules:

1. Do not invent facts.
2. Do not use external knowledge.
3. If the context is insufficient, say so.
4. Preserve important dates and numbers.
5. Preserve technical terminology.
6. Keep answers clear and professional.
7. Cite factual statements using [Source N].
8. Do not fabricate source references.
9. Do not claim that you accessed a document
   unless that document appears in the context.
"""


class AnswerGenerator:
    """
    Generates grounded answers from retrieved
    enterprise document context.
    """

    def __init__(self):

        settings = get_settings()

        self.llm = ChatOpenAI(
            model=settings.chat_model,
            temperature=0,
            api_key=settings.openai_api_key,
        )

    @staticmethod
    def build_context(
        results: list[SearchResult],
    ) -> str:

        blocks: list[str] = []

        for index, result in enumerate(
            results,
            start=1,
        ):

            blocks.append(
                "\n".join(
                    [
                        f"[Source {index}]",
                        f"File: {result.file_name}",
                        (
                            f"Chunk: "
                            f"{result.chunk_index}"
                        ),
                        "Content:",
                        result.content,
                    ]
                )
            )

        return "\n\n---\n\n".join(
            blocks
        )

    def generate(
        self,
        question: str,
        results: list[SearchResult],
    ) -> str:

        if not results:

            return (
                "I could not find relevant "
                "information in the indexed "
                "knowledge base."
            )

        context = self.build_context(
            results
        )

        user_prompt = f"""
Retrieved enterprise context:

{context}

User question:

{question}

Provide a professional answer based
only on the retrieved context.
"""

        messages = [
            SystemMessage(
                content=SYSTEM_PROMPT
            ),
            HumanMessage(
                content=user_prompt
            ),
        ]

        response = self.llm.invoke(
            messages
        )

        return str(
            response.content
        )
