from app.documents.chunker import (
    normalize_text,
    split_text,
)


def test_normalize_text():

    text = (
        "Hello    world\n\n\n"
        "This is a test."
    )

    result = normalize_text(
        text
    )

    assert result == (
        "Hello world\n\n"
        "This is a test."
    )


def test_empty_text():

    result = split_text(
        ""
    )

    assert result == []


def test_chunk_generation():

    text = "A" * 3000

    chunks = split_text(
        text,
        chunk_size=500,
        chunk_overlap=100,
    )

    assert len(chunks) > 1

    assert chunks[0].index == 0

    assert all(
        chunk.content
        for chunk in chunks
    )


def test_invalid_chunk_size():

    try:

        split_text(
            "Hello",
            chunk_size=0,
        )

    except ValueError as exc:

        assert (
            "chunk_size"
            in str(exc)
        )

    else:

        raise AssertionError(
            "Expected ValueError"
        )


def test_invalid_overlap():

    try:

        split_text(
            "Hello",
            chunk_size=10,
            chunk_overlap=10,
        )

    except ValueError as exc:

        assert (
            "chunk_overlap"
            in str(exc)
        )

    else:

        raise AssertionError(
            "Expected ValueError"
        )
