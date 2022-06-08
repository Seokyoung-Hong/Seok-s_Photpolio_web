import os
import datetime
from PIL import Image
from importlib_metadata import metadata
import pandas as pd
import pickle

def buttons(f,j,button_count):
    f.write('        <div class="btn-group" role="group" aria-label="Basic radio toggle button group">\n')
    f.write('            <div class="btn-group me-3" aria-label="Previous">\n')
    # f.write('testsss')
    if j == 0 :
        f.write(f'\t\t\t\t<button type="button" class="btn btn-primary" onclick="location.href=\'index_page{j+1}.html\'" disabled >Previous</button>\n')
    else :
        f.write(f'\t\t\t\t<button type="button" class="btn btn-primary" onclick="location.href=\'index_page{j}.html\'" >Previous</button>\n')
    f.write('            </div>\n')
    f.write('            <div class="btn-group me-3" aria-label="First group"\n>')
    
    
    if j < 5:
        button_start = 1
        button_end = 9
        # print('if')
    
    elif j > button_count-5 :
        button_start = button_count - 8
        button_end = button_count
        # print('else')
    else :
        button_start = j-3
        button_end = j+5
        # print('elif')
    for i in range(button_start,button_end+1):
        if i == j+1 :
            f.write(f'\t\t\t\t<button type=\"button\" class=\"btn btn-primary\" onclick=\"location.href=\'index_page{i}.html\'\"disabled >{i}</button>\n')
        
        else :
            f.write(f'\t\t\t\t<button type=\"button\" class=\"btn btn-primary\" onclick=\"location.href=\'index_page{i}.html\'\">{i}</button>\n')
    f.write('        </div>\n')
    f.write('            <div class="btn-group me-3" aria-label="next">\n')
    if j+1 == button_end :
        f.write(f'\t\t\t\t<button type="button" class="btn btn-primary" onclick="location.href=\'index_page{j+1}.html\'" disabled >Next</button>\n')
    else :
        f.write(f'\t\t\t\t<button type="button" class="btn btn-primary" onclick="location.href=\'index_page{j+2}.html\'" >Next</button>\n')

    f.write('            </div>\n')
    f.write('        </div>\n')
    
    

def html_copy(f,h,a,b) :
    cmt = ''.join(h[a-1:b])
    f.write(cmt)

def insert_img(f,i,table, tag_list) :
    
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
    
    f.write(f'\t\t\t<a href="../images/{i}_1.webp" target="_blank">\n')
    f.write(f'\t\t\t\t<img src=\"../images/{i}_1.webp\" class=\"img_set\">\n')
    f.write(f'\t\t\t</a>\n')
    f.write(f'\t\t\t<h4>\n')
    # f.write(f'\t\t\t\t\t{list2[0]} {list2[1]} {list2[2]}\n')
    if country_name != '' :
        f.write(f'\t\t\t\t<a href="country/{country_name}.html" style="text-decoration: none;" title="{country_name}" target="_self"> {country_name} </a>\n')
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
                f.write('\t\t\t\t<a class = "tag" href="tag/{}.html" style ="text-decoration: none;" target="_self"> {} </a>\n'.format(tag,tag))
        
        f.write(f'\t\t\t\t</details>\n')
    
    f.write('\t\t\t</h4>\n')

with open('index_page.html','r',encoding='UTF-8') as f :
    htmls = f.readlines()
    # print(htmls)

with open('tags.pickle','rb') as f :
    tag_list = pickle.load(f)


# print(''.join(htmls[42:44]))

for j in range(21):
    with open(f'pages/index_page{j+1}.html','w',encoding='UTF-8') as f :
        df = pd.read_excel('img_data.xlsx')
        table = df.to_dict()
        # print(table)
        
        html_copy(f,htmls,1,44)
        buttons(f,j,21)
        
        f.write('\t\t<p>\n')
        
        for i in range(j*15+1,j*15+16) :
            insert_img(f,i,table, tag_list)

        html_copy(f,htmls,92,99)
        
        buttons(f,j,21)
        
        html_copy(f,htmls,121,134)

print('HTML pages made well')