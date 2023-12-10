# Economics ranking

import requests
from pyquery import PyQuery as pq
from pandas.core.frame import DataFrame

homeRes = requests.get("http://www.shanghairanking.com/Shanghairanking-Subject-Rankings/index.html#")
homeDoc = pq(homeRes.text)   # No need to use ()

dataList = []
cateList = homeDoc("#rankingarea > div:nth-child(10) > a:nth-child(1)")

ad = "http://www.shanghairanking.com/Shanghairanking-Subject-Rankings/"
ad = ad + cateList.attr("href")

cateRes = requests.get(ad)   # request"s
cateDoc = pq(cateRes.text)    
nextPgDoc = cateDoc

subject = cateDoc("#rankingarea > span")

subject = str(cateList)
subject = str(subject)
subject = subject.split(">")
subject = subject[1]
subject = subject.split("<")
subject = subject[0]

sub = cateDoc("#rankingnav > form:nth-child(2) > select:nth-child(2)")
for item in sub.items():
    dataDict={}
    dataDict["title"] = ''
    dataDict['country'] = ''
    dataDict['rank'] = ''
    dataList.append(dataDict)

for i in range(1): # while True:
    item = cateDoc("#UniversityRanking > tr")
    for eachItemDoc in item.items():
        dataDict={}
        if eachItemDoc(("td:nth-child(3) > img")).attr("title")!= "United States":
            pass
        else:
            dataDict["title"] = eachItemDoc(".left").text()
            dataDict["country"] = eachItemDoc(("td:nth-child(3) > img")).attr("title")
            dataDict["rank"] = eachItemDoc("tr>td:nth-child(1) ").text()    
            dataList.append(dataDict)
    if len(item) == 0:
        break

print(subject)
data=DataFrame(dataList)

#display(data)
data[1:50]