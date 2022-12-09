# from pprint import pprint as print
from directory import Directory, parse_cd, parse_ls

directories = {}       #directories are stored with key being full path
TOTAL_DISK_SIZE = 70000000
MIN_FREE_SIZE = 30000000

def input_reader(filename):
    raw = [line.strip() for line in open(filename).read().split('$') if line != '']
    return raw

def main(test=True):
    data = input_reader("test.txt" if test else "input.txt")

    cwd = ''
    for action in data:
        if action.startswith("cd"):
            cwd = parse_cd(cwd, action)
        elif action.startswith("ls"):
            parse_ls(cwd, action, directories)


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

    print(directories["/"].print_dir(1))



if __name__ == '__main__':
    main(test=True)