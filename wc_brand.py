from wordcloud import WordCloud
fontpath='SourceHanSansCN-Regular.otf'

text=''
with open('./brand.txt','r') as f:
    text=f.read()
    f.close()
print(text[:1000])

wc = WordCloud(font_path=fontpath,  # 设置字体
               background_color="white",  # 背景颜色
               max_words=1000,  # 词云显示的最大词数
               max_font_size=500,  # 字体最大值
               min_font_size=20, #字体最小值
               random_state=42, #随机数
               collocations=False, #避免重复单词
               width=1600,height=1200,margin=10, #图像宽高，字间距，需要配合下面的plt.figure(dpi=xx)放缩才有效
              )
wc.generate(text)

#cell-4
import matplotlib.pyplot as plt
plt.figure(dpi=100) #通过这里可以放大或缩小
plt.imshow(wc, interpolation='catrom',vmax=1000)
plt.axis("off") #隐藏坐标
plt.show()



#参考：https://www.jianshu.com/p/656c978764cb
# 字体需要下载
