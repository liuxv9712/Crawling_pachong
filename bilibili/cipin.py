# 评论词频
import pandas as pd
from matplotlib import pyplot as plt
import jieba
import wordcloud
import seaborn as sns

sns.set(font='SimHei')
stop_list = pd.read_csv('停用词.txt', engine='python',encoding='utf-8', names=['t'])['t'].tolist()
df = pd.read_excel('B站弹幕数据more.xlsx')

def txt_cut(f):
    return [w for w in jieba.cut(f) if w not in stop_list]
'''
分词cut
jieba.cut()分词提供了多种模式：全模式，精确模式，搜索引擎模式
全模式：速度块，扫描成词的词语，但时会出现歧义的词语
精确模式：尽可能最准确非切分词语，比较适合作文本分析
搜索引擎模式：就是精确模式的基础上，对长词再次切分，提高召回率
运行后出现：
Building prefix dict from the default dictionary ...
Loading model from cache C:\...\jieba.cache
Loading model cost 1.538 seconds.
Prefix dict has been built succesfully.
说明加载词库成功
'''
word_list = []#保存分词后的词
for line in df[df['弹幕'].notnull()]['弹幕'].tolist():
    for word in txt_cut(line):
        word_list.append(word)
# print(word_list)
#画词频分布图
word_count = pd.Series(word_list).value_counts().sort_values(ascending=False)[0:50]
# Series结构是基于NumPy的ndarray结构，是一个一维的标签矩阵（感觉跟python里的字典结构有点像）
word_count.to_excel('词频50.xlsx')

word_count2 = word_count.dropna()

fig = plt.figure(figsize=(15, 8))  # 创建一个图形是咧 大小是15*8（长*宽）单位是英寸
x = word_count.index.tolist()  # 获取的是index列，转换成list
y = word_count.values.tolist()  # 获取的是values列，转换成list
sns.barplot(x, y, palette="BuPu_r")
# barplot是作图方法，传入xy值，palette="BuPu_r" 设置的是柱状图的颜色样式。
# #BuPu_r 从左到右，颜色由深到浅，BuPu与之相反
plt.title('词频Top20')
plt.ylabel('count')
# 如果不加这句，那么出现的就是个四方的框，这个是用来溢出轴脊柱的，加上bottom=tur，意思就是连下方的轴脊柱也溢出
sns.despine(bottom=True)
plt.savefig('词频统计.png', dpi=400)
# plt.show()

