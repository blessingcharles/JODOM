from templates import banner
from templates.colors import blue ,reset
import argparse , requests
from crawler.crawler import crawl , external_urls , urls

if __name__ == '__main__':
    banner.banner(blue,reset)
    parser = argparse.ArgumentParser(description="DOM XSS SCANNER")
    parser.add_argument('-u','--url',help='target url',dest='url',required=True)
    args = parser.parse_args()

    url = args.url
    crawl(url)
    for url in urls:
        print(url)
        print("\n")

