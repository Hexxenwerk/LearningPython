import files
import translate


def main() -> int:
    path = "."
    selector = "*.txt"
    file_list = files.get_files_in_dir(path, selector)

    if len(file_list) < 1:
        print(f"No files found under {path} for {selector}")
        exit(0)

    for f in file_list:
        content = files.read_file_content(f, 5)
        for line in content:
            print(translate.translate_de(line))

    return 0


exit(main())
