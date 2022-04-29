import os
import sys

file_sizes = {

    }


def stats(cur_dir):

    for file in os.scandir(cur_dir):
        if os.path.isfile(file):
            f_size = os.stat(file).st_size
            size = 10 ** (len(str(f_size)))

            count = file_sizes.get(size)
            if count == None:
                count = 1
            else:
                count += 1
            file_sizes[size] = count
        else:
            next_dir = os.path.join(cur_dir, file)
            stats(next_dir)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        BASE_DIR = os.path.dirname(os.path.abspath(sys.argv[1]))
    else:
        BASE_DIR = os.getcwd()
    stats(BASE_DIR)
    print(file_sizes)
