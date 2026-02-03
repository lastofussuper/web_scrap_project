import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
from collections import Counter
import os
import json

class ImgTitleDesc:
    def __init__(self, url):
        self.url =url
        self.soup =None
        self.img_urls =[]
        self.title =''
        self.description =''
        self.header ={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
                 "Accept-Language":"pl,en;q=0.9",
                 "Referer":"https://www.vinted.pl/"}
    def fetch_content(self):
        import requests
        
        header =self.header
        r =requests.get(self.url, headers =header,timeout =20)
        if r.status_code !=200:
            return None,r.status_code
        
        self.soup =BeautifulSoup(r.text,'html.parser')

        return self.soup, r.status_code
    def extract_img_urls(self):
        soup =self.soup
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
        url =list(dict.fromkeys(url_cand))  # remove duplicates while preserving order

        basename = [urlparse(u).path.split('/')[-1] for u in url]
        most_common_basename, _ =Counter(basename).most_common(1)[0]

        foto_urls =[u for u in url if most_common_basename in u]
        self.img_urls =foto_urls
        return foto_urls
    def extract_title_description(self):
        soup =self.soup
        title =soup.find_all('title')[0].get_text(strip=True).split('|')[0]
        description =soup.find_all('meta',
                                   attrs={'name':'description'}) \
                                    [0]['content']
        self.title =title
        self.description =description
        return title, description
    def save_content(self):
    
      
        for i, img_url in enumerate(self.img_urls):
            header = self.header
            r =requests.get(img_url,headers =header)
            
            save_title =re.sub(r'[\\/*?:"<>|]',"_",self.title)[:10].strip()
            os.makedirs(save_title,exist_ok =True)

            with open(f'{save_title}/{i}.jpg','wb') as f:
                f.write(r.content)

        with open(f'{save_title}/title_description.txt','w',encoding ='utf-8') as f:
            f.write(self.title)
            f.write('\n')
            f.write(self.description)

        
    def process(self):
        
        soup ,status_code =self.fetch_content()
        
        if soup is None and status_code !=200:
            return status_code
        
        self.extract_img_urls()
        self.extract_title_description()
        self.save_content()
        
        return status_code

     
            
        
        

if __name__ == '__main__':

    current_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_path)

    
    with open(os.path.join(current_path,'input_file.json'),
              'r',encoding ='utf-8') as f:
        input_data =json.load(f)
    issue_urls =[]
    for item in input_data:
        url =item['url']
        try:
            processor =ImgTitleDesc(url)
            status_code = processor.process()
        except ValueError as e:
            print(f'Error creating processor for URL {url}: {e}')
            issue_urls.append(url)
            continue
       
        
        if status_code !=200:
            print(f'Issue with URL: {url}, Status Code: {status_code}')
            break
        issue_urls.append(url)
            
    if issue_urls:
        with open('issue_urls.txt','w',encoding ='utf-8') as f:
            for url in issue_urls:
                f.write(url +'\n')
    print(len(issue_urls))
    