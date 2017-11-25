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


wc = WordCloud(max_words=1000, margin=10,
               random_state=1).generate(text)

# store default colored image
default_colors = wc.to_array()
plt.title("Custom colors")
plt.imshow(random_state=3, interpolation="bilinear")
wc.to_file("a_new_dope.png")
plt.axis("off")
plt.figure()
plt.title("Default colors")
plt.imshow(default_colors, interpolation="bilinear")
plt.axis("off")
plt.show()