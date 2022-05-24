f = open("htmls.txt", 'w')
for i in range(1, 187):
    data = f"<img src=\"images/{i}_1.jpg\" class=\"img_set\">\n"
    f.write(data)
f.close()