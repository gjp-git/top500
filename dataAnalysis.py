# coding = utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

cols = ['rank','nameCn','nameEn','ceo','industry','location'
    ,'countryCn','cityCn','employee','income'
    ,'countryEn','cityEn','incomeRatio','profit','profitRatio'
    ,'asset','assetRatio','equity','equityRatio','netProfitRatio','assetIncomeRatio']

cols1 = ['rank','rank_last','nameCn','nameEn','income','profit'
    ,'countryCn','cityCn','employee','ceo','industry'
    ,'countryEn','cityEn','incomeRatio','profitRatio'
    ,'asset','assetRatio','equity','equityRatio','netProfitRatio','assetIncomeRatio']
base = 7
    
data5002017 = pd.read_table('D:/$Python data analysis/500/500result.txt',sep='::',header=None,names=cols,na_values=["--","-"],engine = 'python')
data5002015 = pd.read_table('D:/$Python data analysis/500/2015_500result.txt',sep='::',header=None,names=cols1,na_values=["--","-"],thousands=',',engine = 'python')
data5002016 = pd.read_table('D:/$Python data analysis/500/2016_500result.txt',sep='::',header=None,names=cols1,na_values=["--","-"],thousands=',',engine = 'python')

data5002017 = data5002017.replace('阿拉伯联合酋长国','阿联酋')
data5002017 = data5002017.replace('沙特阿拉伯','沙特')
data5002015 = data5002015.replace('阿拉伯联合酋长国','阿联酋')
data5002015 = data5002015.replace('沙特阿拉伯','沙特')
data5002016 = data5002016.replace('阿拉伯联合酋长国','阿联酋')
data5002016 = data5002016.replace('沙特阿拉伯','沙特')

data5002017_1 = pd.read_table('D:/$Python data analysis/500/2017_500result.txt',sep='::',header=None,names=cols1[:base],na_values=["--","-"],thousands=',',engine = 'python')
data5002017['profit'] = data5002017_1['profit']
data5002017['rank_last'] = data5002017_1['rank_last']
data5002017['countryCn'] = data5002017_1['countryCn']
data5002017['nameEn'] = data5002017_1['nameEn']
'''
data5002015 = data5002015.replace(['-','--'],np.nan)
data5002016 = data5002016.replace(['-','--'],np.nan)
data5002017 = data5002017.replace(['-','--'],np.nan)
'''
data5002015['profit'] = data5002015['profit'].astype('float64')
data5002016['profit'] = data5002016['profit'].astype('float64')
data5002017['profit'] = data5002017['profit'].astype('float64')
data5002015.rank_last = data5002015['rank_last'].fillna('999').astype('int32')
data5002016.rank_last = data5002016['rank_last'].fillna('999').astype('int32')
data5002017.rank_last = data5002017['rank_last'].fillna('999').astype('int32')

data5002015['ind']= ''
data5002015.ix[data5002015['industry'].isin(['银行：商业储蓄','人寿与健康保险（股份）','财产与意外保险（股份）','人寿与健康保险（互助）','多元化金融','保健：保险和管理医保','财产与意外保险（互助）']),'ind'] = '保险金融'
data5002015.ix[data5002015['industry'].isin(['炼油','公用设施','采矿、原油生产','能源','化学品','家居、个人用品','油气设备与服务','公用事业：天然气和电力']),'ind'] = '能源电力化工'
data5002015.ix[data5002015['industry'].isin(['制药','食品生产','食品：消费产品','饮料','食品：饮食服务业','医疗器材和设备','保健：药品和其他服务','保健：医疗设施','烟草']),'ind'] = '食品医药'
data5002015.ix[data5002015['industry'].isin(['电子、电气设备','计算机、办公设备','半导体、电子元件']),'ind'] = '电子设备'
data5002015.ix[data5002015['industry'].isin(['航空','邮件、包裹及货物包装运输','铁路运输','管道运输','船务']),'ind'] = '交通运输'
data5002015.ix[data5002015['industry'].isin(['车辆与零部件','航天与防务','工业机械','建筑和农业机械']),'ind'] = '机械制造'
data5002015.ix[data5002015['industry'].isin(['食品店和杂货店','专业零售','综合商业','批发商：多元化','批发：食品','批发：电子、办公设备','批发：保健']),'ind'] = '批发零售'
data5002015.ix[data5002015['industry'].isin(['服装','纺织']),'ind'] = '服装纺织'
data5002015.ix[data5002015['industry'].isin(['互联网服务和零售','计算机软件','电信','网络、通讯设备']),'ind'] = 'TMT'
data5002015.ix[data5002015['industry'].isin(['工程与建筑','建材、玻璃','房地产']),'ind'] = '房地产建筑建材'
data5002015.ix[data5002015['industry'].isin(['信息技术服务','雇佣帮助']),'ind'] = '专业服务'
data5002015.ix[data5002015['industry'].isin(['娱乐','旅游服务']),'ind'] = '文化旅游'
data5002015.ix[data5002015['industry'].isin(['金属产品']),'ind'] = '冶金矿产'
data5002015.ix[data5002015['industry'].isin(['其他']),'ind'] = '其他'
data5002015.ix[data5002015['industry'].isin(['贸易']),'ind'] = '贸易投资'

data5002016['ind']= ''
data5002016.ix[data5002016['industry'].isin(['银行：商业储蓄','人寿与健康保险（股份）','财产与意外保险（股份）','人寿与健康保险（互助）','多元化金融','保健：保险和管理医保','财产与意外保险（互助）']),'ind'] = '保险金融'
data5002016.ix[data5002016['industry'].isin(['炼油','公用设施','采矿、原油生产','能源','化学品','家居、个人用品','油气设备与服务','公用事业：天然气和电力']),'ind'] = '能源电力化工'
data5002016.ix[data5002016['industry'].isin(['制药','食品生产','食品：消费产品','饮料','食品：饮食服务业','医疗器材和设备','保健：药品和其他服务','保健：医疗设施','烟草']),'ind'] = '食品医药'
data5002016.ix[data5002016['industry'].isin(['电子、电气设备','计算机、办公设备','半导体、电子元件']),'ind'] = '电子设备'
data5002016.ix[data5002016['industry'].isin(['航空','邮件、包裹及货物包装运输','铁路运输','管道运输','船务']),'ind'] = '交通运输'
data5002016.ix[data5002016['industry'].isin(['车辆与零部件','航天与防务','工业机械','建筑和农业机械']),'ind'] = '机械制造'
data5002016.ix[data5002016['industry'].isin(['食品店和杂货店','专业零售','综合商业','批发商：多元化','批发：食品','批发：电子、办公设备','批发：保健']),'ind'] = '批发零售'
data5002016.ix[data5002016['industry'].isin(['服装','纺织']),'ind'] = '服装纺织'
data5002016.ix[data5002016['industry'].isin(['互联网服务和零售','计算机软件','电信','网络、通讯设备']),'ind'] = 'TMT'
data5002016.ix[data5002016['industry'].isin(['工程与建筑','建材、玻璃','房地产']),'ind'] = '房地产建筑建材'
data5002016.ix[data5002016['industry'].isin(['信息技术服务','雇佣帮助']),'ind'] = '专业服务'
data5002016.ix[data5002016['industry'].isin(['娱乐','旅游服务']),'ind'] = '文化旅游'
data5002016.ix[data5002016['industry'].isin(['金属产品']),'ind'] = '冶金矿产'
data5002016.ix[data5002016['industry'].isin(['其他']),'ind'] = '其他'
data5002016.ix[data5002016['industry'].isin(['贸易']),'ind'] = '贸易投资'

data5002017['ind']= ''
data5002017.ix[data5002017['industry'].isin(['银行：商业储蓄','人寿与健康保险（股份）','财产与意外保险（股份）','人寿与健康保险（互助）','多元化金融','保健：保险和管理医保','财产与意外保险（互助）']),'ind'] = '保险金融'
data5002017.ix[data5002017['industry'].isin(['炼油','公用设施','采矿、原油生产','能源','化学品','家居、个人用品','油气设备与服务','公用事业：天然气和电力']),'ind'] = '能源电力化工'
data5002017.ix[data5002017['industry'].isin(['制药','食品生产','食品：消费产品','饮料','食品：饮食服务业','医疗器材和设备','保健：药品和其他服务','保健：医疗设施','烟草']),'ind'] = '食品医药'
data5002017.ix[data5002017['industry'].isin(['电子、电气设备','计算机、办公设备','半导体、电子元件']),'ind'] = '电子设备'
data5002017.ix[data5002017['industry'].isin(['航空','邮件、包裹及货物包装运输','铁路运输','管道运输','船务']),'ind'] = '交通运输'
data5002017.ix[data5002017['industry'].isin(['车辆与零部件','航天与防务','工业机械','建筑和农业机械']),'ind'] = '机械制造'
data5002017.ix[data5002017['industry'].isin(['食品店和杂货店','专业零售','综合商业','批发商：多元化','批发：食品','批发：电子、办公设备','批发：保健']),'ind'] = '批发零售'
data5002017.ix[data5002017['industry'].isin(['服装','纺织']),'ind'] = '服装纺织'
data5002017.ix[data5002017['industry'].isin(['互联网服务和零售','计算机软件','电信','网络、通讯设备']),'ind'] = 'TMT'
data5002017.ix[data5002017['industry'].isin(['工程与建筑','建材、玻璃','房地产']),'ind'] = '房地产建筑建材'
data5002017.ix[data5002017['industry'].isin(['信息技术服务','雇佣帮助']),'ind'] = '专业服务'
data5002017.ix[data5002017['industry'].isin(['娱乐','旅游服务']),'ind'] = '文化旅游'
data5002017.ix[data5002017['industry'].isin(['金属产品']),'ind'] = '冶金矿产'
data5002017.ix[data5002017['industry'].isin(['其他']),'ind'] = '其他'
data5002017.ix[data5002017['industry'].isin(['贸易']),'ind'] = '贸易投资'

#三年地区统计
loc2017 = data5002017.groupby('countryCn').size().sort_values(ascending=False)
loc2016 = data5002016.groupby('countryCn').size().sort_values(ascending=False)
loc2015 = data5002015.groupby('countryCn').size().sort_values(ascending=False)
loc = pd.DataFrame([loc2015,loc2016,loc2017])
loc.index = [2015,2016,2017]
loc = loc.T
loc = loc.sort_values(by=2017,ascending=False)
loc[:8].plot(kind='bar')


#三年行业统计
ind2017 = data5002017.groupby('ind').size().sort_values(ascending=False)
ind2016 = data5002016.groupby('ind').size().sort_values(ascending=False)
ind2015 = data5002015.groupby('ind').size().sort_values(ascending=False)
ind = pd.DataFrame([ind2015,ind2016,ind2017])
ind.index = [2015,2016,2017]
ind = ind.T
ind = ind.sort_values(by=2017,ascending=False)
ind.plot(kind='bar')

#三年新入榜企业
newCop2017 = data5002017[data5002017['rank_last']==999]
newCop2016 = data5002016[data5002016['rank_last']==999]
newCop2015 = data5002015[data5002015['rank_last']==999]

newCopCot2017 = newCop2017.groupby('countryCn').size().sort_values(ascending=False)
newCopCot2016 = newCop2016.groupby('countryCn').size().sort_values(ascending=False)
newCopCot2015 = newCop2015.groupby('countryCn').size().sort_values(ascending=False)

newCopCot = pd.DataFrame([newCopCot2015,newCopCot2016,newCopCot2017])
newCopCot.index = [2015,2016,2017]
newCopCot = newCopCot.T.fillna(0).sort_values(by=2017,ascending=False)
newCopCot.plot(kind='bar')

newCopInd2017 = newCop2017.groupby('ind').size().sort_values(ascending=False)
newCopInd2016 = newCop2016.groupby('ind').size().sort_values(ascending=False)
newCopInd2015 = newCop2015.groupby('ind').size().sort_values(ascending=False)

newCopInd = pd.DataFrame([newCopInd2015,newCopInd2016,newCopInd2017])
newCopInd.index = [2015,2016,2017]
newCopInd = newCopInd.T.fillna(0).sort_values(by=2017,ascending=False)
newCopInd.plot(kind='bar')



#三年排名聚合
rank500 = pd.merge(pd.merge(data5002015[['nameCn','rank_last','rank']],data5002016[['nameCn','rank_last','rank']],left_on='rank',right_on='rank_last',how='outer',suffixes=('_2015','_2016')),data5002017[['nameCn','rank_last','rank']],left_on='rank_2016',right_on='rank_last',how='outer',suffixes=('','_2017'))

#2016年跌出排行榜的企业
copSet2016 = set(rank500[(rank500['rank_2015'].notnull()) & (rank500['rank_2016'].isnull())]['nameCn_2015'])
cotDropInd2016 = data5002015[data5002015['nameCn'].isin(copSet2016)].groupby('ind').size().sort_values(ascending=False)
cotDropInd2016.plot(kind='barh')
cotDropCot2016 = data5002015[data5002015['nameCn'].isin(copSet2016)].groupby('countryCn').size().sort_values(ascending=False)
cotDropCot2016.plot(kind='barh')

#2017年跌出排行榜的企业
copSet2017 = set(rank500[(rank500['rank_2016'].notnull()) & (rank500['rank'].isnull())]['nameCn_2016'])
cotDropInd2017 = data5002016[data5002016['nameCn'].isin(copSet2017)].groupby('ind').size().sort_values(ascending=False)
cotDropInd2017.plot(kind='barh')
cotDropCot2017 = data5002016[data5002016['nameCn'].isin(copSet2017)].groupby('countryCn').size().sort_values(ascending=False)
cotDropCot2017.plot(kind='barh')

#2016,2017两年行业情况比较
cotDropInd = pd.DataFrame([cotDropInd2016,cotDropInd2017])
cotDropInd.index = [2016,2017]
cotDropInd = cotDropInd.T.fillna(0).sort_values(by=2017,ascending=False)
cotDropInd.plot(kind='barh')


#三年一直稳步提升
alwaysUp = set(rank500[(rank500['rank_last_2015']>=rank500['rank_2015']) & (rank500['rank_last_2016']>=rank500['rank_2016']) & (rank500['rank_last']>=rank500['rank']) & (rank500['rank_2015'] != 999) & (rank500['rank_2016'] != 999) & (rank500['rank'] != 999)]['nameCn'])
cotUpInd = data5002017[data5002017['nameCn'].isin(alwaysUp)].groupby('ind').size().sort_values(ascending=False)
cotUpInd.plot(kind='barh')
cotUpCountry = data5002017[data5002017['nameCn'].isin(alwaysUp)].groupby('countryCn').size().sort_values(ascending=False)
cotUpCountry.plot(kind='barh')


#每年提升的行业及比例
riseSet2015 = set(rank500[rank500['rank_last_2015']>=rank500['rank_2015']]['nameCn_2015'])
riseSet2016 = set(rank500[rank500['rank_last_2016']>=rank500['rank_2016']]['nameCn_2016'])
riseSet2017 = set(rank500[rank500['rank_last']>=rank500['rank']]['nameCn'])

riseInd2015 = data5002015[data5002015['nameCn'].isin(riseSet2015)].groupby('ind').size().sort_values(ascending=False)
riseInd2016 = data5002016[data5002016['nameCn'].isin(riseSet2016)].groupby('ind').size().sort_values(ascending=False)
riseInd2017 = data5002016[data5002016['nameCn'].isin(riseSet2017)].groupby('ind').size().sort_values(ascending=False)
riseInd2015.plot(kind='barh')
riseInd2016.plot(kind='barh')
riseInd2017.plot(kind='barh')

riseIndRate2015 = (riseInd2015/ind2015).sort_values(ascending=False)
riseIndRate2015.plot(kind='barh')
riseIndRate2016 = (riseInd2016/ind2016).sort_values(ascending=False)
riseIndRate2016.plot(kind='barh')
riseIndRate2017 = (riseInd2017/ind2017).sort_values(ascending=False)
riseIndRate2017.plot(kind='barh')

data5002017[data5002017['countryCn']=='中国'].groupby('ind').size().sort_values(ascending=False).plot(kind='pie')

data5002017[data5002017['countryCn']=='美国'].groupby('ind').size().sort_values(ascending=False).plot(kind='pie')
