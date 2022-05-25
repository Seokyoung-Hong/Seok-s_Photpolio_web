
for j in range(10):
    f = open(f"texts/html_{j+1}.txt", 'w')
    for i in range(1,21):
        data = f"<img src=\"images/{j*20+i}_1.jpg\" class=\"img_set\">\n"
        f.write(data)
    f.close()