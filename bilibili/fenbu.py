import pandas as pd
from matplotlib import pyplot as plt


# 加载中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

title_size = 20
label_size = 14
df = pd.read_excel('B站弹幕数据more.xlsx')
# 评论字数分布
df['评论字数'] = df['弹幕'].str.len()#相当于新增了一列评论数字
# df['整理弹幕字数']=df['评论字数']
# df['整理弹幕字数'].loc[df['评论字数']>25]=25#此处有疑问，如何写大于多少的直方图
df.to_excel('弹幕数量.xlsx')

# print(df['评论字数'].mean())
plt.figure(figsize=(12, 5))
plt.title('弹幕字数数据分布', fontsize=title_size)

df['评论字数'].hist(bins=10, edgecolor='white', color='#f5a045')
plt.grid(linestyle='--')
plt.xlabel('字幕数量', fontsize=label_size)
plt.ylabel('计数', fontsize=label_size)
plt.savefig('弹幕字数数据分布直方图.png')
