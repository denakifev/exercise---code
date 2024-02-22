import time
import os

backup_list = ['/Users/denisakifev/desktop/pictures']

target_dir = '/Users/denisakifev/documents'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = "zip -qr {0} {1}".format(target, ' '.join(backup_list))
if os.system(zip_command)==0:
    print('Резервная копия создалась успешно')
else: print('Создание резервной копии не удалось')