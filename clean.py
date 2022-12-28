from pathlib import Path
import re

ANSI_ESCAPE_CHARACTERS = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

def clean_text(file_name, sub_directory=None):
    with open(file_name, 'r') as help_text:
        text = help_text.read()
        clean_text = ANSI_ESCAPE_CHARACTERS.sub('', text)
    with open(file_name, 'w') as help_text:
        help_text.write(clean_text)    

if __name__ == "__main__":
    clean_text('help.txt')
    files = list(Path('gcloud').glob('*.txt'))
    for file in files:
        clean_text(file, sub_directory='gcloud')

    
