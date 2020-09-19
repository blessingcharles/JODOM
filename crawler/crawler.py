from urllib.request import urlparse , urljoin
from bs4 import BeautifulSoup
import requests 

external_urls = set()
urls = set()

def get_all_js_links(url):
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content , "html.parser")
    for script_tags in soup.findAll("script"):
        script_url = script_tags.attrs.get("src")
        if script_url == None or script_url == "":
            continue
        script_url = urljoin(url,script_url)
        if domain_name not in urlparse(script_url).netloc:
            external_urls.add(script_url)
            continue
        
        urls.add(script_url)

def crawl(url):
    link = get_all_js_links(url)

