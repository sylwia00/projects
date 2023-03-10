import os
from datetime import datetime

date = datetime.today().strftime('%Y-%m-%d')

backup_path = '/home/sylwia/backups/{}'.format(date)

folders_paths = {
    'flaga': '/var/www',
    '.ssh': '/home/sylwia'
}

files_paths = { 
    'flaga.service': '/etc/systemd/system',
    'programowanie-python.online': '/etc/nginx/sites-available',
    'backup_script.py': '/home/sylwia'
}

os.system('mkdir {}'.format(backup_path))

for name, path in folders_paths.items():
    folder_source = path + '/' + name
    dest = backup_path
    os.system('cp -r {} {}'.format(folder_source, dest))
    print(folder_source)
    print(dest)
    print()

for name, path in files_paths.items():
    file_source = path + '/' + name
    dest = backup_path
    os.system('cp {} {}'.format(file_source, dest))
    print(file_source)
    print(dest)

os.system('zip -r {} {}'.format(backup_path, backup_path))
