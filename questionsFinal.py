# 1. For each image, look for the word "Pattern" at the top of the page to determine if there's a question on that page
# 1a. If there is the word "Pattern" at the top, then it must have a question/puzzle right below it.
# 2. Within these images, look for the word "Solution" or "Variation" at y-location 250:350
# 2a. These 2 words are case-sensitive, and only appear in one location (just before the answer/solution begins)
# 3. Split the page from y = 0 to the y-value found in 2.
# 4. Make sure code is correctly cropping the image, ex. if y-location is 290, need to crop at y = 40 (290 minus 250)

import pytesseract
import cv2
import os

path_to_folder = r'C:\Users\nharw\PycharmProjects\pdf2AnkiVersion2\baseImages\imagesPreProcessing'
sorted_images = os.listdir(path_to_folder)
sorted_images.sort(key=lambda f: int(''.join(filter(str.isdigit, f)))) # copied this line (Python doesn't sort properly)

pages_with_pattern_at_top = []
substring = "Pattern"
pastern = "Pastern"  # due to a PDF scan mistake, one puzzle has the word "Pastern" at the top, which won't be detected
                     # if I only use the word "Pattern"

for each_image in sorted_images:
    path_to_img = rf'C:\Users\nharw\PycharmProjects\pdf2AnkiVersion2\baseImages\imagesPreProcessing\{each_image}'
    img = cv2.imread(path_to_img, 0)  # loads in mode "0", which is grayscale, use "1" for color and "-1" for unchanged
    cropped_top_of_page = img[0:120, 168:542]  # crop is in format img[y:y+h, x:x+w] #MODIFIED TO 120!!
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    result = pytesseract.image_to_string(cropped_top_of_page)
    if substring in result or pastern in result:     # using substring of "Pastern" as well
        pages_with_pattern_at_top.append(each_image)

path_to_folder = r'C:\Users\nharw\PycharmProjects\pdf2AnkiVersion2\baseImages\imagesPreProcessing'
sorted_images = os.listdir(path_to_folder)
sorted_images.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

y_values_split_page = []
counter = 1

for each_image in pages_with_pattern_at_top:
    y_offset = 250 # since we crop the image from y = 250, the values start at 0 when y = 250, so we need to add 250 below
    path_to_img = rf'C:\Users\nharw\PycharmProjects\pdf2AnkiVersion2\baseImages\imagesPreProcessing\{each_image}'
    img = cv2.imread(path_to_img, 0)
    cropped_top_of_page = img[y_offset:375, :]  # Detect word "Solution" or "Variation" in y value range 250-375
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    data = pytesseract.image_to_data(cropped_top_of_page, config='--psm 6', output_type=pytesseract.Output.DICT)

    # Iterate through the data and find the "top" value (y-position of where "Solution" or "Variation" is located)
    data_filtered = [(i, x) for i, x in enumerate(data["text"])
                if "Solution" in x or "solution" in x or "sonution" in x or "Variation" in x or "Diagram" in x]
    # sometimes misreads as solution (lower case), or sonution, and some answers start with "diagram", couldn't find
    # pattern at the top of the page for 3 puzzles (one as misspelled in the PDF)
    print(data["text"], each_image)  # bug testing

    assert len(data_filtered) > 0, (data["text"], each_image)   # bug catching line
    assert len(data_filtered) == 1, (data["text"], each_image)  # bug catching line
    i, x = data_filtered.pop()

    name_of_file = 'Puzzle'   # Renaming to Puzzle, because Anki is overriding the cards with the same image name...

    cropped_question = img[0: y_offset+data["top"][i]]
    print(rf'C:\Users\nharw\PycharmProjects\pdf2AnkiVersion2\questionsFinalCopy\{name_of_file}{counter}.jpg')
    cv2.imwrite(rf'C:\Users\nharw\PycharmProjects\pdf2AnkiVersion2\questionsFinalCopy\{name_of_file}{counter}.jpg', cropped_question)
    counter += 1

# 1. Out of 170 images, it properly converted 114 images, but 3 images had puzzles that it didn't grab them, 1 word was
#    detected the as "sonution" instead
# 2. One of 3 errors was a PDF error, "Pastern" at top of page. Other two were puzzles 98.jpg and 116.jpg,
#    I'm not sure why it can't find the word pattern at top, need to investigate by seeing what pytesseract
#    output is for the entire page!
# 3. Many puzzles (especially near the end) have 3-page solutions instead of 2.  The original way of converting
#    2-page solutions won't work because it's 3 pages now, need to plan out a solution before coding

