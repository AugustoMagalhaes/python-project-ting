import sys

from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(0, len(instance)):
        if path_file == instance.search(index)["nome_do_arquivo"]:
            return

    content = txt_importer(path_file)

    file_data = {"nome_do_arquivo": path_file,
                 "qtd_linhas": len(content),
                 "linhas_do_arquivo": content}

    sys.stdout.write(str(file_data))
    instance.enqueue(file_data)


def remove(instance):
    try:
        path_file = instance.search(0)["nome_do_arquivo"]
        instance.dequeue()
        sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")
    except IndexError:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
