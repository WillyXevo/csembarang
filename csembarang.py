import json
from random import seed
from random import choice
from random import randint
import requests
from logcolor import *
from bs4 import BeautifulSoup

class Csembarang:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    path = "all.json"
    wpath = "whitelist.json"
    data = []
    wdata = []
    lendata = 0
    wlendata = 0
    biji = 0
    
    def __init__(self):
        f = open(self.path, "r")
        t = f.read()
        f.close()
        
        self.data = json.loads(t)
        self.lendata = len(self.data)

        f = open(self.wpath, "r")
        t = f.read()
        f.close()

        self.wdata = json.loads(t)
        self.wlendata = len(self.wdata)
    
    def randin(self, lend, biji=0):
        if biji != 0:
            seed(biji)
            #self.biji+=1
        
        sel = randint(0, lend-1)
        return sel
        
    def cparser(self, data):
        ret = ""
        try:
            r = requests.get(data[1], headers=self.headers)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            shlog("error", "Failed to connect")
            raise SystemExit(err)
        else:
            if r.status_code == 200:
                # ret = r.content
                soup = BeautifulSoup(r.content, "html.parser")
                div = soup.find("div", id="content")
                ret = str(div)
        return ret

    def rchord(self):
        data = self.data[self.randin(self.lendata)]
        return self.cparser(data)

    def wrchord(self):
        data = self.wdata[self.randin(self.wlendata)]
        return self.cparser(data)


if __name__ == '__main__':
    """
    cs = Csembarang()
    
    for i in range(0,10):
        a = cs.randin(len(cs.wdata))
        print(a)
    """