# coding = utf-8
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image,ImageSequence
reload(sys)
sys.setdefaultencoding('utf-8')

image = Image.open('D:/$Python data analysis/500/cloud.jpg')
graph = np.array(image)
font=os.path.join("C:/Windows/Fonts/SIMYOU.TTF")   
mytext= open('D:/$Python data analysis/500/2017_ind.txt').read().decode('utf-8')
wordcloud = WordCloud(font_path=font,background_color = 'white',mask = graph).generate(mytext)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('D:/$Python data analysis/500/2017_ind.png',dpi=400,bbox_inches='tight')