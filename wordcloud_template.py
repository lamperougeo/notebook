# -*- coding = utf-8 -*-
# @Time : 2021/4/13 10:30
# Author : Lelouch
# @File : wordcloud_template.py
# @Software : PyCharm

import jieba
from wordcloud import WordCloud
from imageio import imread
from time import *

#程序内容：对文本文档生成词云图
#需修改的参数：1、文本文件地址  2、模版图片JPG文件地址  3、Wrodcloud参数


#记录开始时间
starttime = time()
def create_wordcloud():
    #读取文本文件
    with open('text.txt', "r", encoding='UTF-8') as f:
        text = f.read()  # 读取文件内容

    # 对文本进行分词
    cut_text = ''.join(jieba.lcut(text))

    #读取图片
    color_mask = imread('模版图片.jpg')

    #调整词云图参数
    cloud = WordCloud(
                        font_path="msyh.ttc",   #字体
                      background_color="white", #背景颜色
                      mask=color_mask,        #词云图背景
                      max_words=1200,         #允许最大词汇
                      max_font_size=20,       # 最大号字体
                      scale = 1.5             #图片范围
                    )


    #生成词云图
    word_cloud = cloud.generate(cut_text)


    #统计程序运行时间
    endtime = time()
    print('该程序共耗时：%.2f秒'%(endtime - starttime))

    # 词云图保存地址
    filename = "词云图" + str(strftime("%Y-%m-%d"))+'.jpg'
    #保存词云图
    cloud.to_file(filename)
    print("保存的文件名为"+filename)


create_wordcloud()

