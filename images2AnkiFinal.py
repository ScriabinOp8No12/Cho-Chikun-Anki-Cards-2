import os
import genanki

my_model = genanki.Model(
    24908234,
    'Test Model',
    fields=[

        {'name': 'ImageFront'},
        {'name': 'ImageBack'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{ImageFront}}', # 'qfmt' stands for question format, don't change this
            'afmt': '{{ImageBack}}',
        },
    ],
    css="""
        img {
            max-width: 100%;
            max-height: 100%;
        }
        """
)

my_deck = genanki.Deck(
    65873579,
    'Eric Cho Chikun PDF2')  # this is the name of the deck that you see on Anki

path_to_questions = os.listdir(r"C:\Users\nharw\PycharmProjects\pdf2AnkiVersion2\questionsFinalRenamed")

my_package = genanki.Package(my_deck)
my_package.media_files = []

for x in range(1, len(path_to_questions)+1):  # loop through all images in the questionsFinal folder
    my_note = genanki.Note(
        model=my_model,
        fields=[f'<img src="Puzzle{x}.jpg"/>', f'<img src="Solution{x}.jpg"/>'])

    my_deck.add_note(my_note)
    my_package.media_files.append(rf"C:\Users\nharw\PycharmProjects\pdf2AnkiVersion2\questionsFinalRenamed\Puzzle{x}.jpg")
    my_package.media_files.append(rf"C:\Users\nharw\PycharmProjects\pdf2AnkiVersion2\solutionsFinalRenamed\Solution{x}.jpg")

my_package.write_to_file(r'C:\Users\nharw\PycharmProjects\pdf2AnkiVersion2\ankiOutputFinal\final_1.apkg')
