import os, shutil
from pathlib import Path

curr_dir = Path.cwd()

for foldername, _, filenames in os.walk(curr_dir):
   for filename in filenames:
    ext = filename.split('.')[-1]

    if ext == 'zip':
        try:
        # print(f"moving {curr_dir / filename} to {curr_dir / 'zip'} ")
          shutil.move(curr_dir / filename, curr_dir / 'zip')
        except shutil.Error as err:
           print(err)