#GovRptWordCloudv1.py
import jieba
import wordcloud
f = open("SensetimeEn.txt", "r")
t = f.read()
f.close()
ls = jieba.lcut(t)

txt = " ".join(ls)
w = wordcloud.WordCloud( \
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc", max_words = 15
    )
w.generate(txt)
w.to_file("wordcloud.png")


