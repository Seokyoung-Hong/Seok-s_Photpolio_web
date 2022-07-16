import os
import datetime
from PIL import Image
from importlib_metadata import metadata
import pandas as pd
import pickle
from module import *


with open('index_country.html','r',encoding='UTF-8') as f :
    htmls = f.readlines()
    # print(htmls)



# print(''.join(htmls[42:44]))

df = pd.read_excel('img_data.xlsx')
table = df.to_dict()

# place_list = ['Switzerland','Germany','France','Italia','Monaco','Austria','Nederland','Spain','Russia','South Korea']
place_list = []
for img in table['place']:
    if table['place'][img] not in place_list and str(table['place'][img]) != 'nan':
        place_list.append(str(table['place'][img]))
        

with open('tags.pickle','rb') as f :
    tag_list = pickle.load(f)
df2 = pd.read_csv('Yolo/tags.csv')
table2 = df2.to_dict

# print(tag_list)
for c_name in place_list :
    with open(f'pages/place/{c_name}.html','w',encoding='UTF-8') as f :
        # print(table)
        
        
        index1 = search(htmls, '<link rel="canonical" href="https://seok.tk/pages/index_page0.html">')
        html_copy(f,htmls,1,index1)
        f.write(f'\t<link rel="canonical" href="https://seok.tk/pages/place/{c_name}.html">\n')
        
        index2 = search(htmls, '<div class="btn-group" role="group" aria-label="Basic radio toggle button group">')
        html_copy(f,htmls,index1+2,index2)
        # buttons(f,j,21)
        
        f.write(f'\t\t<h2>{c_name}</h2>\n')
        
        f.write('\t\t<p>\n')
        
        for i in range(1,317) :
            insert_img(f,i,table,tag_list,c_name,place=True)
        
        index3 = search(htmls,'</body>')
        index4 = search(htmls, '<footer>')+1
        html_copy(f,htmls,index3,index4)

# buttons(f,j,21)

        index5 = search(htmls, '<div id="footer">')+1
        end = search(htmls,'</html>') +1
        html_copy(f,htmls,index5,end)

print('HTML pages made well')