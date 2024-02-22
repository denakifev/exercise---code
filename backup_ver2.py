import time
import os

backup_list = ['/Users/denisakifev/desktop/pictures']


target_dir = '/Users/denisakifev/documents'

today = target_dir + os.sep + time.strftime('%Y%m%d')


name = time.strftime('%H%M%S')
if not os.path.exists(today):
    os.mkdir(today)
    print('Каталог успешно создан')
    
target = today + os.sep + name + '.zip'
zip_command = "zip -qr {0} {1}".format(target, ' '.join(backup_list))
if os.system(zip_command)==0:
    print('Резервная копия создалась успешно')
else: print('Создание резервной копии не удалось')