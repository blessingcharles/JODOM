from urllib.request import urlparse , urljoin
from bs4 import BeautifulSoup
import requests 
import concurrent.futures
from re import search
from templates.headers import headers
from templates.colors import red , reset , green , grey
external_urls = []
internal_urls = []
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
            external_urls.append(script_url)
            continue
        
        internal_urls.append(script_url)
    internal_urls.append(url)

def checker(url):
    r = requests.get(url,headers=headers)
    for source in sources:
        if search(source,r.text) :
            print(f"{red}[source] = {source} ---> {green}{url}{reset}")
        
    for sink in sinks:
        if search(sink,r.text):
            print(f"{red}[sinks] = {sink} ---> {green}{url}{reset}")


def xss_finder(Threads):
    source_sinks()       
    with concurrent.futures.ThreadPoolExecutor(max_workers=Threads) as executor:
        executor.map(checker,internal_urls)        
        



