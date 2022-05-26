import os
import datetime
from PIL import Image
from importlib_metadata import metadata


with open('index_page.html','r',encoding='UTF-8') as f :
    htmls = f.readlines()
    # print(htmls)



# print(''.join(htmls[42:44]))

j=1
with open(f'index_pagesss.html','w',encoding='UTF-8') as f :
    cmt = ''.join(htmls[:22])
    f.write(cmt)
    # f.write('testsss')
    if j == 0 :
        f.write(f'\t\t\t\t<button type="button" class="btn btn-primary" onclick="location.href=\'index_page{1}.html\'" disabled >Previous</button>\n')
    else :
        f.write(f'\t\t\t\t<button type="button" class="btn btn-primary" onclick="location.href=\'index_page{1}.html\'" >Previous</button>\n')
    
    cmt = ''.join(htmls[23:25])
    print(cmt)
    f.write(cmt)
    
    x = j+1
    for i in range(1,22):
        if i == x :
            f.write(f'\t\t\t\t<button type=\"button\" class=\"btn btn-primary\" onclick=\"location.href=\'index_page{i}.html\'\"disabled >{i}</button>\n')
        
        else :
            f.write(f'\t\t\t\t<button type=\"button\" class=\"btn btn-primary\" onclick=\"location.href=\'index_page{i}.html\'\">{i}</button>\n')
    
    cmt = ''.join(htmls[46:48])
    f.write(cmt)
    
    if j==21 :
        f.write(f'\t\t\t\t<button type="button" class="btn btn-primary" onclick="location.href=\'index_page{1}.html\'" disabled >Next</button>\n')
    else :
        f.write(f'\t\t\t\t<button type="button" class="btn btn-primary" onclick="location.href=\'index_page{1}.html\'" >Next</button>\n')
    
    cmt = ''.join(htmls[49:52])
    f.write(cmt)
    
    for i in range(1,16) :
        
        imgfile = f"D:/imgs/origin/{i+1}_1.jpg"
        img = Image.open(imgfile)

        meta_data = img._getexif()
        list = meta_data[36867].split(' ')
        list2 = list[0].split(':')

        f.write(f'\t\t\t\t<img src=\"images/{+i}_1.webp\" class=\"img_set\">\n')
        f.write(f'\t\t\t\t<h6>{list2[0]} {list2[1]} {list2[2]}</h6>\n')
        
    cmt = ''.join(htmls[67:72])
    f.write(cmt)
    
    if j == 0 :
        f.write(f'\t\t\t\t<button type="button" class="btn btn-primary" onclick="location.href=\'index_page{1}.html\'" disabled >Previous</button>\n')
    else :
        f.write(f'\t\t\t\t<button type="button" class="btn btn-primary" onclick="location.href=\'index_page{1}.html\'" >Previous</button>\n')
    
    cmt = ''.join(htmls[73:75])
    f.write(cmt)
    
    
    for i in range(1,22):
        if i == x :
            f.write(f'\t\t\t\t<button type=\"button\" class=\"btn btn-primary\" onclick=\"location.href=\'index_page{i}.html\'\"disabled >{i}</button>\n')
        
        else :
            f.write(f'\t\t\t\t<button type=\"button\" class=\"btn btn-primary\" onclick=\"location.href=\'index_page{i}.html\'\">{i}</button>\n')
    
    cmt = ''.join(htmls[96:98])
    f.write(cmt)
    
    if j==21 :
        f.write(f'\t\t\t\t<button type="button" class="btn btn-primary" onclick="location.href=\'index_page{j}.html\'" disabled >Next</button>\n')
    else :
        f.write(f'\t\t\t\t<button type="button" class="btn btn-primary" onclick="location.href=\'index_page{j}.html\'" >Next</button>\n')
    
    
    cmt = ''.join(htmls[99:])
    f.write(cmt)
        
    

# print(htmls[62])


# "\n".join(htmls)