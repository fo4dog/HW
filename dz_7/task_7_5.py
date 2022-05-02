import os
import sys
import json

file_sizes = {

}  # Словарь с размерами и типами файлов


def stats(cur_dir):
    """
    На вход подается расположение дериктории, на выходе получается словарь file_sizes
    вида: {10: (x, ['.py']) ...}  где х - кол-во файлов
    """

    for file in os.scandir(cur_dir):
        if os.path.isfile(file):
            size = 10 ** len(str(os.stat(file).st_size))  # размер файла
            file_extend = os.path.splitext(file)[-1]
            count, extends = file_sizes.get(size, (0, set()))
            extends.add(file_extend)
            count += 1
            file_sizes[size] = (count, extends)
        else:
            next_dir = os.path.join(cur_dir, file)
            stats(next_dir)


# TODO добавить вывод в json файл
if __name__ == "__main__":
    if len(sys.argv) == 2:
        BASE_DIR = sys.argv[1]
        json_dir = sys.argv[1] + "\stats.json"
        stats(BASE_DIR)
        to_json = {k: (file_sizes[k][0], list(file_sizes[k][1])) for k in file_sizes}
        with open(json_dir, 'w') as f:
            print(to_json)
            f.write(json.dumps(to_json))
    else:
        BASE_DIR = os.getcwd()
        stats(BASE_DIR)
        to_json = {k: (file_sizes[k][0], list(file_sizes[k][1])) for k in file_sizes}
        with open('stats.json', 'w') as f:
            print(to_json)
            f.write(json.dumps(to_json))
