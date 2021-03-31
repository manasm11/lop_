import glob
from ocr_test2 import pdf2text
import os
import shutil

def make_directory(dirname):
    try:
        os.mkdir(dirname)
        print ("Successfully created the directory %s " % dirname)
        return dirname
    except OSError:
        print ("Creation of the directory %s failed" % dirname)
        if input('Do you want to delete the existing directory ?')[0] == 'y':
            print('REMOVING !!!')
            shutil.rmtree(dirname)
            make_directory(dirname)
        

dirname = 'texts'
make_directory(dirname)
# print(dirname)

for filename in glob.glob(f"{input('Enter directory of pdfs: ')}/*.pdf"):
    print(f'Converting {filename} to text...')
    try:
        text = pdf2text(filename)
    except:
        open('errors.log', 'a').write(f'Unable to convert {filename}\n')
    new_filename = filename.split('/')[1].replace('pdf', 'txt')
    path = os.path.join(dirname, new_filename)
    print(f'Saving text to {path}...')
    open(path, 'w').write(text)


