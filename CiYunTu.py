import matplotlib.pyplot as plt
import jieba
from wordcloud import wordcloud

# 1.读出词语
with open('name.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    wc = wordcloud.WordCloud(
        background_color='white', # 背景颜色
        width=1000, #宽
        height=600, #高
        max_font_size=50, # 字体最大大小
        min_font_size=10, #字体最小大小
        max_words=5000,
        collocations=False #防止每个单词出现两次
    )
    wc.generate(text)
    wc.to_file('ciyun.jpg')  # 图片保存

# # 5.显示图片
# plt.figure('images/jielun')  # 图片显示的名字
# plt.imshow(wc)
# plt.axis('off')  # 关闭坐标
# plt.show()