import pandas as pd
file = pd.read_csv('all_name.csv', low_memory=False)
file1 = pd.read_csv('cand_max.csv', low_memory=False)
cand0 = file['CAND_ID']
cmte0 = file['CMTE_ID']
name0 = file['NAME']
money0 = file['TRANSACTION_AMT']
cand_max = file1['CAND_ID']
df = pd.concat([cand0, cmte0, name0, money0], axis=1)
list_cmte = list()
filename = 'name.txt' #存储向获得捐款最多的候选人捐款的捐款人名字
for cand in cand_max:
    for cmte in df[df['CAND_ID'] == cand]['CMTE_ID']:
        list_cmte.append(cmte)
list_cmte1 = pd.DataFrame(list_cmte, columns=['cmte'])
cmte1 = list_cmte1['cmte'].drop_duplicates().reset_index(drop=True) #删除重复行并重置索引
with open(filename, 'w') as file:
    file.close()
for cmte in cmte1:
    if not df.loc[df['CMTE_ID'] == cmte].empty:
        x = df.loc[df['CMTE_ID'] == cmte].reset_index(drop=True)
        for name in x['NAME']:
            namea = name.split(', ')[0] #提取名字
            with open(filename, 'a') as file:
                file.write(namea)
                file.write(' ')
                file.close()
