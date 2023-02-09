# 1. I converted the Cho Chikun PDF v2 into jpg images at the highest resolution using Adobe's online tool (link below)
#  https://acrobat.adobe.com/link/acrobat/pdf-to-image/?x_api_client_id=adobe_com&x_api_client_location=pdf_to_image&dropinId=verb-pdf-to-image
# 2. I manually deleted the intro pages and other pages (~15 total) that didn't have a puzzle or answer on it
# 3. Then using the python code below, I renamed each puzzle to be 1.jpg 2.jpg 3.jpg etc.

import os

path_to_folder = r'C:\Users\nharw\PycharmProjects\pdf2AnkiVersion2\baseImages\imagesPreProcessing'
images = os.listdir(path_to_folder)
images.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))  # Python doesn't sort properly so this line is needed

image_number = 1

for each_image in images:
    os.rename(os.path.join(path_to_folder, each_image), os.path.join(path_to_folder, str(image_number) + '.jpg'))
    image_number += 1

