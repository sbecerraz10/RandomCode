import os
import mistune
from docx import Document


def markdown_to_word(input_file_path, output_file_path):
    # Load the Markdown content from the input file
    with open(input_file_path, 'r') as f:
        markdown_content = f.read()

    # Parse the Markdown content to HTML
    html_content = mistune.html(markdown_content)

    # Create a new Word document
    document = Document()

    # Add the paragraphs from the HTML content to the Word document
    for paragraph in html_content.split('<p>'):
        if paragraph.strip():
            p = document.add_paragraph(paragraph.replace('</p>', ''))

    # Save the Word document
    document.save(os.path.splitext(output_file_path)[0] + '.docx')


