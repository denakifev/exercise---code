import zipfile
import os 


target_zip = zipfile.ZipFile('backup.zip', 'w')
for root, dirs, files in os.walk('/Users/denisakifev/desktop/pictures'):
    for file in files:
        target_zip.write(os.path.join(root,file))  

target_zip.close() 
os.replace('backup.zip', '/documents')