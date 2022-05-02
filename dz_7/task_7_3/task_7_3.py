import os
import sys
import shutil
if __name__ == "__main__":
    for dirs in os.listdir(os.getcwd()):
        if os.path.isdir(dirs):
            if dirs == 'my_project':
                os.chdir(dirs)
                if not os.path.isdir('templates'):
                    os.mkdir('templates')
                path = os.path.abspath('templates')
                for i in os.walk(os.getcwd()):
                    if len(i[1]) != 0 and i[1][0] == 'templates':
                        os.chdir(i[0].split('\\')[-1])
                        os.chdir('templates')

                        print(os.getcwd())
                        shutil.copytree(os.getcwd(), path, dirs_exist_ok=True)
                        os.chdir('..')
                        os.chdir('..')

