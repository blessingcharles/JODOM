from templates import banner
from templates.colors import blue ,red,reset , grey , green
import argparse
from crawler.crawler import get_all_js_links ,xss_finder ,external_urls , internal_urls

if __name__ == '__main__':
    banner.banner(blue,reset)
    parser = argparse.ArgumentParser(description="DOM XSS SCANNER")
    parser.add_argument('-u','--url',help='target url',dest='url')
    parser.add_argument('-f','--file',help='enter a file containg urls' , dest='file')
    args = parser.parse_args()

    url = args.url
    urls_file = args.file
    if not url and not urls_file:
        print(f"{red}[-]ENTER A VALID INPUT[-] \n TRY python3 jodom.py --help{reset}")
        quit()
    urls = []
    if urls_file :
        try:
            with open(urls_file,'r',encoding="utf-8") as file:
                for line in file:
                    urls.append(line.strip('\n'))
        except FileNotFoundError:
            print("[-]ENTER A VALID FILE CONTAING URLS[-]")
            quit()
            
    if url:
        get_all_js_links(url)
    if urls:
        for url in urls:
            get_all_js_links(url)

    for url in internal_urls:
        print(f"{grey}[+]POSSIBLE JS URLS --->{green}{url}{reset}")
    xss_finder()