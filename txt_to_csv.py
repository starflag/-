import csv
# 将所有txt文件转化为csv文件
csvFile = open("./weball20.csv",'w',newline='',encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("data/weball20.txt",'r',encoding='GB2312')
for line in f:
    csvRow = line.split("|")
    writer.writerow(csvRow)

f.close()
csvFile.close()



csvFile = open("./ccl.csv",'w',newline='',encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("data/ccl.txt",'r',encoding='GB2312')
for line in f:
    csvRow = line.split("|")
    writer.writerow(csvRow)

f.close()
csvFile.close()



csvFile = open("./itcont_2020_20200722_20200820.csv",'w',newline='',encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("data/itcont_2020_20200722_20200820.txt",'r',encoding='GB2312')
for line in f:
    csvRow = line.split("|")
    writer.writerow(csvRow)

f.close()
csvFile.close()
