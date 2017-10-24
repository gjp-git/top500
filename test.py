from bs4 import BeautifulSoup
import urllib

result = open('result_test.txt','a')




content = urllib.urlopen("http://www.fortunechina.com/global500/221/2017")
contentSoup = BeautifulSoup(content,'html.parser')
infos = contentSoup.find_all('span',class_='txt-14')
table = contentSoup.find_all('table')
cityBlock = table[0].find_all('span',class_='txt-14')
for info in infos:
    result.write('::')
    result.write(info.string.encode('utf-8'))