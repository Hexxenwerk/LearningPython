import files
import translate


def main() -> int:
    path: str = input("Gib den Pfad ein, der nach Dateien durchsucht werden soll ['.']: ")
    selector: str = input("Gib einen Selektor an oder Enter für [*.txt]: ")
    line_count = int(input("Gib die Anzahl der zu übersetzenden Zeilen ein: "))
    file_list = files.get_files_in_dir(path, selector)

    if len(file_list) < 1:
        print(f"No files found under {path} for {selector}")
        exit(0)

    for f in file_list:
        content = files.read_file_content(f, line_count)
        for line in content:
            print(translate.translate_de(line))

    return 0


exit(main())
