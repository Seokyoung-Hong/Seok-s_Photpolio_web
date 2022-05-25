import os
import datetime
from PIL import Image
from importlib_metadata import metadata



for j in range(22):
    with open('index_page.html','r',encoding='UTF-8') as f :
        htmls = f.readlines()
        # print(htmls)



    # print(''.join(htmls[42:44]))


    with open(f'index_page{j+1}.html','w',encoding='UTF-8') as f :
        cmt = ''.join(htmls[:22])
        f.write(cmt)
        x = j+1
        for i in range(1,22):
            if i == x :
                f.write(f'\t\t<button type=\"button\" class=\"btn btn-primary\" onclick=\"location.href=\'index_page{i}.html\'\"disabled >{i}</button>\n')
            
            else :
                f.write(f'\t\t<button type=\"button\" class=\"btn btn-primary\" onclick=\"location.href=\'index_page{i}.html\'\">{i}</button>\n')
        
        cmt = ''.join(htmls[45:47])
        f.write(cmt)
        
        for i in range(1,16) :
            
            imgfile = "D:/imgs/origin/1_1.jpg"
            img = Image.open(imgfile)

            meta_data = img._getexif()
            list = meta_data[36867].split(' ')
            list2 = list[0].split(':')

            f.write(f'\t\t<img src=\"images/{j*15+i}_1.webp\" class=\"img_set\">\n')
            f.write(f'\t\t<h6>{list2[0]} {list2[1]} {list2[2]}</h6>\n')
            
        cmt = ''.join(htmls[62:70])
        f.write(cmt)
        for i in range(1,22):
            if i == x :
                f.write(f'\t\t<button type=\"button\" class=\"btn btn-primary\" onclick=\"location.href=\'index_page{i}.html\'\"disabled >{i}</button>\n')
            
            else :
                f.write(f'\t\t<button type=\"button\" class=\"btn btn-primary\" onclick=\"location.href=\'index_page{i}.html\'\">{i}</button>\n')
        
        cmt = ''.join(htmls[93:])
        f.write(cmt)

        
    

# print(htmls[62])


# "\n".join(htmls)