from urllib.request import urlparse , urljoin
from bs4 import BeautifulSoup
import requests 
from re import search
from templates.headers import headers
from templates.colors import red , reset , green , grey
external_urls = set()
internal_urls = set()
sources = []
sinks = []

def source_sinks():
    with open("./templates/sources.txt",'r',encoding='utf-8') as file:
        for line in file:
            sources.append(line.strip('\n'))
    with open('./templates/sinks.txt','r',encoding='utf-8') as file:
        for line  in file:
            sinks.append(line.strip('\n')) 

def get_all_js_links(url):
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url,headers=headers).content , "html.parser")
    for script_tags in soup.findAll("script"):
        script_url = script_tags.attrs.get("src")
        if script_url == None or script_url == "":
            continue
        script_url = urljoin(url,script_url)
        if domain_name not in urlparse(script_url).netloc:
            external_urls.add(script_url)
            continue
        
        internal_urls.add(script_url)
    internal_urls.add(url)

def checker(url):
    r = requests.get(url)
    for source in sources:
        if search(source,r.text) :
            print(f"{red}[source] = {source} ---> {green}{url}{reset}")
        
    for sink in sinks:
        if search(sink,r.text):
            print(f"{red}[sinks] = {sink} ---> {green}{url}{reset}")


def xss_finder():
    source_sinks()       
    for url in internal_urls :        
        checker(url)



