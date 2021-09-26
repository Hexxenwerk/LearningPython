import user
import files
import translate


def main() -> int:
    path, selector, line_count = user.cli_input()
    file_list: list = files.get_files_in_dir(path, selector)

    if len(file_list) < 1:
        print(f"No files found under {path} for {selector}")
        exit(0)

    for f in file_list:
        content = files.read_file_content(f, line_count)
        for line in content:
            print(translate.translate(line))

    return 0


exit(main())
