import pickle
# имя файла, в котором мы сохраним объект
shoplistfile = 'shoplist.data'
# список покупок
shoplist = ['яблоки', 'манго', 'морковь']
# Запись в файл
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f) # помещаем объект в файл
f.close()
del shoplist # уничтожаем переменную shoplist

with open(shoplistfile, 'rb') as f:
    shoplist = pickle.load(f,)

print(shoplist)