import sys


def txt_importer(path_file):
    try:
        is_txt = path_file.endswith(".txt")
        if not is_txt:
            sys.stderr.write("Formato inválido\n")
        with open(path_file, "r") as file:
            content = file.read().splitlines()
            return content
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
