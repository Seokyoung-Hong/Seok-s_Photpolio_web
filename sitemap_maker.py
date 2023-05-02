import os
import datetime

home = ['country_choice.html', 'tag_choice.html']


pages = os.listdir('pages/')
for n, i in enumerate(pages):
    if i[-5:] != '.html':
        pages.pop(n)

tag = os.listdir('pages/tag/')
for n, i in enumerate(tag):
    if i[-5:] != '.html':
        tag.pop(n)

country = os.listdir('pages/country')
for n, i in enumerate(country):
    if i[-5:] != '.html':
        country.pop(n)

place = os.listdir('pages/place')
for n, i in enumerate(place):
    if i[-5:] != '.html':
        place.pop(n)

video = os.listdir('Video')
for n, i in enumerate(country):
    if i[-5:] != '.html':
        country.pop(n)

with open('sitemap.xml', 'w', encoding='UTF-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    priority = 1
    # f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    f.write('<urlset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xhtml="http://www.w3.org/1999/xhtml" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd" xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    time = datetime.datetime.fromtimestamp(os.path.getmtime(f'index.html'))
    time_str = time.isoformat()
    f.write(f'\t<url>\n')
    f.write(f'\t\t<loc>https://sio2.pe.kr/</loc>\n')
    f.write(f'\t\t<lastmod>{time_str}</lastmod>\n')
    f.write(f'\t\t<priority>{priority}</priority>\n')
    f.write(f'\t</url>\n')
    priority = 0.8
    for i in home:
        time = datetime.datetime.fromtimestamp(os.path.getmtime(f'{i}'))
        time_str = time.isoformat()
        f.write(f'\t<url>\n')
        f.write(f'\t\t<loc>https://sio2.pe.kr/{i}</loc>\n')
        f.write(f'\t\t<lastmod>{time_str}</lastmod>\n')
        f.write(f'\t\t<priority>{priority}</priority>\n')
        f.write(f'\t</url>\n')

    priority = 0.5
    for i in country:
        time = datetime.datetime.fromtimestamp(
            os.path.getmtime(f'pages/country/{i}'))
        time_str = time.isoformat()
        f.write(f'\t<url>\n')
        f.write(f'\t\t<loc>https://sio2.pe.kr/pages/country/{i}</loc>\n')
        f.write(f'\t\t<lastmod>{time_str}</lastmod>\n')

        f.write(f'\t\t<priority>{priority}</priority>\n')
        f.write(f'\t</url>\n')

    priority = 0.5
    for i in place:
        time = datetime.datetime.fromtimestamp(
            os.path.getmtime(f'pages/place/{i}'))
        time_str = time.isoformat()
        f.write(f'\t<url>\n')
        f.write(f'\t\t<loc>https://sio2.pe.kr/pages/place/{i}</loc>\n')
        f.write(f'\t\t<lastmod>{time_str}</lastmod>\n')

        f.write(f'\t\t<priority>{priority}</priority>\n')
        f.write(f'\t</url>\n')

    priority = 0.5
    for i in tag:
        time = datetime.datetime.fromtimestamp(
            os.path.getmtime(f'pages/tag/{i}'))
        time_str = time.isoformat()
        f.write(f'\t<url>\n')
        f.write(f'\t\t<loc>https://sio2.pe.kr/pages/tag/{i}</loc>\n')
        f.write(f'\t\t<lastmod>{time_str}</lastmod>\n')

        f.write(f'\t\t<priority>{priority}</priority>\n')
        f.write(f'\t</url>\n')

    priority = 0.4
    for i in pages:
        time = datetime.datetime.fromtimestamp(os.path.getmtime(f'pages/{i}'))
        time_str = time.isoformat()
        f.write(f'\t<url>\n')
        f.write(f'\t\t<loc>https://sio2.pe.kr/pages/{i}</loc>\n')
        f.write(f'\t\t<lastmod>{time_str}</lastmod>\n')

        f.write(f'\t\t<priority>{priority}</priority>\n')
        f.write(f'\t</url>\n')

    priority = 0.6
    for i in video:
        time = datetime.datetime.fromtimestamp(os.path.getmtime(f'Video/{i}'))
        time_str = time.isoformat()
        f.write(f'\t<url>\n')
        f.write(f'\t\t<loc>https://sio2.pe.kr/Video/{i}</loc>\n')
        f.write(f'\t\t<lastmod>{time_str}</lastmod>\n')

        f.write(f'\t\t<priority>{priority}</priority>\n')
        f.write(f'\t</url>\n')
    f.write('</urlset>')

with open('sitemap.txt', 'w') as f:
    for i in home:
        f.write(f'https://sio2.pe.kr/{i}\n')
    for i in country:
        f.write(f'https://sio2.pe.kr/pages/country/{i}\n')
    for i in place:
        f.write(f'https://sio2.pe.kr/pages/place/{i}\n')
    for i in tag:
        f.write(f'https://sio2.pe.kr/pages/tag/{i}\n')
    for i in pages:
        f.write(f'https://sio2.pe.kr/pages/{i}\n')
    for i in video:
        f.write(f'https://sio2.pe.kr/Video/{i}')
print('sitemap made well')
