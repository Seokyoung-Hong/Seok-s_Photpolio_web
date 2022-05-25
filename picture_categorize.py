import os
import datetime
from PIL import Image
from importlib_metadata import metadata

imgfile = "D:/imgs/origin/1_1.jpg"

img = Image.open(imgfile)

meta_data = img._getexif()
list = meta_data[36867].split(' ')
list2 = list[0].split(':')


data_head = "<!DOCTYPE html>\n<html>\n\thead>\n\t\t<meta charset=\"UTF-8\">\n\t\t<meta name=\"description\" content = \"Photpolio\">\n\t\t<meta name=\"kewards\" content=\"HTML, CSS\">\n\t\t<meta name=\"author\" content=\"Seok(SiO2)\">\n\t\t<link rel=\"stylesheet\" href=\"style.css\">\n\t\t<link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor\" crossorigin=\"anonymous\">\n\t\t<script type=\"text/javascript\">\n\t\t\t\tdocument.oncontextmenu = function(){return false;}\n\t\t</script>\n\t\t<title>Seok's Photpolio</title>\n\t</head>\n\t<body class = \"background text margin\" oncontextmenu=\"return false\" onselectstart=\"return false\" ondragstart=\"return false\" onkeydown=\"return false\">\n\t\t<p>\n\t\t\t\t<h1>\n\t\t\t\tSeok's Photpolio\n\t\t\t\t</h1>\n\t\t</p>\n\t\t<div class=\"btn-group me-3\" aria-label=\"First group\">"

data_button_1 = "<button type=\"button\" class=\"btn btn-primary\" onclick=\"location.href=\'index_page1.html\'\">1</button>"
data_button_2 = "<button type=\"button\" class=\"btn btn-primary\" onclick=\"location.href=\'index_page1.html\'\"disabled >1</button>"

def button_1(a,b):
    if a==b :
        data_button = f"<button type=\"button\" class=\"btn btn-primary\" onclick=\"location.href=\'index_page{a}.html\'\"disabled >{a}</button>"
    else :
        data_button = f"<button type=\"button\" class=\"btn btn-primary\" onclick=\"location.href=\'index_page{a}.html\'\">{a}</button>"


# ctime = os.path.getctime("images/1_1.webp")
# mtime = os.path.getmtime("images/1_1.webp")
# atime = os.path.getatime("images/1_1.webp")
# os.path.getsize("images/1_1.webp")

# print(datetime.datetime.fromtimestamp(ctime))
