import html_parser 

#html_parser.html_parser('http://feeds.nbcnews.com/nbcnews/public/us-news', 'link')


#print('html_parser.tags')

import pandas as pd
import matplotlib.pyplot as plt

material_per = {'Earth_Part': [71,18,7,4]}
dataframe = pd.DataFrame(material_per,columns=['Earth_Part'],index = ['Water','Mineral','Sand','Metals'])

dataframe.plot.pie(y='Earth_Part',figsize=(7, 7),autopct='%1.1f%%', startangle=90)
plt.show()
