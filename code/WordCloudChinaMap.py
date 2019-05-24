#GovRptWordCloudv2.py
import jieba
import wordcloud
from scipy.misc import imread
mask = imread("chinamap.jpg")
excludes = {}
stop_word = set(wordcloud.STOPWORDS)
stop_word.add("AI")
stop_word.add("SenseTime")
stop_word.add("will")
stop_word.add("company")
stop_word.add("world")
stop_word.add("research")
stop_word.add("new")
stop_word.add("year")
stop_word.add("artificial intelligence")
stop_word.add("one")
stop_word.add("said")
stop_word.add("technology")

f = open("C:/Users/zgxue/Desktop/data/SE/2019_05.txt", "r")

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
w.to_file("wordcloudchinamap1905.png")


