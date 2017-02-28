from os import listdir, rename, getcwd

def rename_files():
    path = getcwd() + "/prank"
    files = listdir(path)

    for file in files:
        oldFile = path + '/' + file
        newName = path + '/' + file.translate(None, '0123456789')
        rename(oldFile, newName)


rename_files()