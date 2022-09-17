import  os
import requests

file1 = open('files_to_download.txt', 'r')
Lines = file1.readlines()
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    temp =line.strip()
    name= line.replace("https://firebasestorage.googleapis.com/v0/b/unseen1-1.appspot.com/o/","")
    r = requests.get(temp, allow_redirects=True)
    open(name +".mp4", 'wb').write(r.content)
