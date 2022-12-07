from pprint import pprint as print
from directory import Directory

directories = {}       #directories are stored with key being full path
TOTAL_DISK_SIZE = 70000000
MIN_FREE_SIZE = 30000000

def input_reader(filename):
    raw = [line.strip() for line in open(filename).read().split('$') if line != '']
    return raw

def parse_cd(cwd, arg):
    arg = arg[3:]
    if arg == '/':
        return '/'
    if arg == '..':
        return '/' + '/'.join(cwd.split("/")[1:-1])
    
    if cwd != '/':
        return f"{cwd}/{arg}"
    else:
        return f"/{arg}"

def parse_ls(current_directory, args):
    if current_directory not in directories:
        directories.update({current_directory: Directory()})

    current_dir = directories[current_directory]
    for inode in args[3:].split('\n'):
        # print(f"Inode: {inode}")
        if inode.startswith('dir'):
            subdir_name = inode.split(" ")[1]
            if current_directory == "/":
                full_subdir_name = f"/{subdir_name}"
            else:
                full_subdir_name = f"{current_directory}/{subdir_name}"
            if full_subdir_name not in directories:
                #Add new child directory to big book of directories
                directories.update({
                    full_subdir_name: Directory()
                })
                #Register new directory as child of current
                directories[current_directory].add_child_directory(
                    directories[full_subdir_name]
                )
        else:
            filesize, filename = inode.split(" ")
            if filename not in current_dir.files:
                current_dir.files.update({filename: filesize})
       
def main(test=True):
    data = input_reader("test.txt" if test else "input.txt")

    cwd = ''
    for action in data:
        if action.startswith("cd"):
            cwd = parse_cd(cwd, action)
        elif action.startswith("ls"):
            parse_ls(cwd, action)


    part_one = sum([D.total_size for d, D in directories.items()
                                 if D.total_size < 100000])
    print(f"Part one: {part_one}")

    free_size = TOTAL_DISK_SIZE - directories['/'].total_size
    need_to_free = MIN_FREE_SIZE - free_size
    print(f"Current free size: {free_size}, need to free up: {need_to_free}")

    delete_candidates = {D.total_size: D    for dirname, D in directories.items() 
                                            if D.total_size > need_to_free}
    smallest_candidate = delete_candidates[min(delete_candidates)]
    print(smallest_candidate.total_size)


if __name__ == '__main__':
    main(test=False)