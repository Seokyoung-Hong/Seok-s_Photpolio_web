import os
import datetime
from PIL import Image
from importlib_metadata import metadata
import pandas as pd
import pickle
from module import *


'''
def insert_img(f,i,table, tag_list) :
    if i == 145 or i == 146 :
        return 0
    country_name = ''
    placetext = ''
    if 'nan' != str(table['country'][i-1]) :
        country_name = '{}'.format(table['country'][i-1])
        # placetext = '{}'.format(table['country'][i-1])
        if 'nan' != str(table['place'][i-1]) :
            placetext = '{}'.format(table['place'][i-1])
            
            if 'nan' != str(table['place2'][i-1]) :
                placetext = placetext+', {}\n'.format(table['place2'][i-1])
            else :
                placetext = placetext + '\n'
        else :
            placetext = placetext + '\n'
    
    # imgfile = f"D:/imgs/origin/{i}_1.jpg"
    # img = Image.open(imgfile)

    # meta_data = img._getexif()
    # list = meta_data[36867].split(' ')
    # list2 = list[0].split(':')
    
    f.write(f'\t\t\t<a href="https://sio2.pe.kr/images/{i}_1.webp" target="_blank">\n')
    f.write(f'\t\t\t\t<img src=\"https://sio2.pe.kr/images/{i}_1.webp\" class=\"img_set\">\n')
    f.write(f'\t\t\t</a>\n')
    f.write(f'\t\t\t<h4>\n')
    # f.write(f'\t\t\t\t\t{list2[0]} {list2[1]} {list2[2]}\n')
    if country_name != '' :
        f.write(f'\t\t\t\t<a href="https://sio2.pe.kr/pages/country/{country_name}.html" style="text-decoration: none;" title="{country_name}" target="_self"> {country_name} </a>\n')
    f.write(f'\t\t\t\t{placetext}\n')
    count = False
    for tag in tag_list :
        if str(i) in tag_list[tag] :
            count = True
    if count :
        f.write(f'\t\t\t\t<details class = "tag_summary">\n')
        f.write(f'\t\t\t\t<summary>Tags</summary>\n')
        f.write(f'\t\t\t\t<p>\n')
        for tag in tag_list :
            if str(i) in tag_list[tag] :
                f.write('\t\t\t\t<a class = "tag" href="https://sio2.pe.kr/pages/tag/{}.html" style ="text-decoration: none;" target="_self"> {} </a>\n'.format(tag,tag))
        
        f.write(f'\t\t\t\t</details>\n')
    
    f.write('\t\t\t</h4>\n')
'''

with open('index_page.html', 'r', encoding='UTF-8') as f:
    htmls = f.readlines()
    # print(htmls)

with open('tags.pickle', 'rb') as f:
    tag_list = pickle.load(f)


# print(''.join(htmls[42:44]))

for j in range(21):
    with open(f'pages/index_page{j+1}.html', 'w', encoding='UTF-8') as f:
        df = pd.read_excel('img_data.xlsx')
        table = df.to_dict()
        # print(table)

        index1 = search(htmls, '<link rel="canonical" href="')
        html_copy(f, htmls, 1, index1)
        f.write(
            f'\t\t<link rel="canonical" href="https://sio2.pe.kr/pages/index_page{j}.html">\n')

        index2 = search(
            htmls, '<div class="btn-group" role="group" aria-label="Basic radio toggle button group">')
        html_copy(f, htmls, index1+2, index2)

        buttons(f, j, 21)

        f.write('\t\t<p>\n')

        for i in range(j*15+1, j*15+16):
            insert_img(f, i, table, tag_list)

        index3 = search(htmls, '</body>')
        index4 = search(htmls, '<footer>')+1
        html_copy(f, htmls, index3, index4)

        buttons(f, j, 21)

        index5 = search(htmls, '<div id="footer">')+1
        end = search(htmls, '</html>') + 1
        html_copy(f, htmls, index5, end)

print('HTML pages made well')
