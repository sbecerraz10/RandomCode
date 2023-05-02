import markdown
from docx import Document

def markdown_to_word(markdown_file, output_file):
    # Read the markdown file
    with open(markdown_file, 'r') as f:
        markdown_text = f.read()
    
    # Convert markdown to HTML
    html_text = markdown.markdown(markdown_text)
    
    # Create a new Word document
    doc = Document()
    
    # Add each paragraph from the HTML as a new paragraph in the Word document
    for paragraph in html_text.split('\n'):
        doc.add_paragraph(paragraph)
    
    # Save the Word document
    doc.save(output_file)
