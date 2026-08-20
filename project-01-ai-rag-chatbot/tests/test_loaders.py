from app.documents.loaders import (
    load_document,
)


def test_load_text():

    document = load_document(
        "example.txt",
        b"Enterprise AI knowledge platform",
    )

    assert document.file_name == (
        "example.txt"
    )

    assert (
        "Enterprise AI"
        in document.text
    )


def test_load_markdown():

    document = load_document(
        "README.md",
        b"# Enterprise AI",
    )

    assert document.text == (
        "# Enterprise AI"
    )


def test_unsupported_extension():

    try:

        load_document(
            "malware.exe",
            b"not supported",
        )

    except ValueError as exc:

        assert (
            "Unsupported file type"
            in str(exc)
        )

    else:

        raise AssertionError(
            "Expected ValueError"
        )


def test_empty_document():

    try:

        load_document(
            "empty.txt",
            b"",
        )

    except ValueError as exc:

        assert (
            "No readable text"
            in str(exc)
        )

    else:

        raise AssertionError(
            "Expected ValueError"
        )
