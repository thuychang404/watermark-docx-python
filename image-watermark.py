from spire.doc import *
from spire.doc.common import *

input_path_file = "./input.docx"
output_path_file = "./output-image-watermark.docx"
img_watermark_file = "./logo.png"

def add_img_watermark_to_docx(input_file, image_file, output_file):
    # Create an object of the Document class
    document = Document()
    # Load a Word document
    document.LoadFromFile(input_file)

    # Create an object of the PictureWatermark class
    imgWatermark = PictureWatermark()
    # Set the watermark image
    imgWatermark.SetPicture(image_file)
    # Set image scaling percent
    imgWatermark.Scaling = 100
    # Disable washout property
    imgWatermark.IsWashout = False

    # Set the image watermark as the watermark of the document
    document.Watermark = imgWatermark

    # Save the resulting document
    document.SaveToFile(output_file, FileFormat.Docx2016)

    # Close the Document object
    document.Close()

add_img_watermark_to_docx(input_path_file, img_watermark_file, output_path_file)
