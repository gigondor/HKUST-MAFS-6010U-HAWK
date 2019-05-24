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
stop_word.add("two")
stop_word.add("said")
stop_word.add("technology")
stop_word.add("still")
stop_word.add("addition")
stop_word.add("improve")
stop_word.add("many")
stop_word.add("promote")
stop_word.add("make")
stop_word.add("method")
stop_word.add("result")
stop_word.add("cc")
stop_word.add("become")
stop_word.add("better")
stop_word.add("work")
stop_word.add("need")
stop_word.add("based")
stop_word.add("cc cc")
stop_word.add("important")
stop_word.add("provide")
stop_word.add("achieve")
stop_word.add("used")

f = open("C:/Users/zgxue/Desktop/data/QE/2019_05.txt", "r")

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


