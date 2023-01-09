def get_ocurrencies(word, data):
    all_lines = [
        {"linha": index + 1}
        for index, line in enumerate(data)
        if word.lower() in line.lower()
    ]
    return all_lines


def find_word(word, all_data):
    words_found = []
    for data in all_data:
        ocurrencies = {
            "palavra": word,
            "arquivo": data["nome_do_arquivo"],
            "ocorrencias": get_ocurrencies(word, data["linhas_do_arquivo"]),
        }
        words_found.append(ocurrencies)

    return words_found


def exists_word(word, instance):
    print(len(instance))
    all_data = [instance.search(index) for index in range(0, len(instance))]
    word_ocurrencies = find_word(word, all_data)
    return word_ocurrencies


def search_by_word(word, instance):
    """print("uai: ", instance)"""
