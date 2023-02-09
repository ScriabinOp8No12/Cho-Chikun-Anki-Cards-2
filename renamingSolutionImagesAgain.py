import os

folder_path = r'C:\Users\nharw\PycharmProjects\pdf2AnkiVersion2\solutionsFinalRenamed'
images = os.listdir(folder_path)
images.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))  # Python doesn't sort properly so this line is needed

for filename in images:
    original_filename = filename

    new_filename = filename.replace('SolutionNumber', 'Solution')
    os.rename(os.path.join(folder_path, original_filename), os.path.join(folder_path, new_filename))

