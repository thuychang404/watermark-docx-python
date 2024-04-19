from spire.doc import *
from spire.doc.common import *

input_path_file = "./input.docx"
output_path_file = "./output-text-watermark.docx"
watermark_text = "NHOM 15"

def add_text_watermark_to_docx(input_file, text, output_file):
    # Create an object of the Document class
    document = Document()
    # Load a Word document
    document.LoadFromFile(input_file)

    # Create an object of the TextWatermark class
    txtWatermark = TextWatermark()
    # Set watermark text, font size, text color and layout
    txtWatermark.Text = text
    txtWatermark.FontSize = 95
    txtWatermark.Color = Color.get_Red()
    txtWatermark.Layout = WatermarkLayout.Diagonal

    # Set the text watermark as the watermark of the document
    document.Watermark = txtWatermark
    

    # Save the resulting document
    document.SaveToFile(output_file, FileFormat.Docx2016)

    # Close the Document object
    document.Close()

add_text_watermark_to_docx(input_path_file, watermark_text, output_path_file)