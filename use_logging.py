import os, logging 

try:
    f = open('test.log', 'w') 
    print('Файл логирования создан')
except: 
    print('Случилась ошибка')

f.close()

logging_file = os.path.join(os.getenv('HOME'), 'test.log')

print("Сохраняем лог в", logging_file)

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s : %(levelname)s : %(message)s', 
    filename = 'test.log',
    filemode = 'w',
)

logging.debug("Начало программы")
logging.info("Какие-то действия")
logging.warning("Программа умирает")