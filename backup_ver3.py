import time
import os

backup_list = ['/Users/denisakifev/desktop/pictures']


target_dir = '/Users/denisakifev/documents'

today = target_dir + os.sep + time.strftime('%Y%m%d')


name = time.strftime('%H%M%S')


comment = input('Введите комментарий --> ')
if len(comment) == 0: # проверяем, введён ли комментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' +
    comment.replace(' ', '_') + '.zip'

  
if not os.path.exists(today):
    os.mkdir(today)
    print('Каталог успешно создан')
    
target = today + os.sep + name + '.zip'
zip_command = "zip -qr {0} {1}".format(target, ' '.join(backup_list))
if os.system(zip_command)==0:
    print('Резервная копия создалась успешно')
else: print('Создание резервной копии не удалось')