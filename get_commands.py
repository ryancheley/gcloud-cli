def get_commands():
    s = open("help.txt").read()
    commands = []
    lines = s.split("GROUPS")[1].strip().split("\n")
    for i in range(len(lines)):
        lines[i] = lines[i].strip().split("\t")[0]    
    lines = [i for i in lines[1:] if i]
    commands = [lines[index] for index in range(2, len(lines), 2)]    
    commands = [i for i in commands if i != 'COMMANDS']
    for command in commands:
        file_name = f'gcloud/{command}.txt'
        cmd = f'gcloud {command} --help > {file_name}'
        print(cmd)

if __name__ == "__main__":
    get_commands()