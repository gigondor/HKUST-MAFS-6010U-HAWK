#GovRptWordCloudv2.py
import jieba
import wordcloud
from scipy.misc import imread
mask = imread("fivestar.png")

excludes = { }

stop_word = set(wordcloud.STOPWORDS)
stop_word.add("旷视")
stop_word.add("方式")
stop_word.add("我国")
stop_word.add("方面")
stop_word.add("需要")
stop_word.add("需求")
stop_word.add("一些")
stop_word.add("基于")
stop_word.add("其中")
stop_word.add("当中")
stop_word.add("但是")
stop_word.add("比如")
stop_word.add("随着")
stop_word.add("进一步")
stop_word.add("整个")
stop_word.add("这些")
stop_word.add("两个")
stop_word.add("多个")
stop_word.add("这个")
stop_word.add("开始")
stop_word.add("非常")
stop_word.add("商汤科技")
stop_word.add("商汤")
stop_word.add("科技")
stop_word.add("我们")
stop_word.add("人工智能")
stop_word.add("AI")
stop_word.add("实现")
stop_word.add("合作")
stop_word.add("技术")
stop_word.add("提供")
stop_word.add("推动")
stop_word.add("已经")
stop_word.add("成为")
stop_word.add("同时")
stop_word.add("提升")
stop_word.add("能够")
stop_word.add("通过")
stop_word.add("共同")
stop_word.add("目前")
stop_word.add("以及")
stop_word.add("包括")
stop_word.add("此次")
stop_word.add("不断")
stop_word.add("双方")
stop_word.add("进行")
stop_word.add("打造")
stop_word.add("可以")
stop_word.add("对于")
stop_word.add("表示")
stop_word.add("作为")
stop_word.add("带来")
stop_word.add("一个")
stop_word.add("不同")
stop_word.add("领域")


f = open("C:/Users/zgxue/Desktop/data/QC/alltime_cn.txt", "r")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)

w = wordcloud.WordCloud(\
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc", mask = mask, stopwords = stop_word
    )

w.generate(txt)

w.to_file("wordcloudfivestar.png")


