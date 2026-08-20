import re

from dataclasses import dataclass


@dataclass
class TextChunk:
    """
    Represents one chunk of a document.
    """

    index: int
    content: str
    metadata: dict


def normalize_text(
    text: str,
) -> str:

    text = text.replace(
        "\x00",
        " ",
    )

    text = re.sub(
        r"[ \t]+",
        " ",
        text,
    )

    text = re.sub(
        r"\n{3,}",
        "\n\n",
        text,
    )

    return text.strip()


def split_text(
    text: str,
    chunk_size: int = 900,
    chunk_overlap: int = 150,
) -> list[TextChunk]:

    if chunk_size <= 0:

        raise ValueError(
            "chunk_size must be greater than zero."
        )

    if chunk_overlap < 0:

        raise ValueError(
            "chunk_overlap cannot be negative."
        )

    if chunk_overlap >= chunk_size:

        raise ValueError(
            "chunk_overlap must be smaller "
            "than chunk_size."
        )

    text = normalize_text(text)

    if not text:

        return []

    chunks: list[TextChunk] = []

    start = 0
    index = 0

    while start < len(text):

        end = min(
            start + chunk_size,
            len(text),
        )

        # Try to break at a natural boundary.
        if end < len(text):

            paragraph_break = text.rfind(
                "\n\n",
                start,
                end,
            )

            sentence_breaks = [
                text.rfind(
                    ". ",
                    start,
                    end,
                ),
                text.rfind(
                    "? ",
                    start,
                    end,
                ),
                text.rfind(
                    "! ",
                    start,
                    end,
                ),
            ]

            sentence_break = max(
                sentence_breaks
            )

            boundary = max(
                paragraph_break,
                sentence_break,
            )

            minimum_boundary = (
                start
                + int(chunk_size * 0.55)
            )

            if boundary >= minimum_boundary:

                end = boundary + 1

        content = text[
            start:end
        ].strip()

        if content:

            chunks.append(
                TextChunk(
                    index=index,
                    content=content,
                    metadata={
                        "start_char": start,
                        "end_char": end,
                    },
                )
            )

            index += 1

        if end >= len(text):

            break

        next_start = (
            end - chunk_overlap
        )

        start = max(
            next_start,
            start + 1,
        )

    return chunks
