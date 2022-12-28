from pathlib import Path



def get_help_text(file_name, command=None):
    if command:
        cmd = f'gcloud {command} --help > {file_name}.txt'
    else:
        cmd = f'gcloud --help > {file_name}.txt'
    print(cmd)



def main():
    get_help_text('help')

if __name__ == "__main__":
    main()