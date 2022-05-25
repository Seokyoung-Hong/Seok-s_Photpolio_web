
for j in range(22):
    f = open(f"texts/html_{j+1}.txt", 'w')
    for i in range(0,15):
        data = f"\t\t\t<img src=\"images/{j*15+i+1}_1.webp\" class=\"img_set\">\n"
        f.write(data)
    f.close()
    
    
    

    