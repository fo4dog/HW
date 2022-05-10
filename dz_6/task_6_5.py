import sys
import task_6_3
import json


if __name__ == '__main__':
    dict_out = task_6_3.prepare_dataset(sys.argv[1], sys.argv[2])
    with open(sys.argv[3], 'w', encoding='utf-8') as fw:
        json.dump(dict_out, fw, ensure_ascii=False, indent=2)