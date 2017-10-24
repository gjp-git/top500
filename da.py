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
    
data500 = pd.read_table('D:/$Python data analysis/500/500result.txt',sep='::',header=None,names=cols,engine = 'python')


data500 = data500.replace('阿拉伯联合酋长国','阿联酋')
data500 = data500.replace('沙特阿拉伯','沙特')

data500_1 = pd.read_table('D:/$Python data analysis/500/2017_500result.txt',sep='::',header=None,names=cols1[:base],thousands=',',engine = 'python')

data500['profit'] = data500_1['profit']
data500['rank_last'] = data500_1['rank_last']
data500['countryCn'] = data500_1['countryCn']
data500 = data500.replace(['-','--'],np.nan)




data500[data500['industry'] == '银行：商业储蓄']['nameCn']

data500['ind']= ''
data500.ix[data500['industry'].isin(['银行：商业储蓄','人寿与健康保险（股份）','财产与意外保险（股份）','人寿与健康保险（互助）','多元化金融','保健：保险和管理医保','财产与意外保险（互助）']),'ind'] = '保险金融'
data500.ix[data500['industry'].isin(['炼油','公用设施','采矿、原油生产','能源','化学品','家居、个人用品','批发商：多元化','油气设备与服务']),'ind'] = '能源化工'
data500.ix[data500['industry'].isin(['制药','食品生产','批发：保健','食品：消费产品','饮料','批发：食品','食品：饮食服务业','医疗器材和设备','保健：药品和其他服务','保健：医疗设施','烟草','其他']),'ind'] = '食品医药'
data500.ix[data500['industry'].isin(['电子、电气设备','计算机、办公设备','半导体、电子元件','批发：电子、办公设备']),'ind'] = '电子设备'
data500.ix[data500['industry'].isin(['电信','网络、通讯设备']),'ind'] = '网络通信'
data500.ix[data500['industry'].isin(['航空','邮件、包裹及货物包装运输','铁路运输','管道运输','船务']),'ind'] = '交通运输'
data500.ix[data500['industry'].isin(['车辆与零部件','航天与防务','工业机械','建筑和农业机械']),'ind'] = '机械制造'
data500.ix[data500['industry'].isin(['食品店和杂货店','贸易','专业零售','综合商业','房地产']),'ind'] = '商业贸易'
data500.ix[data500['industry'].isin(['服装','纺织']),'ind'] = '服装纺织'
data500.ix[data500['industry'].isin(['互联网服务和零售','计算机软件']),'ind'] = 'IT互联网'
data500.ix[data500['industry'].isin(['工程与建筑','建材、玻璃']),'ind'] = '建筑建材'
data500.ix[data500['industry'].isin(['信息技术服务','雇佣帮助']),'ind'] = '专业服务'
data500.ix[data500['industry'].isin(['娱乐','旅游服务']),'ind'] = '文化旅游'
data500.ix[data500['industry'].isin(['金属产品']),'ind'] = '冶金矿产'



loc = data500.groupby('countryCn').size().sort_values(ascending=False)
loc[:8].plot(kind = 'barh')
plt.savefig('D:/$Python data analysis/500/pic/figpath.png',dpi=400,bbox_inches='tight')

inc = data500['income'].groupby(data500['countryCn']).sum().sort_values(ascending=False)
inc[:8].plot(kind = 'barh')

ind = data500.groupby('ind').size().sort_values(ascending=False)
ind.plot(kind='pie')


data500['profit'] = data500['profit'].astype('float64')

prof = data500.sort_values(by='profit',ascending=False)[:10].set_index('nameCn')['profit']
prof.plot(kind='barh')

prof_ind = data500.sort_values(by='profit',ascending=False)[:100].groupby('ind').size().sort_values(ascending=False)
prof_ind.plot(kind='barh')
prof_cot = data500.sort_values(by='profit',ascending=False)[:100].groupby('countryCn').size().sort_values(ascending=False)
prof_cot.plot(kind='barh')

#输出生产云图的数据
data500['ind'].to_csv('D:/$Python data analysis/500/2017_ind.txt',index=False,header=False)


cot_ind = data500.groupby(['countryCn','ind']).size().unstack()
cot_ind = cot_ind.reindex(loc.index)
cot_ind.plot(kind='barh',stacked=True)


newCot = data500[data500['rank_last'].isnull()].groupby('countryCn').size().sort_values(ascending=False)



indUS = data500.groupby(['countryCn','ind']).size().ix['美国'].sort_values()
indUS.plot(kind='pie')
indCHA= data500.groupby(['countryCn','ind']).size().ix['中国'].sort_values()
indCHA.plot(kind='pie')
indJAP = data500.groupby(['countryCn','ind']).size().ix['日本'].sort_values()
indJAP.plot(kind='pie')
indGER = data500.groupby(['countryCn','ind']).size().ix['德国'].sort_values()
indGER.plot(kind='pie')
indFRN = data500.groupby(['countryCn','ind']).size().ix['法国'].sort_values()
indFRN.plot(kind='pie')
indEND = data500.groupby(['countryCn','ind']).size().ix['英国'].sort_values()
indEND.plot(kind='pie')

plt.plot()
indEND = data500.groupby(['countryCn','ind']).size().ix['英国'].sort_values()
indEND.plot(kind='pie')
plt.savefig('D:/$Python data analysis/500/pic/indEND.png',dpi=400,bbox_inches='tight')

plt.savefig('D:/$Python data analysis/500/pic/SecondWeek/.png',dpi=400,bbox_inches='tight')

