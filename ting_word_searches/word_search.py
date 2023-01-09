def get_ocurrencies(word, data, content=False):
    all_lines = [
        {"linha": index + 1}
        if not content
        else {"linha": index + 1, "conteudo": line}
        for index, line in enumerate(data)
        if word.lower() in line.lower()
    ]
    return all_lines


def find_words(word, all_data, content=False):
    words_found = []
    for data in all_data:
        ocurrencies = {
            "palavra": word,
            "arquivo": data["nome_do_arquivo"],
            "ocorrencias": get_ocurrencies(
                word, data["linhas_do_arquivo"], content
            ),
        }
        words_found.append(ocurrencies)

    return words_found


def exists_word(word, instance):
    if not word:
        return []
    all_data = [instance.search(index) for index in range(0, len(instance))]
    word_ocurrencies = find_words(word, all_data, content=False)
    filtered_ocurrencies = [
        ocurrency
        for ocurrency in word_ocurrencies
        if len(ocurrency["ocorrencias"]) > 0
    ]
    return filtered_ocurrencies


def search_by_word(word, instance):
    if not word:
        return []
    all_data = [instance.search(index) for index in range(0, len(instance))]
    word_ocurrencies = find_words(word, all_data, content=True)
    filtered_ocurrencies = [
        ocurrency
        for ocurrency in word_ocurrencies
        if len(ocurrency["ocorrencias"]) > 0
    ]
    return filtered_ocurrencies
