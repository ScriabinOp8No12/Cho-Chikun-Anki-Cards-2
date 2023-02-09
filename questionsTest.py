#  take the puzzles that have pattern at top that aren't getting caught by pytessearct and check pytessearct output for
#  those specific ones are

import pytesseract
import cv2
import os

path_to_folder = r'C:\Users\nharw\PycharmProjects\pdf2AnkiVersion2\baseImages\imagesPreProcessing'
sorted_images = os.listdir(path_to_folder)
sorted_images.sort(key=lambda f: int(''.join(filter(str.isdigit, f)))) # copied this line (Python doesn't sort properly)

pages_with_pattern_at_top = []
substring = "Pattern"

img90 = rf'C:\Users\nharw\PycharmProjects\pdf2AnkiVersion2\baseImages\imagesPreProcessing\90.jpg' # Pastern at top of page
img98 = rf'C:\Users\nharw\PycharmProjects\pdf2AnkiVersion2\baseImages\imagesPreProcessing\98.jpg' # Detects Pattern24 at top when scanning whole page
img116 = rf'C:\Users\nharw\PycharmProjects\pdf2AnkiVersion2\baseImages\imagesPreProcessing\116.jpg'

path_to_img = rf'C:\Users\nharw\PycharmProjects\pdf2AnkiVersion2\baseImages\imagesPreProcessing\98.jpg'
img = cv2.imread(path_to_img, 0)  # loads in mode "0", which is grayscale, use "1" for color and "-1" for unchanged
cropped_top_of_page = img[0:120, 168:542]  # crop is in format img[y:y+h, x:x+w]
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
result = pytesseract.image_to_string(cropped_top_of_page)
# result = pytesseract.image_to_string(img)
print(result)
# result = pytesseract.image_to_string(cropped_top_of_page)
# if substring in result:
#     pages_with_pattern_at_top.append(each_image)