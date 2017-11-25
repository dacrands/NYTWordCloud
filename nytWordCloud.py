# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:27:18 2017

@author: dacrands
"""

import matplotlib.pyplot as plt
from wordcloud import WordCloud


text = open(r"nyt-categories.txt").read()

wc = WordCloud(width=1600, height=800).generate(text)

plt.figure(figsize=(20,10))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")

plt.savefig('nytWordCloud.jpg', facecolor='k', bbox_inches='tight')
plt.show()
