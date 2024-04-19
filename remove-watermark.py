from spire.doc import *
from spire.doc.common import *

input_path_file = "./input.docx"
output_path_file = "./output-remove-watermark-2.docx"

def remove_watermark_of_docx(input_file, output_file):

    # Create an object of the Document class
    document = Document()
    # Load a Word document
    document.LoadFromFile(input_file)

    # Set the watermark as null to remove the text or image watermark from the document
    document.Watermark = None

    # Save the resulting document
    document.SaveToFile(output_file, FileFormat.Docx2016)

    # Close the Document object
    document.Close()

remove_watermark_of_docx(input_path_file, output_path_file)