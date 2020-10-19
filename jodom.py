from templates import banner
from templates.colors import blue ,red,reset , grey , green
import argparse
from crawler.crawler import get_all_js_links ,xss_finder ,external_urls , internal_urls
from templates.logger import Logger

if __name__ == '__main__':
    banner.banner(blue,reset)
    parser = argparse.ArgumentParser(description="DOM XSS SCANNER")
    parser.add_argument('-u','--url',help='target url',dest='url')
    parser.add_argument('-f','--file',help='enter a file containg urls' , dest='file')
    parser.add_argument('-t' , '--threads',type=int,help="enter the threads [default 3]",dest='Threads',default=3)
    parser.add_argument('-o','--output',help="enter the output file to log",dest='logfile')
    args = parser.parse_args()

    url = args.url
    urls_file = args.file
    Threads = args.Threads
    logfile = args.logfile
 
    if not url and not urls_file:
        print(f"{red}[-]ENTER A VALID INPUT[-] \n TRY python3 jodom.py --help{reset}")
        quit()
    urls = []
    
    if logfile:
        log = Logger(logfile)
        url_log = log.start()

    if urls_file :
        try:
            with open(urls_file,'r',encoding="utf-8") as file:
                for line in file:
                    urls.append(line.strip('\n'))
        except FileNotFoundError:
            print("[-]ENTER A VALID FILE CONTAING URLS[-]")
            quit()
    try:        
        if url:
            get_all_js_links(url)
        if urls:
            for url in urls:
                get_all_js_links(url)
    except:
        print(f"[-]SOMETHING WENT WRONG : ( {red}\n[check your internet connection]{reset}")
    
    print(f"{grey}[+]POSSIBLE JS INTERNAL URLS{green}")
    for url in internal_urls:
        url_log.info(url)

    log.close_logging()

    xss_finder(Threads)

