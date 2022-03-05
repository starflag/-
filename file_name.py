import csv
import pandas as pd
import numpy as np
file = pd.read_csv('all_name.csv', low_memory=False)
cand0 = file['CAND_ID']
cmte0 = file['CMTE_ID']
name0 = file['NAME']
money0 = file['TRANSACTION_AMT']
df = pd.concat([cand0, cmte0, name0, money0], axis=1)
list_cmte = list()
list_name = list()
list_money = list()
cand_ID = df['CAND_ID'].drop_duplicates().reset_index(drop=True) #提取出所有不重复的houxuanrID
for cand in cand_ID:
    list_money.append(df[df['CAND_ID'] == cand]['TRANSACTION_AMT'].sum())
money_sum = pd.DataFrame(list_money, columns=['money'])
cand_money = pd.concat([cand_ID, money_sum], axis=1)
cand_max = cand_money['CAND_ID'][cand_money['money'] == max(list_money)]
cand_max.to_csv('cand_max.csv') #存储获得捐款最多的候选人ID
cand_three = cand_money.sort_values(by='money', ascending=False)
cand_three.iloc[:3].to_csv('cand_three.csv') #存储获得捐款前三的候选人ID
filename = 'name.txt' #存储向获得捐款最多的候选人捐款的捐款人名字
for cand in cand_max:
    for cmte in df[df['CAND_ID'] == cand]['CMTE_ID']:
        list_cmte.append(cmte)
for i in range(len(list_cmte)):
    if not df.loc[df['CMTE_ID'] == list_cmte[i]].empty:
        x = df.loc[df['CMTE_ID'] == list_cmte[i]].reset_index(drop=True)
        for name in x['NAME']:
            namea = name.split(', ')[0]
            with open(filename, 'a') as file:
                file.write(namea)
                file.write(' ')
                file.close()
            # print(namea)
        # y.to_csv('name_trans.csv')
# .reset_index(drop=True)