import numpy as np
import pandas as pd
import jieba
import wordcloud
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

sns.set(font='SimHei')

stop_list = pd.read_csv('停用词.txt', engine='python',encoding='utf-8', names=['t'])['t'].tolist()


df = pd.read_excel('B站弹幕数据more.xlsx')

def txt_cut(f):
    return [w for w in jieba.cut(f) if w not in stop_list]

word_list = []#保存分词后的词
for line in df[df['弹幕'].notnull()]['弹幕'].tolist():
    for word in txt_cut(line):
        word_list.append(word)

result = " ".join(word_list)  # 必须给每个符号分隔开分词结果,否则不能绘制词云
# 1、初始化自定义背景图片
image = Image.open(r'timg.png')
#导入的图片会直接导致最终形成的云图效果，需要一次次生成查看和调试
graph = np.array(image)

# 2、产生词云图
# 有自定义背景图：生成词云图由自定义背景图像大小决定
wc = wordcloud.WordCloud(
                         font_path=r"msyh.ttf",#字体地址
                         background_color='white',#背景色
                         max_font_size=100,#显示字体最大值
                         #max_words=100,  # 最大词数
                         mask=graph) #导入的图片
wc.generate(result)

# 3、绘制文字的颜色以背景图颜色为参考
image_color = wordcloud.ImageColorGenerator(graph)  # 从背景图片生成颜色值
wc.recolor(color_func=image_color)
wc.to_file(r"史上第一混乱cloud.png")  # 按照背景图大小保存绘制好的词云图，比下面程序显示更清晰

# 4、显示图片
plt.title("史上第一混乱词云图")  # 指定所绘图名称
plt.imshow(wc)  # 以图片的形式显示词云
plt.axis("off")  # 关闭图像坐标系
plt.show()
