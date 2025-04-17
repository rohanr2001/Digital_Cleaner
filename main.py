from scanner.file_scanner import FileScanner
from scanner.file_cleaner import File_Cleaner

if __name__ == '__main__':
    directory = input("Enter the directory to scan: ")

    scanner = FileScanner(directory)
    junk_files = scanner.find_junk_files()

    if junk_files:
        print("\nJunk Files Found")
        for file in junk_files:
            print(file)
        
        confirm = input("\nDo you want to delete these files? (yes/no): ").lower()
        if confirm == 'yes':
            cleaner = File_Cleaner()
            deleted_files = cleaner.delete_files(junk_files)

            print(f"Deleted {len(deleted_files)} files:")
            for file in deleted_files:
                print(file)
        
        else:
            print("No files were deleted.")

    else:
        print("\nNo Junk Files Found")