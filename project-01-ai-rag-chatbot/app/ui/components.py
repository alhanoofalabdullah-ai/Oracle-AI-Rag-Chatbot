import streamlit as st

from app.database.connection import (
    ping_database,
)
from app.database.repository import (
    DocumentRepository,
)
from app.rag.service import (
    RAGService,
)


def render_sidebar() -> None:
    """
    Render system status sidebar.
    """

    with st.sidebar:

        st.header("System Status")

        if ping_database():

            st.success(
                "Oracle Database Connected"
            )

        else:

            st.error(
                "Oracle Database Unavailable"
            )

        try:

            repository = (
                DocumentRepository()
            )

            document_count = (
                repository
                .count_documents()
            )

            chunk_count = (
                repository
                .count_chunks()
            )

            st.metric(
                "Documents",
                document_count,
            )

            st.metric(
                "Indexed Chunks",
                chunk_count,
            )

        except Exception:

            st.warning(
                "Database statistics unavailable."
            )

        st.divider()

        st.caption(
            "Oracle AI RAG Chatbot"
        )

        st.caption(
            "Python • LangChain • "
            "OpenAI • Oracle Vector Search"
        )


def render_sources(
    results,
) -> None:

    if not results:

        return

    with st.expander(
        "Retrieved Sources",
        expanded=True,
    ):

        for index, result in enumerate(
            results,
            start=1,
        ):

            similarity = max(
                0.0,
                1.0 - result.distance,
            )

            st.markdown(
                f"### [Source {index}] "
                f"{result.file_name}"
            )

            st.caption(
                f"Chunk: {result.chunk_index} "
                f"| Similarity: "
                f"{similarity:.3f}"
            )

            preview = (
                result.content[:1200]
            )

            if len(
                result.content
            ) > 1200:

                preview += "..."

            st.write(preview)

            st.divider()


def render_upload_section() -> None:
    """
    Render document ingestion UI.
    """

    st.subheader(
        "Document Knowledge Base"
    )

    uploaded_files = st.file_uploader(
        "Upload enterprise documents",
        type=[
            "pdf",
            "docx",
            "txt",
            "md",
        ],
        accept_multiple_files=True,
    )

    if not uploaded_files:

        return

    if st.button(
        "Index Documents",
        type="primary",
        use_container_width=True,
    ):

        service = RAGService()

        for uploaded_file in uploaded_files:

            try:

                with st.spinner(
                    f"Indexing "
                    f"{uploaded_file.name}..."
                ):

                    summary = service.ingest(
                        file_name=(
                            uploaded_file.name
                        ),
                        data=(
                            uploaded_file
                            .getvalue()
                        ),
                    )

                st.success(
                    f"{summary.file_name} "
                    f"indexed successfully. "
                    f"{summary.chunks_created} "
                    f"chunks created."
                )

            except Exception as exc:

                st.error(
                    f"Failed to index "
                    f"{uploaded_file.name}: "
                    f"{exc}"
                )


def render_chat() -> None:
    """
    Render conversational RAG interface.
    """

    st.subheader(
        "Enterprise Knowledge Assistant"
    )

    if "messages" not in st.session_state:

        st.session_state.messages = []

    for message in (
        st.session_state.messages
    ):

        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )

            if message.get(
                "sources"
            ):

                render_sources(
                    message["sources"]
                )

    question = st.chat_input(
        "Ask a question about your documents..."
    )

    if not question:

        return

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    try:

        service = RAGService()

        with st.chat_message(
            "assistant"
        ):

            with st.spinner(
                "Searching Oracle "
                "Vector Search..."
            ):

                answer, sources = (
                    service.answer(
                        question
                    )
                )

            st.markdown(answer)

            render_sources(
                sources
            )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
                "sources": sources,
            }
        )

    except Exception as exc:

        error_message = (
            "The request could not be "
            "completed. Please check the "
            "application configuration."
        )

        with st.chat_message(
            "assistant"
        ):

            st.error(
                error_message
            )

            st.caption(
                str(exc)
            )


def render_app() -> None:
    """
    Render complete Streamlit application.
    """

    st.set_page_config(
        page_title=(
            "Oracle AI RAG Chatbot"
        ),
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title(
        "Oracle AI RAG Chatbot"
    )

    st.markdown(
        """
        **Enterprise Retrieval-Augmented Generation platform**

        Search enterprise documents using semantic vector
        retrieval and AI-generated grounded responses.
        """
    )

    render_sidebar()

    st.divider()

    render_upload_section()

    st.divider()

    render_chat()
