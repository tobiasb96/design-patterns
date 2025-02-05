"""Challenge 2: Document Converter System.

Your Task:
---------
Refactor this poorly implemented document converter system to use the Factory pattern.
The current implementation violates Open-Closed Principle and has tight coupling.

Requirements for the refactored solution:
1. Use Factory pattern to create appropriate converters
2. Make it easy to add new converter types without modifying existing code
3. Each converter should focus only on its conversion logic (SRP)
4. Provide a clean interface for client code to use
"""
import contextlib
from abc import ABC, abstractmethod


class DocumentConverter:
    def __init__(self) -> None:
        self.supported_conversions = ["pdf_to_txt", "docx_to_txt"]

    def convert_document(self, source_path: str, target_path: str) -> bool:
        # Extract file extensions
        source_ext = source_path.split(".")[-1].lower()
        target_ext = target_path.split(".")[-1].lower()
        conversion_type = f"{source_ext}_to_{target_ext}"

        if conversion_type not in self.supported_conversions:
            msg = f"Unsupported conversion: {conversion_type}"
            raise ValueError(msg)

        # Large if-else block that handles different conversion types
        if conversion_type == "pdf_to_txt":
            # Simulate PDF reading
            content = f"PDF content from {source_path}"

            # Simulate conversion
            converted_text = content.upper()

            with open(target_path, "w") as f:
                f.write(converted_text)

        elif conversion_type == "docx_to_txt":
            # Simulate DOCX reading
            content = f"DOCX content from {source_path}"

            # Different conversion logic for DOCX
            converted_text = content.lower()

            with open(target_path, "w") as f:
                f.write(converted_text)

        return True


# Example usage of the current implementation:
if __name__ == "__main__":
    converter = DocumentConverter()

    # Convert a PDF file
    converter.convert_document("sample.pdf", "output.txt")

    # Convert a DOCX file
    converter.convert_document("sample.docx", "output.txt")

    # This will raise an error
    with contextlib.suppress(ValueError):
        converter.convert_document("sample.jpg", "output.txt")

# Problems with this implementation:
# 1. Single class handling all conversion types (violates SRP)
# 2. Adding new conversion types requires modifying this class (violates OCP)
# 3. Tight coupling between conversion logic and file handling
# 4. Duplicate code for file operations
# 5. Hard to test individual conversion types
# 6. No clear extension points for new formats

# Implement your refactored solution below using the Factory pattern


class DocumentConverter(ABC):
    def __init__(self, source_path: str, target_path: str):
        self.source_path = source_path
        self.target_path = target_path

    @abstractmethod
    def convert(self):
        pass


class PDFDocumentConverter(DocumentConverter):
    def __init__(self, source_path: str, target_path: str):
        super().__init__(source_path, target_path)

    def convert(self):
        content = f"PDF content from {self.source_path}"
        converted_text = content.upper()
        with open(self.target_path, "w") as f:
            f.write(converted_text)


class WordDocumentConverter(DocumentConverter):
    def __init__(self, source_path: str, target_path: str):
        super().__init__(source_path, target_path)

    def convert(self):
        content = f"DOCX content from {self.source_path}"
        converted_text = content.lower()  # different conversion
        with open(self.target_path, "w") as f:
            f.write(converted_text)


class ConverterFactory:

    # This could also by a dynamics registration for supporting changes without having to change
    # the code - but as the conversions do not change to often, this should be fine
    CONVERSION_MAPPING = {
        "pdf_to_txt": PDFDocumentConverter,
        "docx_to_txt": WordDocumentConverter,
    }

    def __init__(self):
        pass

    def create(self, source_path: str, target_path: str):
        source_ext = source_path.split(".")[-1].lower()
        target_ext = target_path.split(".")[-1].lower()
        conversion_type = f"{source_ext}_to_{target_ext}"
        converter_class = self.CONVERSION_MAPPING.get(conversion_type, None)

        if not converter:
            raise ValueError("Not supported")

        return converter_class(source_path=source_path, target_path=target_path)



class ConverterEngine:
    def __init__(self):
        pass

    @staticmethod
    def handle_conversion(source_path: str, target_path: str):
        converter = ConverterFactory().create(source_path, target_path)
        converter.convert()


if __name__ == "__main__":
    # Convert a PDF file
    ConverterEngine.handle_conversion("sample.pdf", "output.txt")

    # Convert a DOCX file
    ConverterEngine.handle_conversion("sample.docx", "output.txt")

    # Handle unsupported conversion gracefully
    with contextlib.suppress(ValueError):
        ConverterEngine.handle_conversion("sample.jpg", "output.txt")