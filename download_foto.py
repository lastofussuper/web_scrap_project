# %%
import json


with open('input_file.json','r') as f:
    foto_urls =json.load(f)


print(len(foto_urls))
print(foto_urls[:5])

# %%
test_url =next(iter(foto_urls[0].values()))
# test_url =foto_urls[0]['url']

import requests
header ={'User-Agent':'Mozilla/5.0'}

r = requests.get(test_url, headers =header)
print(r.status_code)
print('length:', len(r.text))
print(r.text[:300])
# %%
# Read web DNAs from html pages
# There are several styles of embedding structured data in html pages
# Here are examples of 3 most common styles
# style one ld +json 
# (ld as load, most common, good for search engine optimization) 
# the data is embedded in a <script> tag with type "application/ld+json" 
# rather than being directly in html tags. The purpose of this 
# structure is to provide
# a standardized format for search engines and 
# other applications to extract and understand
# the data about products, reviews, events, and 
# other entities on a web page.

# <!DOCTYPE html>
# <html>
# <head>
#   <script type="application/ld+json">
#   {
#     "@type": "Product",
#     "name": "Leather Belt",
#     "description": "Genuine leather belt",
#     "image": [
#       "https://img1.jpg",
#       "https://img2.jpg"
#     ]
#   }
#   </script>
# </head>
# <body>
#   <h1>Leather Belt</h1>
# </body>
# </html>
# <!DOCTYPE html>
#to read such data, we can simply do below:
#data =json.loads(script.string)
#data['name'], data['description'], data['image']




# style two microdata: __NEXT_DATA__ 
# the data is embedded in a <script> tag with id "__NEXT_DATA__" and
#type "application/json", the real data structure is nested 
# insde several layers of props and pageProps.The purpose
# of this structure is to support server-side rendering 
# and client-side navigation
#in Next.js applications.
# <!DOCTYPE html>
# <html>
# <head>
#   <script id="__NEXT_DATA__" type="application/json">
#   {
#     "props": {
#       "pageProps": {
#         "item": {
#           "title": "Leather Belt",
#           "description": "Genuine leather belt",
#           "photos": [
#             {"url": "https://img1.jpg"},
#             {"url": "https://img2.jpg"}
#           ]
#         }
#       }
#     }
#   }
#   </script>
# </head>
# <body>
#   <div id="__next"></div>
# </body>
# </html>
# to read such data, we can simply do below:
# data = json.loads(script.string)
# item = data["props"]["pageProps"]["item"]
# item["title"]
# item["photos"][0]["url"]

# style three: 
# plain html tags, no special script tag
# the data is directly embedded in html tags such as <h1>, <div>, <img>
# the purpose of this structure is to provide
# a simple and human-readable format for displaying
# data on a web page.

# <!DOCTYPE html>
# <html>
# <body>
#   <h1 class="title">Leather Belt</h1>
#   <div class="desc">Genuine leather belt</div>
#   <img src="https://img1.jpg">
#   <img src="https://img2.jpg">
# </body>
# </html>

# to read such data, we can use BeautifulSoup to parse html
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html_content, 'html.parser')
# title = soup.find('h1', class_='title').text
# description = soup.find('div', class_='desc').text
# images = [img['src'] for img in soup.find_all('img')]








# %%
# check the actual html content of a sample url
from bs4 import BeautifulSoup
soup =BeautifulSoup(r.text, 'html.parser')
# %%
