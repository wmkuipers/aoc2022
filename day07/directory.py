class Directory:
    def __init__(self, dirname):
        self.child_dirs = []
        self.files = {}
        self.dirname = dirname

    def add_child_directory(self, child_dir):
        self.child_dirs.append(child_dir)

    def print_dir(self, indent):
        print(" "*(indent+2) + "- " + self.dirname + " (dir)")
        for dir in self.child_dirs:
            dir.print_dir(indent+2)
        for file, size in self.files.items():
            print(" "*(indent+3) + " " + file + " (file, size=" + size+")")



    @property
    def total_size(self):
        files_size = sum([int(size) for file, size in self.files.items()])
        directories_size = sum([directory.total_size for directory in self.child_dirs])
        return files_size + directories_size

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

def parse_ls(current_dir_path, args, directories):
    if current_dir_path not in directories:
        directories.update({current_dir_path: Directory(current_dir_path)})

    current_dir = directories[current_dir_path]
    for inode in args[3:].split('\n'):
        # print(f"Inode: {inode}")
        if inode.startswith('dir'):
            subdir_name = inode.split(" ")[1]
            if current_dir_path == "/":
                full_subdir_path = f"/{subdir_name}"
            else:
                full_subdir_path = f"{current_dir_path}/{subdir_name}"
            if full_subdir_path not in directories:
                #Add new child directory to big book of directories
                directories.update({
                    full_subdir_path: Directory(subdir_name)
                })
                #Register new directory as child of current
                directories[current_dir_path].add_child_directory(
                    directories[full_subdir_path]
                )
        else:
            filesize, filename = inode.split(" ")
            if filename not in current_dir.files:
                current_dir.files.update({filename: filesize})
       