import sys
import os
import zipfile
import time

#list of directories and files to backup
src = '/home/out0fbounds/Pictures/'

#Dirctory where the backup will be stored
dest = '/home/out0fbounds/backup/'

filename = dest+time.strftime('%Y-%m-%d|%H:%M:%S')+'.zip'

zip_file = zipfile.ZipFile(filename,mode='w')

for x in os.listdir(src):
	zip_file.write(src+x, os.path.basename(src+x), compress_type = zipfile.ZIP_DEFLATED)
zip_file.close()
