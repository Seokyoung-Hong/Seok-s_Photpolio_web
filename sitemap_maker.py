import os
import datetime

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
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    priority = 1
    f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    time = datetime.datetime.fromtimestamp(os.path.getmtime(f'index.html'))
    time_str = time.isoformat()
    f.write(f'\t<url>\n')
    f.write(f'\t\t<loc> https://seok.tk/ </loc>\n')
    f.write(f'\t\t<priority> {priority} </priority>\n')
    f.write(f'\t\t<lastmod> {time_str} </lastmod>\n')
    f.write(f'\t</url>\n')
    priority = 0.8
    for i in home :
        time = datetime.datetime.fromtimestamp(os.path.getmtime(f'{i}'))
        time_str = time.isoformat()
        f.write(f'\t<url>\n')
        f.write(f'\t\t<loc> https://seok.tk/{i} </loc>\n')
        f.write(f'\t\t<priority> {priority} </priority>\n')
        f.write(f'\t\t<lastmod> {time_str} </lastmod>\n')
        f.write(f'\t</url>\n')
    
    priority = 0.5
    for i in country :
        time = datetime.datetime.fromtimestamp(os.path.getmtime(f'pages/country/{i}'))
        time_str = time.isoformat()
        f.write(f'\t<url>\n')
        f.write(f'\t\t<loc>https://seok.tk/pages/country/{i}</loc>\n')
        f.write(f'\t\t<priority> {priority} </priority>\n')
        f.write(f'\t\t<lastmod> {time_str} </lastmod>\n')
        f.write(f'\t</url>\n')
    priority = 0.5
    for i in tag :
        time = datetime.datetime.fromtimestamp(os.path.getmtime(f'pages/tag/{i}'))
        time_str = time.isoformat()
        f.write(f'\t<url>\n')
        f.write(f'\t\t<loc>https://seok.tk/pages/tag/{i}</loc>\n')
        f.write(f'\t\t<priority> {priority} </priority>\n')
        f.write(f'\t\t<lastmod> {time_str} </lastmod>\n')
        f.write(f'\t</url>\n')
    
    priority = 0.4
    for i in pages :
        time = datetime.datetime.fromtimestamp(os.path.getmtime(f'pages/{i}'))
        time_str = time.isoformat()
        f.write(f'\t<url>\n')
        f.write(f'\t\t<loc>https://seok.tk/pages/{i}</loc>\n')
        f.write(f'\t\t<priority> {priority} </priority>\n')
        f.write(f'\t\t<lastmod> {time_str} </lastmod>\n')
        f.write(f'\t</url>\n')
    f.write('</urlset>')