# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:27:18 2017

@author: dacrands
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud


text = open(r"nyt-categories.txt").read()

mask = np.array(Image.open('nyt-logo.jpg'))

wc = WordCloud(width=1600, height=800, mask=mask).generate(text)

plt.figure(figsize=(20,10))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")

plt.savefig('nytLogoCloud.jpg', facecolor='k', bbox_inches='tight')
plt.show()
