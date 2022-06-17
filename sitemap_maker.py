import os

home = ['index.html','index_country.html','index_tag.html','index_page.html']


pages = os.listdir('pages/')
for n,i in enumerate(pages) :
    if '.html' not in i :
        pages.pop(n)

tag = os.listdir('pages/tag/')
for n,i in enumerate(tag) :
    if '.html' not in i :
        tag.pop(n)

country = os.listdir('pages/country')
for n,i in enumerate(country) :
    if '.html' not in i :
        country.pop(n)

with open('sitemap.xml','w') as f :
    f.write('<?xml version="1.0" encoding="UTF-8"?>')
    priority = 1000
    f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    f.write(f'\t<url>\n\t\t<loc>https://photpolio-seok.netlify.app/</loc>\n\t\t<priority>{priority}</priority>\n\t</url>\n')
    priority = 800
    for i in home :
        f.write(f'\t<url>\n\t\t<loc>https://photpolio-seok.netlify.app/{i}</loc>\n\t\t<priority>{priority}</priority>\n\t</url>\n')
    
    priority = 700
    for i in country :
        f.write(f'\t<url>\n\t\t<loc>https://photpolio-seok.netlify.app/pages/country/{i}</loc>\n\t\t<priority>{priority}</priority>\n\t</url>\n')
    
    priority = 600
    for i in tag :
        f.write(f'\t<url>\n\t\t<loc>https://photpolio-seok.netlify.app/pages/tag/{i}</loc>\n\t\t<priority>{priority}</priority>\n\t</url>\n')
    
    priority = 300
    for i in pages :
        f.write(f'\t<url>\n\t\t<loc>https://photpolio-seok.netlify.app/pages/{i}</loc>\n\t\t<priority>{priority}</priority>\n\t</url>\n')
    f.write('</urlset>')