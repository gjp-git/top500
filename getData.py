#coding=utf-8

from bs4 import BeautifulSoup
import urllib
from collections import defaultdict

resource = open('2017_500.txt','r')
result = open('2017_500result.txt','a')
logtxt = open('2017_500log.txt','a')
soup = BeautifulSoup(resource,'html.parser')
cols = ['rank','rank_last','nameCn','nameEn','income','profit'
    ,'countryCn','cityCn','employee','ceo','industry'
    ,'countryEn','cityEn','incomeRatio','profitRatio'
    ,'asset','assetRatio','equity','equityRatio','netProfitRatio','assetIncomeRatio']
base = 7
    
items = soup.find_all('tr')

for item in items:
    infos = item.find_all('td')
    
    infoRow = {}
    for col in cols:
        infoRow.setdefault(col,'--')
    
    
    
    rank = infos[0].string
    rank_last = infos[1].string
    name = infos[2].find('a').string
    l = len(name)-1
    while l>=0:
        if name[l]==u'\uff08':
            break
        l = l-1
    nameCn = name[:l].encode('utf-8')
    nameEn = name[l+1:-1].encode('utf-8')
    income = infos[3].string
    profit = infos[4].string
    countryCn = infos[5].string.encode('utf-8')
    
    for index in range(base):
            infoRow[cols[index]] = vars()[cols[index]]
    path = "http://www.fortunechina.com/"+infos[2].a['href'][12:]

    content = urllib.urlopen(path)
        
    contentSoup = BeautifulSoup(content,'html.parser')
    table = contentSoup.find_all('table')
    if len(table)==0:
        logtxt.write(nameCn)
        logtxt.write('\n')
            
    else:
        cityBlock = table[0].find_all('span',class_='txt-14')
        cityCn = cityBlock[1].string.replace('\r\n','').strip().encode('utf-8')
        cityEn = cityBlock[2].string.replace('\r\n','').strip()[1:-1].encode('utf-8')
        
        details = contentSoup.find_all('span',class_='txt-14')
            
        countryEn = contentSoup.find_all('span',class_='ft-silver txt-13')[1].string.replace('\r\n','').strip()[1:-1].encode('utf-8')

        incomeRatio = table[1].find_all('tr')[1].find_all('td')[2].string.replace('\r\n','').strip()
        ceo = details[4].string.replace('\r\n','').strip().encode('utf-8')
        employee = details[8].string.replace('\r\n','').strip()
        profitRatio = details[16].string.replace('\r\n','').strip()
        asset = details[18].string.replace('\r\n','').strip()
        assetRatio = details[19].string.replace('\r\n','').strip()
        equity = details[21].string.replace('\r\n','').strip()
        equityRatio = details[22].string.replace('\r\n','').strip()
        netProfitRatio = details[25].string.replace('\r\n','').strip()
        assetIncomeRatio = details[27].string.replace('\r\n','').strip()
        
        industryBlock = contentSoup.find('div',class_='competitorsdata').find('p',class_='rankcolname').strings
        for ind in industryBlock:
            if '-' in ind:
                industry = ind.split('-')[0].encode('utf-8')
                break
        
        for index in range(base,len(cols)):
            infoRow[cols[index]] = vars()[cols[index]]
            
        
    for index in range(len(cols)):
        if index!=0:
            result.write('::')
        result.write(infoRow[cols[index]])
    
  
    result.write('\n')