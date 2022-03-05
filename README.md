由于捐款人的文档大小超过300MB，不能上传，非常抱歉

要按照步骤运行，才能生成所需要的的数据文件，否则跨步骤运行会出错

首先运行txt_to_csv.py，将所有txt文件转化为csv文件

其次运行candidate.py，将所有候选人信息与捐款人信息进行自然连接，从而排除掉无关数据，并为接下来打好基础

第一个生成热度图，调用all_state.csv中的文件，生成state_trans.csv后，运行ReDuTu.py即可生成热度图

第二个生成折线图，在ZheXianTu.py中，调用all_date.csv和cand_three.csv中的文件，按照日期将之前所有金额相加，由此以日期为横坐标，总金额为纵坐标，生成折线图

第三个生成词云图，在file_name.py中，将捐款人信息放入name.txt中，在CiYunTu.py中，按照出现次数来决定名字的大小
