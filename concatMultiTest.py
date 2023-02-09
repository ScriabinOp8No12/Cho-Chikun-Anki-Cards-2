import pytesseract
import cv2
import os
import numpy as np

path_to_folder = r'C:\Users\nharw\PycharmProjects\pdf2AnkiVersion2\concatMultiTestImages'
sorted_images = os.listdir(path_to_folder)
sorted_images.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

substring = "Pattern"
pastern = "Pastern"   # added this string here for one puzzle being messed up in PDF
answer_counter = 1  # start at 1 because I want my image names to start at 1 and not 0

for each_image in sorted_images:
    path_to_img = rf'C:\Users\nharw\PycharmProjects\pdf2AnkiVersion2\concatMultiTestImages\{each_image}'
    img = cv2.imread(path_to_img, 0)
    cropped_top_of_page = img[0:120, 168:542]  # img[y:y+h, x:x+w]  # changes to 0:120
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    result = pytesseract.image_to_string(cropped_top_of_page)

    if substring in result or pastern in result:
        cv2.imwrite(rf'C:\Users\nharw\PycharmProjects\pdf2AnkiVersion2\concatMultiTestOutput\{answer_counter}.jpg', img)
        answer_counter += 1

    else:
        cv2.imwrite(rf'C:\Users\nharw\PycharmProjects\pdf2AnkiVersion2\concatMultiTestOutput\{answer_counter}.jpg', img)
        prev_image = cv2.imread(
            rf'C:\Users\nharw\PycharmProjects\pdf2AnkiVersion2\concatMultiTestOutput\{answer_counter-1}.jpg', 0) # "-1" is important
        curr_image = cv2.imread(rf'C:\Users\nharw\PycharmProjects\pdf2AnkiVersion2\concatMultiTestOutput\{answer_counter}.jpg', 0)

        combined_solution = np.vstack((prev_image, curr_image))  # vertically concatenates the 2 images

        file_name = f"{answer_counter-1}.jpg"  # saves it as the first answer's file name to stay consistent with question numbers
        cv2.imwrite(rf'C:\Users\nharw\PycharmProjects\pdf2AnkiVersion2\concatMultiTestOutput\{file_name}', combined_solution)


# Concatenating MORE THAN 2 images vertically.  For each page after the first page that has pattern at top, concat it to
# the page before,  trick is to figure out how to rename it to the first image.  JUST DO IT BY LOWEST NUMBER ON THE IMAGE?

# Basically after combining 2 images, it looks at the 3rd image, and if it's also an answer page (no "Pattern" at top)
# then concat this page to the longer previous page.  Rename to the LOWEST page number image (first one always)