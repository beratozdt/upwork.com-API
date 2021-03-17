import requests
import re
result=[]
query="translation"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
url="http://www.upwork.com/ab/jobs/search/?"
for i in range(10):
    if i >1:
        url=url+"page="+str(i)+"&q="+query+"&sort=recency"
    else:
        url = "http://www.upwork.com/ab/jobs/search/?q="+query+"&sort=recency"
    response=requests.api.get(url=url,headers=headers)
    a=response.text
    dumb=re.findall('%s(.*)%s' % ("href=\"/job/", "\""), a)
    if dumb==[]:
        break
    for i in range(len(dumb)):
        result.append("http://www.upwork.com/jobs/"+dumb[i])
for i in range(len(result)):
    print(result[i])
