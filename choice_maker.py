import os
import datetime
from PIL import Image
from importlib_metadata import metadata
import pandas as pd
import pickle
from module import *
from glob import glob

with open('index_country.html','r',encoding='UTF-8') as f :
    htmls = f.readlines()
    # print(htmls)

df = pd.read_excel('img_data.xlsx')
table = df.to_dict()

country_list = []
for img in table['country']:
    if table['country'][img] not in country_list and str(table['country'][img]) != 'nan':
        country_list.append(str(table['country'][img]))


with open('tags.pickle','rb') as f :
    tag_list = pickle.load(f)
df2 = pd.read_csv('Yolo/tags.csv')
table2 = df2.to_dict

choice_list = glob('pages/*/')

choice_name = []
for i in choice_list :
    temp = i.split('\\')[1]
    choice_name.append(temp)
print(choice_list,choice_name)


for choice in choice_name :
    with open(f'{choice}_choice.html','w',encoding='UTF-8') as f:
        index1 = search(htmls, '<link rel="canonical" href="https://seok.tk/pages/index_page0.html">')
        html_copy(f,htmls,1,index1)
        f.write(f'\t<link rel="canonical" href="https://seok.tk/{choice}_choice.html">\n')
        
        index2 = search(htmls, '<div class="btn-group" role="group" aria-label="Basic radio toggle button group">')
        html_copy(f,htmls,index1+2,index2)
        f.write(f'\t\t<h2>{choice} lists</h2>\n\t\t<ul type="square">\n')
        file_list = os.listdir(f'pages/{choice}')
        for file_name in file_list :
            f.write(f'\t\t\t<li><a style="text-decoration: none; font-size: 120%;" href="https://seok.tk/pages/{choice}/{file_name}" target="_self"> {file_name[:-5]} </a></li>\n')
        f.write('\t\t</ul>\n')
        f.write('\t</body>\n')
        f.write('\t<footer>\n')
        
        index3 = search(htmls, '<p class = "footer text">Taken by Seok_young Hong</p>')
        html_copy(f,htmls,index3,-1)
        f.write('</html>')
        











'''
# print(tag_list)
for c_name in country_list :
    with open(f'pages/country/{c_name}.html','w',encoding='UTF-8') as f :
        # print(table)
        
        
        index1 = search(htmls, '<link rel="canonical" href="https://seok.tk/pages/index_page0.html">')
        html_copy(f,htmls,1,index1)
        f.write(f'\t<link rel="canonical" href="https://seok.tk/pages/country/{c_name}.html">\n')
        
        index2 = search(htmls, '<div class="btn-group" role="group" aria-label="Basic radio toggle button group">')
        html_copy(f,htmls,index1+2,index2)
        # buttons(f,j,21)
        
        f.write(f'\t\t<h2>{c_name}</h2>\n')
        
        f.write('\t\t<p>\n')
        
        for i in range(1,317) :
            insert_img(f,i,table,tag_list,c_name)
        
        index3 = search(htmls,'</body>')
        index4 = search(htmls, '<footer>')+1
        html_copy(f,htmls,index3,index4)

# buttons(f,j,21)

        index5 = search(htmls, '<div id="footer">')+1
        end = search(htmls,'</html>') +1
        html_copy(f,htmls,index5,end)
'''
'''
print('HTML pages made well')
'''