# %%
#reading html content from vinted listing page
from bs4 import BeautifulSoup
import requests
import json

with open('input_file.json','r') as f:
    data =json.load(f)

test_url =data[0]['url']
header = {'User-Agent':'Mozilla/5.0'}
r =requests.get(test_url, headers =header)



soup = BeautifulSoup(r.text, 'html.parser')

# %%
# first attempt to get image urls
with open('test_response.html','w',
          encoding ='utf-8') as f:
    f.write(soup.prettify())

links =soup.find_all('link',href =True)

img_urls =[link['href'] for link  \
           in links if link['href'].startswith( \
               'https://images1.vinted.net')]

# img_urls =soup.find_all('link',
#                         href =lambda x:
#                         x and \
#                         x.startswith( \
#                             'https://images1.vinted.net'))

# %%
# the above method does not work well, try other methods
# save the html content to a file for inspection
with open('test_response.html','w',
          encoding ='utf-8') as f:
    f.write(soup.prettify())
#pythonic selector
img_urls =soup.find_all('img', attrs={'data-testid': \
                                     lambda x: x and x.startswith( \
                                    'item-photo-') and x.endswith('--img')}
                                    )
# css language selector
img_urls =soup.select("img[data-testid^='item-photo-'][data-testid$='--img']")
# regex selector
import re
img_urls =soup.find_all('img', attrs={'data-testid': re.compile( \
    r'^item-photo-.*--img$')})
img_url = [img['src'] for img in img_urls if img.get('src')]
len(img_url)
img_ur= set(img_url)
# %%
#break down of urls
# url: scheme://netloc/path;parameters?query#fragment
#netloc: domain:port, example: www.example.com:80 

# the above methods do not work well, try other methods
# extract all urls from the html content
# use urlparse to parse and filter the urls
# retain only those that match the image url pattern

from urllib.parse import urlparse
import re
from collections import Counter

urls =re.findall(r'https?://[^\s"\'<>]+',soup.prettify())
urls =[u.rstrip("\\") for u in urls]  # remove trailing backslash or single quote
url_cand =[]
for url in urls:
    
    parsed_url =urlparse(url)
    if 'images1.vinted.net' not in parsed_url.netloc:
        
        continue
    if 'f800' not in parsed_url.path:
        
        continue
    if not parsed_url.path.endswith(('.webp','.jpg','.jpeg','.png')):
        
        continue
    normalized_url =parsed_url.geturl()
    url_cand.append(normalized_url)
url =list(dict.fromkeys(url_cand))  # remove duplicates while preserving order list

basename = [urlparse(u).path.split('/')[-1] for u in url]
most_common_basename, _ =Counter(basename).most_common(1)[0]

foto_urls =[u for u in url if most_common_basename in u]
#%%
#extract title and description
#obtain title
title =soup.find_all('title')[0].get_text(strip=True).split('|')[0]

#obtain description
description =soup.find_all('meta',
                           attrs={'name':'description'}) \
                            [0]['content']
# %%
#save images and text to local files

import requests
img_url =foto_urls[0]
header = {'User-Agent':'Mozilla/5.0'}
r =requests.get(img_url,headers =header)
img_file_name =img_url.split('/')[-1]
with open(f'{title}/{img_file_name}.jpg','wb') as f:
    f.write(r.content)

with open(f'{title}/description.txt','w',encoding ='utf-8') as f:
    f.write(description)

with open(f'{title}/title.txt','w',encoding ='utf-8') as f:
    f.write(title)

# %%
