from src.pre_built.counter import count_ocurrences


def test_counter():
    # Caminho do arquivo de teste
    test_file_path = "data/test_jobs.csv"

    # Palavra a ser contabilizada
    test_word = "Python"

    # Conteúdo do arquivo de teste
    test_data = (
        "Python is a programming language. "
        "javascript is another language. "
        "Python, JavaScript, python."
    )

    # Escreva o conteúdo no arquivo de teste
    with open(test_file_path, "w") as test_file:
        test_file.write(test_data)

    # Chame a função count_ocurrences
    result = count_ocurrences(test_file_path, test_word)

    # Verifique se a contagem está correta
    assert result == 3

    # Teste de case-insensitivity
    result_case_insensitive = count_ocurrences(test_file_path, "python")
    assert result_case_insensitive == 3

    # Teste com palavra que não existe
    result_nonexistent_word = count_ocurrences(test_file_path, "Java")
    assert result_nonexistent_word == 0

    # Limpeza do arquivo de teste
    import os

    os.remove(test_file_path)
