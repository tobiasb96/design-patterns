from abc import ABC, abstractmethod
from typing import Dict, List


def get_file_type(file_path: str) -> str:
    file_type = file_path.split(".")[-1]
    if not file_type:
        raise ValueError(f"Could not determine file type for file {file_path}.")
    return file_type


class DocumentToTxtConverter(ABC):
    @abstractmethod
    def file_type(self) -> str:
        pass

    @abstractmethod
    def convert(self, file_path: str):
        pass

    def check_file_type(self, file_path):
        file_type = get_file_type(file_path)
        if not file_type == self.file_type():
            return TypeError(f"Wrong converter for file type {file_type}")


class DocumentToTxtConverterFactory:
    converters: Dict[str, DocumentToTxtConverter]

    def __init__(self, converters: List[DocumentToTxtConverter]):
        self.converters = {converter.file_type(): converter for converter in converters}

    def convert_file_to_txt(self, file_path: str):
        file_type = get_file_type(file_path)
        converter = self.converters.get(file_type)
        if not converter:
            raise TypeError(f"File type {file_type} is not (yet) supported.")

        return converter.convert(file_path)


class PdfToTxtConverter(DocumentToTxtConverter):
    def file_type(self) -> str:
        return "pdf"

    def convert(self, file_path: str):
        self.check_file_type(file_path)

        # some library call to read in a pdf file
        # extract the text from the pdf
        # save it as a .txt file


class DocxToTxtConverter(DocumentToTxtConverter):
    def file_type(self) -> str:
        return "docx"

    def convert(self, file_path: str):
        self.check_file_type(file_path)

        # some library call to read in a docx file
        # extract the text from the docx
        # save it as a .txt file


if __name__ == "__main__":
    converters = [PdfToTxtConverter(), DocxToTxtConverter]
    converter_factory = DocumentToTxtConverterFactory(converters)

    converter_factory.convert_file_to_txt("./pdfs/my_pdf.pdf")
    converter_factory.convert_file_to_txt("./word/my_doc.docx")

