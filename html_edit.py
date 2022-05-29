import os
import datetime
from PIL import Image
from importlib_metadata import metadata


def buttons(f,j,button_count):
    f.write('        <div class="btn-group" role="group" aria-label="Basic radio toggle button group">\n')
    f.write('            <div class="btn-group me-3" aria-label="Previous">\n')
    # f.write('testsss')
    if j == 0 :
        f.write(f'\t\t\t\t<button type="button" class="btn btn-primary" onclick="location.href=\'pages/index_page{j+1}.html\'" disabled >Previous</button>\n')
    else :
        f.write(f'\t\t\t\t<button type="button" class="btn btn-primary" onclick="location.href=\'pages/index_page{j}.html\'" >Previous</button>\n')
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
            f.write(f'\t\t\t\t<button type=\"button\" class=\"btn btn-primary\" onclick=\"location.href=\'pages/index_page{i}.html\'\"disabled >{i}</button>\n')
        
        else :
            f.write(f'\t\t\t\t<button type=\"button\" class=\"btn btn-primary\" onclick=\"location.href=\'pages/index_page{i}.html\'\">{i}</button>\n')
    f.write('        </div>\n')
    f.write('            <div class="btn-group me-3" aria-label="next">\n')
    if j+1 == button_end :
        f.write(f'\t\t\t\t<button type="button" class="btn btn-primary" onclick="location.href=\'pages/index_page{j+1}.html\'" disabled >Next</button>\n')
    else :
        f.write(f'\t\t\t\t<button type="button" class="btn btn-primary" onclick="location.href=\'pages/index_page{j+2}.html\'" >Next</button>\n')

    f.write('            </div>\n')
    f.write('        </div>\n')
    
    

def html_copy(f,h,a,b) :
    cmt = ''.join(h[a-1:b])
    f.write(cmt)



with open('index_page.html','r',encoding='UTF-8') as f :
    htmls = f.readlines()
    # print(htmls)



# print(''.join(htmls[42:44]))

for j in range(22):
    with open(f'pages/index_page{j+1}.html','w',encoding='UTF-8') as f :
        
        html_copy(f,htmls,1,20)
        buttons(f,j,21)
        
        f.write('\t\t<p>\n')
        
        for i in range(1,16) :
            
            imgfile = f"D:/imgs/origin/{i+1}_1.jpg"
            img = Image.open(imgfile)

            meta_data = img._getexif()
            list = meta_data[36867].split(' ')
            list2 = list[0].split(':')
            
            f.write(f'\t\t\t\t<img src=\"images/{j*15+i}_1.webp\" class=\"img_set\">\n')
            f.write(f'\t\t\t\t<h6>\n\t\t\t\t\t{list2[0]} {list2[1]} {list2[2]}\n')
            f.write(f'\t\t\t\t\t<a href="images/{j*15+i}_1.webp" target="_blank">open image bigger</a>\n')
            f.write('\t\t\t\t</h6>\n')
            
        html_copy(f,htmls,68,71)
        
        buttons(f,j,21)
        
        html_copy(f,htmls,102,109)