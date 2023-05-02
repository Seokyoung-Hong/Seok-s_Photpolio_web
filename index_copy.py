import os
import datetime
from PIL import Image
from importlib_metadata import *
from module import *

with open('index_copy.html', 'r', encoding='UTF-8') as f:
    htmls = f.readlines()
    # print(htmls)


# print(''.join(htmls[42:44]))


with open(f'index.html', 'w', encoding='UTF-8') as f:
    a = 13
    changes = a - 13
    index1 = search(htmls, '<div class="carousel-inner">')
    html_copy(f, htmls, 1, index1)
    # buttons(f,j,21)

    for i in range(1, 317):
        if i in [32, 38, 68, 74, 75, 85, 129, 130, 135, 160, 195, 196, 230, 262, 263, 265, 268, 274, 275, 276, 279, 284, 298, 290, 292, 293, 296, 303, 306, 307, 311, 312, 313, 316]:
            continue
        if i == 1:
            f.write('\t\t\t\t\t<div class="carousel-item active">\n')
        else:
            f.write('\t\t\t\t\t<div class="carousel-item">\n')
        f.write(
            f'\t\t\t\t\t<img src="https://sio2.pe.kr/images/{i}_1.webp" class="d-block w-100" alt="{i}_1.webp">\n')
        f.write('\t\t\t\t\t</div>\n')

    # html_copy(f,htmls,47,71)
    index2 = search(htmls, '<button class="carousel-control-prev"')
    index3 = search(htmls, '</html>')
    html_copy(f, htmls, index2, index3)
    f.write('</html>')

print('HTML pages copied well')
