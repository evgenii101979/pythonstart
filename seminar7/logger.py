def log_result(result):
    with open('file.txt', 'a', encoding='utf-8') as f:
        f.write(result)