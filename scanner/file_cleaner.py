import os

class File_Cleaner:
    def delete_files(self, files):
        deleted_files = []
        for file in files:
            try:
                os.remove(file)
                deleted_files.append(file)
            except Exception as e:
                print(f"Failed to delete {file}: {e}")
        return deleted_files