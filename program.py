import re
import os

ANSI_ESCAPE_CHARACTERS = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

def main():
    os.system('gcloud --help > help.txt')
    with open('help.txt') as file:
        help_line = file.readlines()
        for i in help_line:
            with open('clean_help.txt', 'a') as clean_file:
                clean_file.writelines(ANSI_ESCAPE_CHARACTERS.sub('', i))

if __name__ == "__main__":
    main()