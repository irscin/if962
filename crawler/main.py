import requests as rq
import sys
import bs4
from .crawler.crawler_package import CrawlerPackage
from .crawler.graph import Graph, BfsGraphIterable, Node
from .crawler.crawlable_reference import BsCrawlableReference

def crawlable_reference_with_anchor_meta_info_from_url(url):
    bs = bs4.BeautifulSoup(rq.get(url).text)
    crawlable_reference = BsCrawlableReference(url)

def main():
    n_args = len(sys.argv)
    if n_args != 1:
        print(f'{n_args} argumentos foram recebidos, mas 1 é esperado')
        raise Exception


if __name__ == '__main__':
    main()
