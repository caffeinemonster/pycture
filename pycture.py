#!/usr/bin/python
bDebug = True
import random
import sys
import os
import requests
import pylogger
import urllib

sFile = "images.txt"
mysubreddits = []
parameters = {'limit': 25, }
headers = {
    'User-Agent': 'Pycture - Reddit image grabber'
}


def getsize(uri):
    try:
        ofile = urllib.urlopen(uri)
        size = ofile.headers.get("content-length")
        ofile.close()
        return int(size)
    except:
        return 0


def AddImages(strType, strCheck):
    if strCheck[-len(strType):] == strType:
        if getsize(strCheck) > 1024:
            f = open(sFile, 'a')
            f.write(strCheck + "\n")
            pylogger.add("INFOADDEDIMAGE", strCheck)
            f.close()


def DeleteFile(sFilename):
    if os.path.exists(sFilename):
        os.remove(sFilename)


def GetData(intsubreddit):
    data = ""
    try:
        rs = r'http://www.reddit.com/r/' + mysubreddits[intsubreddit] + '/.json'
        pylogger.add("INFOQUERY", rs)
        r = requests.get(rs, headers=headers, params=parameters)
        data = r.json()
    except:
        pylogger.add("GETDATAERROR", "Error fetching data. (" + str(mysubreddits[intsubreddit]) + ")")
    return data


def LoadDataSources():
    with open('urls.txt', 'r') as ofile:
        for line in ofile:
            s = line.strip()[3:]
            if len(s) > 0:
                pylogger.add("INFODSADDED", s)
                mysubreddits.append(s)


def Main():
    intsubreddit = 0
    DeleteFile(sFile)
    LoadDataSources()
    random.shuffle(mysubreddits)
    while(1 == 1):
        data = GetData(intsubreddit)
        intsubreddit = intsubreddit + 1
        if intsubreddit >= len(mysubreddits):
            intsubreddit = 0
        for child in data['data']['children']:
            mystring = child['data']['url'].lower()
            for s in ['jpg', '.jpeg', 'png', 'tiff', 'bmp']:
                AddImages("." + s, mystring)
        intDelay = random.randint(5, 15)
        os.system("feh -D " + str(intDelay) + " --randomize -x -N --cycle-once -F --zoom fill --geometry 1920x1080 -f " + sFile)
        DeleteFile(sFile)

Main()