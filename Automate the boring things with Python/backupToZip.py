import zipfile, os

def backupToZip(folder):
    # Back up the entire contents of "folder" into a ZIP file

    folder = os.path.abspath(folder) # make sure folder is absolute

    # Figure out the filename this code should use based on what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'

        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Create the ZIP file.
    print(f'Creating {zipFilename}...')
    backupToZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder
    for foldername, _, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        # Add the current folder to the ZIP file
        backupToZip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupToZip.write(os.path.join(foldername, filename))
    backupToZip.close()

    print('Done.')


folder_path = '/home/eliasderby/Desktop/python/automate exercise'

backupToZip(folder_path)