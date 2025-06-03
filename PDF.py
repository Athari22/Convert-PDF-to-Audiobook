from fpdf import FPDF

def text_to_pdf(text, output_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    # Add text line-by-line
    for line in text.split('\n'):
        pdf.multi_cell(0, 10, line)

    pdf.output(output_file)
    print(f"✅ PDF saved as {output_file}")

# Example text
sample_text = """This is a test document.
We are using Azure Text-to-Speech to convert this PDF into an audiobook.
Enjoy your listening experience!
"""

# Convert to PDF
text_to_pdf(sample_text, "book.pdf")
