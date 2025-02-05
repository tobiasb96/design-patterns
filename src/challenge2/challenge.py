"""
Challenge 2: Document Converter System

Requirements:
------------
1. Define an abstraction for a document converter that supports a common conversion interface
2. Implement at least two converters (e.g., PDF-to-TXT and DOCX-to-TXT)
3. Create a central converter engine that instantiates and uses the appropriate converter
   based on the file extension

Hints:
------
- Use a Factory pattern so that adding a new document converter does not require 
  changing the central engine code (OCP)
- Ensure that your converter classes only focus on the conversion logic (SRP)
- The solution should be easily extensible when supporting new file formats

Example Test Cases to Consider:
-----------------------------
1. Test converter factory creates correct converter for each file type
2. Test PDF to TXT conversion
3. Test DOCX to TXT conversion
4. Test handling of unsupported file types
5. Test error handling for invalid/corrupt files
6. Test that adding a new converter type doesn't break existing functionality
"""

# Implement your solution here 