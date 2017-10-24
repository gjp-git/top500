#coding=utf-8

from bs4 import BeautifulSoup
import urllib
from collections import defaultdict

result = open('500result111.txt','a')
log = open('result.txt','a')

cols = ['rank','nameCn','nameEn','ceo','industry','location'
    ,'countryCn','cityCn','employee','income'
    ,'countryEn','cityEn','incomeRatio','profit','profitRatio'
    ,'asset','assetRatio','equity','equityRatio','netProfitRatio','assetIncomeRatio']
base = 10

for i in range(45,46):
    #榜单路径
    html = urllib.urlopen("http://www.fortunechina.com/search/f500beta/search.do?facetAction=&facetStr=type%23%E6%89%80%E5%B1%9E%E6%A6%9C%E5%8D%95%23%E4%B8%96%E7%95%8C500%E5%BC%BA%3Byear%23%E6%9C%80%E8%BF%91%E4%B8%8A%E6%A6%9C%E6%97%B6%E9%97%B4%232017%3B&"+('curPage=%d'%i)).read()
    soup = BeautifulSoup(html,'html.parser')
    comItems = soup.find_all('div',class_='rankitem')
    for n,item in enumerate(comItems):
        infoRow = {}
        for col in cols:
            infoRow.setdefault(col,'--')
    
    
    
        rank = str((i-1)*10+n+1)
        nameTag = item.find('a',target='_blank')
        name = nameTag.string.strip().encode('utf-8')
        
        l = len(name)-1
        while True:
            if name[l]=='(':
                break
            l = l-1
        nameCn = name[:l]
        nameEn = name[l+1:-1]
        ceo = item.find('span',class_='content_user').string.strip().encode('utf-8')
        infos = item.find_all('span',class_='content')
        industry = infos[0].string.replace('\r\n','').strip().encode('utf-8')
        location = infos[1].string.replace('\r\n','').replace(' ','').strip().encode('utf-8')
        locs = location.split(',')
        cityCn = locs[0]
        countryCn = locs[1]
        income = infos[2].string.replace('\r\n','').strip().encode('utf-8')
        employee = infos[3].string.replace('\r\n','').strip().encode('utf-8')
        
        for index in range(base):
            infoRow[cols[index]] = vars()[cols[index]]
        
        #详细信息的路径
        path = nameTag['href']
        content = urllib.urlopen(path)
        
        contentSoup = BeautifulSoup(content,'html.parser')
        table = contentSoup.find_all('table')
        if len(table)==0:
            log.write(nameCn)
            log.write('\n')
            
        else:
            cityBlock = table[0].find_all('span',class_='txt-14')
            city = cityBlock[1].string.replace('\r\n','').strip().encode('utf-8')
            cityEn = cityBlock[2].string.replace('\r\n','').strip()[1:-1].encode('utf-8')
            
            details = contentSoup.find_all('span',class_='txt-14')
            
            countryEn = contentSoup.find_all('span',class_='ft-silver txt-13')[1].string.replace('\r\n','').strip()[1:-1].encode('utf-8')
            country = details[6].string.replace('\r\n','').strip().encode('utf-8')
            incomeRatio = table[1].find_all('tr')[1].find_all('td')[2].string.replace('\r\n','').strip()
            profit = details[15].string.replace('\r\n','').strip()
            profitRatio = details[16].string.replace('\r\n','').strip()
            asset = details[18].string.replace('\r\n','').strip()
            assetRatio = details[19].string.replace('\r\n','').strip()
            equity = details[21].string.replace('\r\n','').strip()
            equityRatio = details[22].string.replace('\r\n','').strip()
            netProfitRatio = details[25].string.replace('\r\n','').strip()
            assetIncomeRatio = details[27].string.replace('\r\n','').strip()
            
            for index in range(base,len(cols)):
                infoRow[cols[index]] = vars()[cols[index]]
            
        
        for index in range(len(cols)):
            if index!=0:
                result.write('::')
            result.write(infoRow[cols[index]])
        
        """
        #输出结果
        result.write(str((i-1)*10+n+1))
        result.write('::')
        temp = name.string.encode('utf-8').strip()
        names = temp.split('(')
        nameCn = names[0]
        nameEn = names[1][:-1]
        result.write(nameCn)
        result.write('::')
        result.write(nameEn)
        result.write('::')
        if n==0:
            result.write(boss.string.encode('utf-8').strip())
            for info in infos:
                result.write('::')
                result.write(info.string.replace('\r\n','').strip().encode('utf-8'))
            
        else:
            result.write(boss.string.encode('utf-8'))
            for info in infos:
                result.write('::')
                result.write(info.string.encode('utf-8'))
                
        if hasDetail:
            result.write('::')
            result.write(country.string.replace('\r\n','').strip().encode('utf-8'))
            result.write('::')
            result.write(countryEn.string.replace('\r\n','').strip()[1:-1].encode('utf-8'))
            result.write('::')
            result.write(city.string.replace('\r\n','').strip().encode('utf-8'))
            result.write('::')
            result.write(cityEn.string.replace('\r\n','').strip()[1:-1].encode('utf-8'))
            
            result.write('::')
            result.write(incomeRatio.string.replace('\r\n','').strip())
            result.write('::')
            result.write(profit.string.replace('\r\n','').strip())
            result.write('::')
            result.write(profitRatio.string.replace('\r\n','').strip())
            result.write('::')
            result.write(asset.string.replace('\r\n','').strip())
            result.write('::')
            result.write(assetRatio.string.replace('\r\n','').strip())
            result.write('::')
            result.write(equity.string.replace('\r\n','').strip())
            result.write('::')
            result.write(equityRatio.string.replace('\r\n','').strip())
            result.write('::')
            result.write(netProfitRatio.string.replace('\r\n','').strip())
            result.write('::')
            result.write(assetIncomeRatio.string.replace('\r\n','').strip())
        
        #利润14
        result.write('::')
        result.write(details[5].string.replace('\r\n','').strip())
        #利润年增减%15
        result.write('::')
        result.write(details[6].string.replace('\r\n','').strip())
        #资产17
        result.write('::')
        result.write(details[8].string.replace('\r\n','').strip())
        #资产年增减%18
        result.write('::')
        result.write(details[9].string.replace('\r\n','').strip())
        #股东权益20
        result.write('::')
        result.write(details[11].string.replace('\r\n','').strip())
        #股东权益年增减%21
        result.write('::')
        result.write(details[12].string.replace('\r\n','').strip())
        #净利率%24
        result.write('::')
        result.write(details[15].string.replace('\r\n','').strip())
        #资产收益率%26
        result.write('::')
        result.write(details[17].string.replace('\r\n','').strip())
        """
        result.write('\n')
        