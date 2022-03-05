import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
from matplotlib.pyplot import rcParams
file = pd.read_csv('all_date.csv', low_memory=False)
file_cand_three = pd.read_csv('cand_three.csv', low_memory=False)
cand0 = file['CAND_ID']
cmte0 = file['CMTE_ID']
date0 = file['TRANSACTION_DT']
money0 = file['TRANSACTION_AMT']
df = pd.concat([cand0, cmte0, date0, money0], axis=1)
cand_three0 = file_cand_three['CAND_ID']
cand_three = pd.merge(cand_three0, df).drop('CMTE_ID', axis=1)
# DT_MY为date_money缩写
DT_MY = cand_three.groupby(['CAND_ID', 'TRANSACTION_DT'], as_index=False)['TRANSACTION_AMT'].sum()
DT_MY1 = DT_MY.loc[DT_MY['CAND_ID'].isin([cand_three0.iloc[0]])].drop('CAND_ID', axis=1)
DT_MY2 = DT_MY.loc[DT_MY['CAND_ID'].isin([cand_three0.iloc[1]])].drop('CAND_ID', axis=1)
DT_MY3 = DT_MY.loc[DT_MY['CAND_ID'].isin([cand_three0.iloc[2]])].drop('CAND_ID', axis=1)
# 将金额累加
DT_MY1['money'] = DT_MY1['TRANSACTION_AMT'].cumsum()
DT_MY2['money'] = DT_MY2['TRANSACTION_AMT'].cumsum()
DT_MY3['money'] = DT_MY3['TRANSACTION_AMT'].cumsum()
# 去掉原来每日金额的纵列并重置索引
DT_MY1 = DT_MY1.drop('TRANSACTION_AMT', axis=1).reset_index(drop=True)
DT_MY2 = DT_MY2.drop('TRANSACTION_AMT', axis=1).reset_index(drop=True)
DT_MY3 = DT_MY3.drop('TRANSACTION_AMT', axis=1).reset_index(drop=True)
for i in range(len(DT_MY1)):
    DT_MY1.loc[i, 'TRANSACTION_DT'] = (DT_MY1.loc[i, 'TRANSACTION_DT'] - 2020) / 1000000
for j in range(len(DT_MY2)):
    DT_MY2.loc[j, 'TRANSACTION_DT'] = (DT_MY2.loc[j, 'TRANSACTION_DT'] - 2020) / 1000000
for k in range(len(DT_MY3)):
    DT_MY3.loc[k, 'TRANSACTION_DT'] = (DT_MY3.loc[k, 'TRANSACTION_DT'] - 2020) / 1000000
str1 = cand_three0.iloc[0]
str2 = cand_three0.iloc[1]
str3 = cand_three0.iloc[2]
fig = plt.figure(figsize=(13,7))
time =pd.to_datetime(np.arange(0,30), unit='D',origin=pd.Timestamp('2020-07-22'))
plt.plot(time, DT_MY1['money'], c = 'red', label = str1)
plt.plot(time, DT_MY2['money'], c = 'yellow', label = str2)
plt.plot(time, DT_MY3['money'], c = 'blue', label = str3)
plt.legend()
plt.xlabel('date')
plt.ylabel('money')
ax = plt.subplot(111)
ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))
plt.xticks(pd.date_range(time[0], time[-1], freq='D'),rotation=45)
plt.title('ZheXianTu')
plt.savefig('ZheXianTu.jpg')
plt.show()

# print(DT_MY)

