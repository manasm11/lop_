import requests
import os

dirname = 'handouts_2nd_sem'
os.mkdir(dirname)
for url in open('handout.json').readlines():
    #print(url.strip())
    res = requests.get(url.strip())
    open(os.path.join(dirname, url.split('/')[-1].strip()), 'wb').write(res.content)