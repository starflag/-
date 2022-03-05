import pandas as pd
file_CMTE = pd.read_csv('all_state.csv', low_memory=False)
state = file_CMTE['STATE']
TRANSACTION = file_CMTE['TRANSACTION_AMT']
where = {'AL':0, 'AK':0, 'AZ':0, 'AR':0, 'CA':0, 'CO':0, 'CT':0, 'DE':0, 'FL':0, 'GA':0, 'HI':0, 'ID':0, 'IL':0
         , 'IN':0, 'IA':0, 'KS':0, 'KY':0, 'LA':0, 'ME':0, 'MD':0, 'MA':0, 'MI':0, 'MN':0, 'MS':0, 'MO':0, 'MT':0
         , 'NE':0, 'NV':0, 'NH':0, 'NJ':0, 'NM':0, 'NY':0, 'NC':0, 'ND':0, 'OH':0, 'OK':0, 'OR':0, 'PA':0, 'RI':0
         , 'SC':0, 'SD':0, 'TN':0, 'TX':0, 'UT':0, 'VT':0, 'VA':0, 'WA':0, 'WV':0, 'WI':0, 'WY':0}
money = [0]*50
for i in range(len(state)):
    if state[i]=='AL':
        money[0] = money[0] + TRANSACTION[i]
        s1 = {'AL':money[0]}
        where.update(s1)
    if state[i]=='AK':
        money[1] = money[1] + TRANSACTION[i]
        s1 = {'AK':money[1]}
        where.update(s1)
    if state[i]=='AZ':
        money[2] = money[2] + TRANSACTION[i]
        s1 = {'AZ':money[2]}
        where.update(s1)
    if state[i]=='AR':
        money[3] = money[3] + TRANSACTION[i]
        s1 = {'AR':money[3]}
        where.update(s1)
    if state[i]=='CA':
        money[4] = money[4] + TRANSACTION[i]
        s1 = {'CA':money[4]}
        where.update(s1)
    if state[i]=='CO':
        money[5] = money[5] + TRANSACTION[i]
        s1 = {'CO':money[5]}
        where.update(s1)
    if state[i]=='CT':
        money[6] = money[6] + TRANSACTION[i]
        s1 = {'CT':money[6]}
        where.update(s1)
    if state[i]=='DE':
        money[7] = money[7] + TRANSACTION[i]
        s1 = {'DE':money[7]}
        where.update(s1)
    if state[i]=='FL':
        money[8] = money[8] + TRANSACTION[i]
        s1 = {'FL':money[8]}
        where.update(s1)
    if state[i]=='GA':
        money[9] = money[9] + TRANSACTION[i]
        s1 = {'GA':money[9]}
        where.update(s1)
    if state[i]=='HI':
        money[10] = money[10] + TRANSACTION[i]
        s1 = {'HI':money[10]}
        where.update(s1)
    if state[i]=='ID':
        money[11] = money[11] + TRANSACTION[i]
        s1 = {'ID':money[11]}
        where.update(s1)
    if state[i]=='IL':
        money[12] = money[12] + TRANSACTION[i]
        s1 = {'IL':money[12]}
        where.update(s1)
    if state[i]=='IN':
        money[13] = money[13] + TRANSACTION[i]
        s1 = {'IN':money[13]}
        where.update(s1)
    if state[i]=='IA':
        money[14] = money[14] + TRANSACTION[i]
        s1 = {'IA':money[14]}
        where.update(s1)
    if state[i]=='KS':
        money[15] = money[15] + TRANSACTION[i]
        s1 = {'KS':money[15]}
        where.update(s1)
    if state[i]=='KY':
        money[16] = money[16] + TRANSACTION[i]
        s1 = {'KY':money[16]}
        where.update(s1)
    if state[i]=='LA':
        money[17] = money[17] + TRANSACTION[i]
        s1 = {'LA':money[17]}
        where.update(s1)
    if state[i]=='ME':
        money[18] = money[18] + TRANSACTION[i]
        s1 = {'ME':money[18]}
        where.update(s1)
    if state[i]=='MD':
        money[19] = money[19] + TRANSACTION[i]
        s1 = {'MD':money[19]}
        where.update(s1)
    if state[i]=='MA':
        money[20] = money[20] + TRANSACTION[i]
        s1 = {'MA':money[20]}
        where.update(s1)
    if state[i]=='MI':
        money[21] = money[21] + TRANSACTION[i]
        s1 = {'MI':money[21]}
        where.update(s1)
    if state[i]=='MN':
        money[22] = money[22] + TRANSACTION[i]
        s1 = {'MN':money[22]}
        where.update(s1)
    if state[i]=='MS':
        money[23] = money[23] + TRANSACTION[i]
        s1 = {'MS':money[23]}
        where.update(s1)
    if state[i]=='MO':
        money[24] = money[24] + TRANSACTION[i]
        s1 = {'MO':money[24]}
        where.update(s1)
    if state[i]=='MT':
        money[25] = money[25] + TRANSACTION[i]
        s1 = {'MT':money[25]}
        where.update(s1)
    if state[i]=='NE':
        money[26] = money[26] + TRANSACTION[i]
        s1 = {'NE':money[26]}
        where.update(s1)
    if state[i]=='NV':
        money[27] = money[27] + TRANSACTION[i]
        s1 = {'NV':money[27]}
        where.update(s1)
    if state[i]=='NH':
        money[28] = money[28] + TRANSACTION[i]
        s1 = {'NH':money[28]}
        where.update(s1)
    if state[i]=='NJ':
        money[29] = money[29] + TRANSACTION[i]
        s1 = {'NJ':money[29]}
        where.update(s1)
    if state[i]=='NM':
        money[30] = money[30] + TRANSACTION[i]
        s1 = {'NM':money[30]}
        where.update(s1)
    if state[i]=='NY':
        money[31] = money[31] + TRANSACTION[i]
        s1 = {'NY':money[31]}
        where.update(s1)
    if state[i]=='NC':
        money[32] = money[32] + TRANSACTION[i]
        s1 = {'NC':money[32]}
        where.update(s1)
    if state[i]=='ND':
        money[33] = money[33] + TRANSACTION[i]
        s1 = {'ND':money[33]}
        where.update(s1)
    if state[i]=='OH':
        money[34] = money[34] + TRANSACTION[i]
        s1 = {'OH':money[34]}
        where.update(s1)
    if state[i]=='OK':
        money[35] = money[35] + TRANSACTION[i]
        s1 = {'OK':money[35]}
        where.update(s1)
    if state[i]=='OR':
        money[36] = money[36] + TRANSACTION[i]
        s1 = {'OR':money[36]}
        where.update(s1)
    if state[i]=='PA':
        money[37] = money[37] + TRANSACTION[i]
        s1 = {'PA':money[37]}
        where.update(s1)
    if state[i]=='RI':
        money[38] = money[38] + TRANSACTION[i]
        s1 = {'RI':money[38]}
        where.update(s1)
    if state[i]=='SC':
        money[39] = money[39] + TRANSACTION[i]
        s1 = {'SC':money[39]}
        where.update(s1)
    if state[i]=='SD':
        money[40] = money[40] + TRANSACTION[i]
        s1 = {'SD':money[40]}
        where.update(s1)
    if state[i]=='TN':
        money[41] = money[41] + TRANSACTION[i]
        s1 = {'TN':money[41]}
        where.update(s1)
    if state[i]=='TX':
        money[42] = money[42] + TRANSACTION[i]
        s1 = {'TX':money[42]}
        where.update(s1)
    if state[i]=='UT':
        money[43] = money[43] + TRANSACTION[i]
        s1 = {'UT':money[43]}
        where.update(s1)
    if state[i]=='VT':
        money[44] = money[44] + TRANSACTION[i]
        s1 = {'VT':money[44]}
        where.update(s1)
    if state[i]=='VA':
        money[45] = money[45] + TRANSACTION[i]
        s1 = {'VA':money[45]}
        where.update(s1)
    if state[i]=='WA':
        money[46] = money[46] + TRANSACTION[i]
        s1 = {'WA':money[46]}
        where.update(s1)
    if state[i]=='WV':
        money[47] = money[47] + TRANSACTION[i]
        s1 = {'WV':money[47]}
        where.update(s1)
    if state[i]=='WI':
        money[48] = money[48] + TRANSACTION[i]
        s1 = {'WI':money[48]}
        where.update(s1)
    if state[i]=='WY':
        money[49] = money[49] + TRANSACTION[i]
        s1 = {'WY':money[49]}
        where.update(s1)
STATE = {'state': ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL'
         , 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT'
         , 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI'
         , 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'],
         'transaction': money}
df=pd.DataFrame.from_dict(STATE)
df.to_csv('state_trans.csv')