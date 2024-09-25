
from docx import Document

def create_docs():
    doc = Document()
    doc.add_paragraph("Hello, World!")
    doc.save("output.docx")