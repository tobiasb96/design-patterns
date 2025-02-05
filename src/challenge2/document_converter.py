"""
Challenge 2: Document Converter System

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


class DocumentConverter:
    def __init__(self):
        self.supported_conversions = ['pdf_to_txt', 'docx_to_txt']

    def convert_document(self, source_path: str, target_path: str):
        # Extract file extensions
        source_ext = source_path.split('.')[-1].lower()
        target_ext = target_path.split('.')[-1].lower()
        conversion_type = f"{source_ext}_to_{target_ext}"

        if conversion_type not in self.supported_conversions:
            raise ValueError(f"Unsupported conversion: {conversion_type}")

        # Large if-else block that handles different conversion types
        if conversion_type == 'pdf_to_txt':
            print(f"Reading PDF file: {source_path}")
            # Simulate PDF reading
            content = f"PDF content from {source_path}"
            
            print("Converting PDF to text...")
            # Simulate conversion
            converted_text = content.upper()
            
            print(f"Writing text to: {target_path}")
            with open(target_path, 'w') as f:
                f.write(converted_text)

        elif conversion_type == 'docx_to_txt':
            print(f"Reading DOCX file: {source_path}")
            # Simulate DOCX reading
            content = f"DOCX content from {source_path}"
            
            print("Converting DOCX to text...")
            # Different conversion logic for DOCX
            converted_text = content.lower()
            
            print(f"Writing text to: {target_path}")
            with open(target_path, 'w') as f:
                f.write(converted_text)

        print("Conversion completed!")
        return True


# Example usage of the current implementation:
if __name__ == "__main__":
    converter = DocumentConverter()
    
    # Convert a PDF file
    converter.convert_document("sample.pdf", "output.txt")
    
    # Convert a DOCX file
    converter.convert_document("sample.docx", "output.txt")
    
    # This will raise an error
    try:
        converter.convert_document("sample.jpg", "output.txt")
    except ValueError as e:
        print(f"Error: {e}")

# Problems with this implementation:
# 1. Single class handling all conversion types (violates SRP)
# 2. Adding new conversion types requires modifying this class (violates OCP)
# 3. Tight coupling between conversion logic and file handling
# 4. Duplicate code for file operations
# 5. Hard to test individual conversion types
# 6. No clear extension points for new formats

# Implement your refactored solution below using the Factory pattern 