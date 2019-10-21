def checkdir(dir, new_folder):
    ### Usage: checkdir('/mnt/drive/FOLDER', 'New Folder')
    ### Checks the dir for a particular folder and if it does not exist, create it
    folder = os.path.join(dir, new_folder)
    try:
        if not os.path.isdir(folder):
            os.mkdir(folder)
            return True
    except:
        return False
