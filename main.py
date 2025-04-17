from scanner.file_scanner import FileScanner

if __name__ == '__main__':
    directory = input("Enter the directory to scan: ")

    scanner = FileScanner(directory)
    junk_files = scanner.find_junk_files()

    if junk_files:
        print("\nJunk Files Found")
        for file in junk_files:
            print(file)

    else:
        print("\nNo Junk Files Found")