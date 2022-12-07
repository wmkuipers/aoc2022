class Directory:
    def __init__(self):
        self.child_dirs = []
        self.files = {}

    def set_parent_directory(self, parent):
        self.parent = parent

    def add_child_directory(self, child_dir):
        self.child_dirs.append(child_dir)

    @property
    def total_size(self):
        files_size = sum([int(size) for file, size in self.files.items()])
        directories_size = sum([directory.total_size for directory in self.child_dirs])
        return files_size + directories_size