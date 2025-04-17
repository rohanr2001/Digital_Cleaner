import os

class FileScanner:
    def __init__(self, directory):
        self.directory = directory
        self.supported_extensions = ['.tmp', '.log', '.bak']

    def find_junk_files(self):
        junk_files = []
        for root, _, files in os.walk(self.directory):
            for file in files:
                if any(file.lower().endswith(ext) for ext in self.supported_extensions):
                    junk_files.append(os.path.join(root, file))
        return junk_files
