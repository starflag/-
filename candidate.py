import pandas as pd
file_CAND = pd.read_csv('weball20.csv', low_memory=False)
file_CAND_CMTE = pd.read_csv('ccl.csv', low_memory=False)
file_CMTE = pd.read_csv('itcont.csv', low_memory=False)
cand_id1 = file_CAND['CAND_ID'] #候选人文件中候选人ID
cand_id2 = file_CAND_CMTE['CAND_ID'] #连接文件中候选人ID
cmte_id1 = file_CAND_CMTE['CMTE_ID'] #连接文件中捐款人ID
cmte_id2 = file_CMTE['CMTE_ID'] #捐款人文件中捐款人ID
money = file_CMTE['TRANSACTION_AMT'] #捐款人文件中捐款金额
name0 = file_CMTE['NAME'] #捐款人文件中捐款人姓名
date0 = file_CMTE['TRANSACTION_DT'] #捐款人文件中捐款日期
state = file_CMTE['STATE'] #捐款人文件中捐款人所在的州
cand_cmte0 = pd.concat([cand_id2, cmte_id1], axis=1) #候选人ID与捐款人ID合并（笛卡尔积）
cand_cmte = pd.merge(cand_cmte0, cand_id1) #选出位于候选人文件中候选人ID与捐款人ID，去除无捐款人的候选人（自然连接）
cmet_money0 = pd.concat([cmte_id2, money], axis=1) #捐款人ID与金额合并
cand_cmet_money = pd.merge(cand_cmte, cmet_money0) #选出位于捐款人文件中捐款人ID与金额，去除无金额的捐款人
cmte_name = pd.concat([cmte_id2, name0], axis=1) #捐款人ID与姓名合并
cmte_date = pd.concat([cmte_id2, date0], axis=1) #捐款人ID与日期合并
cmte_state = pd.concat([cmte_id2, state], axis=1) #捐款人ID与州合并
money_sum = list()
cand_ID = cand_cmet_money['CAND_ID'].drop_duplicates().reset_index(drop=True) #删除重复行并重置索引
for cand in cand_ID:
    money_sum.append(cand_cmet_money[cand_cmet_money['CAND_ID'] == cand]['TRANSACTION_AMT'].sum())
money_sum1 = pd.DataFrame(money_sum, columns=['money'])
cand_money = pd.concat([cand_ID, money_sum1], axis=1)
cand_max = cand_money['CAND_ID'][cand_money['money'] == max(money_sum)] #找到获得捐款最多的候选人ID
cand_max.to_csv('cand_max.csv') #存储获得捐款最多的候选人ID
cand_three = cand_money.sort_values(by='money', ascending=False)
cand_three.iloc[:3].to_csv('cand_three.csv') #存储获得捐款前3的候选人ID
cmte_name_money = pd.concat([cmte_name, money], axis=1, ignore_index=False)
cmte_date_money = pd.concat([cmte_date, money], axis=1, ignore_index=False)
cmte_state_money = pd.concat([cmte_state, money], axis=1, ignore_index=False)
all_name = pd.merge(cand_cmte, cmte_name_money)
all_name.to_csv('all_name.csv')
all_date = pd.merge(cand_cmte, cmte_date_money)
all_date.to_csv('all_date.csv')
all_date = pd.merge(cand_cmte, cmte_state_money)
all_date.to_csv('all_state.csv')

