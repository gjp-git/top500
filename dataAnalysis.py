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

data5002017 = data5002017.replace('����������������','������')
data5002017 = data5002017.replace('ɳ�ذ�����','ɳ��')
data5002015 = data5002015.replace('����������������','������')
data5002015 = data5002015.replace('ɳ�ذ�����','ɳ��')
data5002016 = data5002016.replace('����������������','������')
data5002016 = data5002016.replace('ɳ�ذ�����','ɳ��')

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
data5002015.ix[data5002015['industry'].isin(['���У���ҵ����','�����뽡�����գ��ɷݣ�','�Ʋ������Ᵽ�գ��ɷݣ�','�����뽡�����գ�������','��Ԫ������','���������պ͹���ҽ��','�Ʋ������Ᵽ�գ�������']),'ind'] = '���ս���'
data5002015.ix[data5002015['industry'].isin(['����','������ʩ','�ɿ�ԭ������','��Դ','��ѧƷ','�Ҿӡ�������Ʒ','�����豸�����','������ҵ����Ȼ���͵���']),'ind'] = '��Դ��������'
data5002015.ix[data5002015['industry'].isin(['��ҩ','ʳƷ����','ʳƷ�����Ѳ�Ʒ','����','ʳƷ����ʳ����ҵ','ҽ�����ĺ��豸','������ҩƷ����������','������ҽ����ʩ','�̲�']),'ind'] = 'ʳƷҽҩ'
data5002015.ix[data5002015['industry'].isin(['���ӡ������豸','��������칫�豸','�뵼�塢����Ԫ��']),'ind'] = '�����豸'
data5002015.ix[data5002015['industry'].isin(['����','�ʼ��������������װ����','��·����','�ܵ�����','����']),'ind'] = '��ͨ����'
data5002015.ix[data5002015['industry'].isin(['�������㲿��','���������','��ҵ��е','������ũҵ��е']),'ind'] = '��е����'
data5002015.ix[data5002015['industry'].isin(['ʳƷ����ӻ���','רҵ����','�ۺ���ҵ','�����̣���Ԫ��','������ʳƷ','���������ӡ��칫�豸','����������']),'ind'] = '��������'
data5002015.ix[data5002015['industry'].isin(['��װ','��֯']),'ind'] = '��װ��֯'
data5002015.ix[data5002015['industry'].isin(['���������������','��������','����','���硢ͨѶ�豸']),'ind'] = 'TMT'
data5002015.ix[data5002015['industry'].isin(['�����뽨��','���ġ�����','���ز�']),'ind'] = '���ز���������'
data5002015.ix[data5002015['industry'].isin(['��Ϣ��������','��Ӷ����']),'ind'] = 'רҵ����'
data5002015.ix[data5002015['industry'].isin(['����','���η���']),'ind'] = '�Ļ�����'
data5002015.ix[data5002015['industry'].isin(['������Ʒ']),'ind'] = 'ұ����'
data5002015.ix[data5002015['industry'].isin(['����']),'ind'] = '����'
data5002015.ix[data5002015['industry'].isin(['ó��']),'ind'] = 'ó��Ͷ��'

data5002016['ind']= ''
data5002016.ix[data5002016['industry'].isin(['���У���ҵ����','�����뽡�����գ��ɷݣ�','�Ʋ������Ᵽ�գ��ɷݣ�','�����뽡�����գ�������','��Ԫ������','���������պ͹���ҽ��','�Ʋ������Ᵽ�գ�������']),'ind'] = '���ս���'
data5002016.ix[data5002016['industry'].isin(['����','������ʩ','�ɿ�ԭ������','��Դ','��ѧƷ','�Ҿӡ�������Ʒ','�����豸�����','������ҵ����Ȼ���͵���']),'ind'] = '��Դ��������'
data5002016.ix[data5002016['industry'].isin(['��ҩ','ʳƷ����','ʳƷ�����Ѳ�Ʒ','����','ʳƷ����ʳ����ҵ','ҽ�����ĺ��豸','������ҩƷ����������','������ҽ����ʩ','�̲�']),'ind'] = 'ʳƷҽҩ'
data5002016.ix[data5002016['industry'].isin(['���ӡ������豸','��������칫�豸','�뵼�塢����Ԫ��']),'ind'] = '�����豸'
data5002016.ix[data5002016['industry'].isin(['����','�ʼ��������������װ����','��·����','�ܵ�����','����']),'ind'] = '��ͨ����'
data5002016.ix[data5002016['industry'].isin(['�������㲿��','���������','��ҵ��е','������ũҵ��е']),'ind'] = '��е����'
data5002016.ix[data5002016['industry'].isin(['ʳƷ����ӻ���','רҵ����','�ۺ���ҵ','�����̣���Ԫ��','������ʳƷ','���������ӡ��칫�豸','����������']),'ind'] = '��������'
data5002016.ix[data5002016['industry'].isin(['��װ','��֯']),'ind'] = '��װ��֯'
data5002016.ix[data5002016['industry'].isin(['���������������','��������','����','���硢ͨѶ�豸']),'ind'] = 'TMT'
data5002016.ix[data5002016['industry'].isin(['�����뽨��','���ġ�����','���ز�']),'ind'] = '���ز���������'
data5002016.ix[data5002016['industry'].isin(['��Ϣ��������','��Ӷ����']),'ind'] = 'רҵ����'
data5002016.ix[data5002016['industry'].isin(['����','���η���']),'ind'] = '�Ļ�����'
data5002016.ix[data5002016['industry'].isin(['������Ʒ']),'ind'] = 'ұ����'
data5002016.ix[data5002016['industry'].isin(['����']),'ind'] = '����'
data5002016.ix[data5002016['industry'].isin(['ó��']),'ind'] = 'ó��Ͷ��'

data5002017['ind']= ''
data5002017.ix[data5002017['industry'].isin(['���У���ҵ����','�����뽡�����գ��ɷݣ�','�Ʋ������Ᵽ�գ��ɷݣ�','�����뽡�����գ�������','��Ԫ������','���������պ͹���ҽ��','�Ʋ������Ᵽ�գ�������']),'ind'] = '���ս���'
data5002017.ix[data5002017['industry'].isin(['����','������ʩ','�ɿ�ԭ������','��Դ','��ѧƷ','�Ҿӡ�������Ʒ','�����豸�����','������ҵ����Ȼ���͵���']),'ind'] = '��Դ��������'
data5002017.ix[data5002017['industry'].isin(['��ҩ','ʳƷ����','ʳƷ�����Ѳ�Ʒ','����','ʳƷ����ʳ����ҵ','ҽ�����ĺ��豸','������ҩƷ����������','������ҽ����ʩ','�̲�']),'ind'] = 'ʳƷҽҩ'
data5002017.ix[data5002017['industry'].isin(['���ӡ������豸','��������칫�豸','�뵼�塢����Ԫ��']),'ind'] = '�����豸'
data5002017.ix[data5002017['industry'].isin(['����','�ʼ��������������װ����','��·����','�ܵ�����','����']),'ind'] = '��ͨ����'
data5002017.ix[data5002017['industry'].isin(['�������㲿��','���������','��ҵ��е','������ũҵ��е']),'ind'] = '��е����'
data5002017.ix[data5002017['industry'].isin(['ʳƷ����ӻ���','רҵ����','�ۺ���ҵ','�����̣���Ԫ��','������ʳƷ','���������ӡ��칫�豸','����������']),'ind'] = '��������'
data5002017.ix[data5002017['industry'].isin(['��װ','��֯']),'ind'] = '��װ��֯'
data5002017.ix[data5002017['industry'].isin(['���������������','��������','����','���硢ͨѶ�豸']),'ind'] = 'TMT'
data5002017.ix[data5002017['industry'].isin(['�����뽨��','���ġ�����','���ز�']),'ind'] = '���ز���������'
data5002017.ix[data5002017['industry'].isin(['��Ϣ��������','��Ӷ����']),'ind'] = 'רҵ����'
data5002017.ix[data5002017['industry'].isin(['����','���η���']),'ind'] = '�Ļ�����'
data5002017.ix[data5002017['industry'].isin(['������Ʒ']),'ind'] = 'ұ����'
data5002017.ix[data5002017['industry'].isin(['����']),'ind'] = '����'
data5002017.ix[data5002017['industry'].isin(['ó��']),'ind'] = 'ó��Ͷ��'

#�������ͳ��
loc2017 = data5002017.groupby('countryCn').size().sort_values(ascending=False)
loc2016 = data5002016.groupby('countryCn').size().sort_values(ascending=False)
loc2015 = data5002015.groupby('countryCn').size().sort_values(ascending=False)
loc = pd.DataFrame([loc2015,loc2016,loc2017])
loc.index = [2015,2016,2017]
loc = loc.T
loc = loc.sort_values(by=2017,ascending=False)
loc[:8].plot(kind='bar')


#������ҵͳ��
ind2017 = data5002017.groupby('ind').size().sort_values(ascending=False)
ind2016 = data5002016.groupby('ind').size().sort_values(ascending=False)
ind2015 = data5002015.groupby('ind').size().sort_values(ascending=False)
ind = pd.DataFrame([ind2015,ind2016,ind2017])
ind.index = [2015,2016,2017]
ind = ind.T
ind = ind.sort_values(by=2017,ascending=False)
ind.plot(kind='bar')

#�����������ҵ
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



#���������ۺ�
rank500 = pd.merge(pd.merge(data5002015[['nameCn','rank_last','rank']],data5002016[['nameCn','rank_last','rank']],left_on='rank',right_on='rank_last',how='outer',suffixes=('_2015','_2016')),data5002017[['nameCn','rank_last','rank']],left_on='rank_2016',right_on='rank_last',how='outer',suffixes=('','_2017'))

#2016��������а����ҵ
copSet2016 = set(rank500[(rank500['rank_2015'].notnull()) & (rank500['rank_2016'].isnull())]['nameCn_2015'])
cotDropInd2016 = data5002015[data5002015['nameCn'].isin(copSet2016)].groupby('ind').size().sort_values(ascending=False)
cotDropInd2016.plot(kind='barh')
cotDropCot2016 = data5002015[data5002015['nameCn'].isin(copSet2016)].groupby('countryCn').size().sort_values(ascending=False)
cotDropCot2016.plot(kind='barh')

#2017��������а����ҵ
copSet2017 = set(rank500[(rank500['rank_2016'].notnull()) & (rank500['rank'].isnull())]['nameCn_2016'])
cotDropInd2017 = data5002016[data5002016['nameCn'].isin(copSet2017)].groupby('ind').size().sort_values(ascending=False)
cotDropInd2017.plot(kind='barh')
cotDropCot2017 = data5002016[data5002016['nameCn'].isin(copSet2017)].groupby('countryCn').size().sort_values(ascending=False)
cotDropCot2017.plot(kind='barh')

#2016,2017������ҵ����Ƚ�
cotDropInd = pd.DataFrame([cotDropInd2016,cotDropInd2017])
cotDropInd.index = [2016,2017]
cotDropInd = cotDropInd.T.fillna(0).sort_values(by=2017,ascending=False)
cotDropInd.plot(kind='barh')


#����һֱ�Ȳ�����
alwaysUp = set(rank500[(rank500['rank_last_2015']>=rank500['rank_2015']) & (rank500['rank_last_2016']>=rank500['rank_2016']) & (rank500['rank_last']>=rank500['rank']) & (rank500['rank_2015'] != 999) & (rank500['rank_2016'] != 999) & (rank500['rank'] != 999)]['nameCn'])
cotUpInd = data5002017[data5002017['nameCn'].isin(alwaysUp)].groupby('ind').size().sort_values(ascending=False)
cotUpInd.plot(kind='barh')
cotUpCountry = data5002017[data5002017['nameCn'].isin(alwaysUp)].groupby('countryCn').size().sort_values(ascending=False)
cotUpCountry.plot(kind='barh')


#ÿ����������ҵ������
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

data5002017[data5002017['countryCn']=='�й�'].groupby('ind').size().sort_values(ascending=False).plot(kind='pie')

data5002017[data5002017['countryCn']=='����'].groupby('ind').size().sort_values(ascending=False).plot(kind='pie')
