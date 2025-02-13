"""Test cases for Challenge 2: Document Converter Refactoring.

These tests should pass both before and after your refactoring,
ensuring that the functionality remains the same while the code structure improves.
"""

import os

import pytest

from design_patterns.src.challenge2.document_converter import DocumentConverter


@pytest.fixture
def converter():
    return DocumentConverter()


@pytest.fixture
def cleanup_output():
    # Setup
    if os.path.exists("output.txt"):
        os.remove("output.txt")
    yield
    # Teardown
    if os.path.exists("output.txt"):
        os.remove("output.txt")


def test_pdf_to_txt_conversion(converter, cleanup_output) -> None:
    # Test PDF to TXT conversion
    converter.convert_document("sample.pdf", "output.txt")

    # Check if output file was created
    assert os.path.exists("output.txt")

    # Check content
    with open("output.txt") as f:
        content = f.read()
        assert "PDF CONTENT FROM" in content
        assert content.isupper()


def test_docx_to_txt_conversion(converter, cleanup_output) -> None:
    # Test DOCX to TXT conversion
    converter.convert_document("sample.docx", "output.txt")

    # Check if output file was created
    assert os.path.exists("output.txt")

    # Check content
    with open("output.txt") as f:
        content = f.read()
        assert "docx content from" in content
        assert content.islower()


def test_unsupported_conversion(converter) -> None:
    # Test unsupported conversion type
    with pytest.raises(ValueError) as exc_info:
        converter.convert_document("sample.jpg", "output.txt")
    assert "Unsupported conversion" in str(exc_info.value)


def test_supported_conversions_list(converter) -> None:
    # Test that supported conversions are correctly listed
    assert "pdf_to_txt" in converter.supported_conversions
    assert "docx_to_txt" in converter.supported_conversions


# Additional tests to consider implementing after refactoring:
# 1. Test factory creates correct converter types
# 2. Test each converter type in isolation
# 3. Test error handling for invalid input files
# 4. Test adding a new converter type
# 5. Test converter interface consistency
