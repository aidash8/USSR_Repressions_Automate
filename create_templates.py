import pandas as pd
from docx import Document


def create_template(row, document):

    # Add name
    document.add_paragraph(row['name'])
    # Add Age
    document.add_paragraph(row['age'])
    # Add birth info
    document.add_paragraph(row['birth_info'])
    # Add profession
    document.add_paragraph(row['профессия / место работы'])
    # Add demise info
    document.add_paragraph(row['demise_info']) 

    document.add_page_break()


def create_docs(name: str, df: pd.DataFrame):
    
    doc = Document()

    for _,row in df.iterrows():
        create_template(row, doc)

    doc.save(f"{name}.docx")