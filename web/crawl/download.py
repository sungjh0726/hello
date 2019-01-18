import urllib.request as ur

url = "<button id="searchDanjiBtn" onclick="tmpSearchDanji();">검 색</button>"

saveFile = "./images/weather2.csv"
ur.urlretrieve(url, saveFile)
print("OK!")