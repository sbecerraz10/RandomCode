import markdown
from docx import Document
from docx.shared import Inches

def convert_md_to_docx(input_file_path, output_file_path):
    # Read the markdown file
    with open(input_file_path, 'r') as input_file:
        text = input_file.read()

    # Convert markdown to HTML
    html = markdown.markdown(text)

    # Create a new Word document
    doc = Document()

    # Add the converted HTML to the document
    doc.add_paragraph(html)

    # Save the document as a .docx file
    doc.save(output_file_path + '.docx')

