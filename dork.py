import os
print("Instagram:LQM33.PY")
try:
    os.remove("cıktı.txt")
except:pass
try:
    import urllib.request
except:
    os.system("pip install urllib3")
    os.system("pip install urllib")
import json
import random
url = urllib.request.urlopen("https://random-word-api.herokuapp.com/word?number=50")
words = json.loads(url.read())
print("LQM33 DORK OLUŞTURUCU")
i=0
while (i<50):
    with open("dork.txt",'r')as dorkr:
        for dork in  dorkr:
                random_word = random.choice(words)
                a=dork+random_word
                print(a)
                  
                with open("cıktı.txt",'a+')as cıktı:
                    cıktı.write(a+"\n")
                i+=1
                    
