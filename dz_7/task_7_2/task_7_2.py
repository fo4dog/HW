import yaml
import os

def config_struct(struct):

    for folders in struct:

        if type(folders) != list and type(folders) != dict:
            if len(folders.split('.')) == 2:
                file = open(folders, 'w')
                file.close()
            else:
                if not os.path.isdir(folders):
                    os.mkdir(folders)
        else:
            if str(folders.values()) != 'dict_values([None])': # проверка на то что папка не пуста
                for dir, folder in folders.items():
                    if not os.path.isdir(dir):
                        os.mkdir(dir)
                    os.chdir(dir)
                    config_struct(folder)
                    os.chdir('..')

if __name__ == "__main__":
    with open('config.yaml') as config:
        read_config = yaml.load(config, Loader=yaml.FullLoader)
    read_config_list = []
    read_config_list.append(read_config)
    config_struct(read_config_list)
# TODO Если структура заканчивается папкой