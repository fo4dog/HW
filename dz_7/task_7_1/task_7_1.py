import os

def main():
    folder_struct = {
        "my_project":
            {
                "settings": [],
                "mainapp": [],
                "adminapp": [],
                "authapp": []
            },

    }
    for dir, folders in folder_struct.items():
        if not os.path.isdir(dir):
            os.mkdir(dir)
        os.chdir(dir)
        for folder in folders:
            if not os.path.isdir(folder):
                os.mkdir(folder)
        os.chdir("..")


if __name__ == "__main__":
    main()