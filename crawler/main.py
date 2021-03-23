import requests as rq
import sys
import bs4
from crawler.crawler_package import CrawlerPackage
from crawler.graph import Graph, BfsGraphIterable, Node, ListNodeRepository, ListEdgeRepository
from crawler.crawlable_reference import BsCrawlableReference
from crawler.crawlable_reference.meta.crawlable_reference_with_anchor_meta_info import CrawlableReferenceWithAnchorMetaInfo
from crawler.one_pass_crawler import OnePassCrawler
from crawler import Url
from consuming import BsDownloadConsumer, Path, CounterNamer


def crawlable_reference_with_anchor_meta_info_from_url(url):
    crawlable_reference = BsCrawlableReference(url)

    return CrawlableReferenceWithAnchorMetaInfo(crawlable_reference, None)


def main():
    n_args = len(sys.argv)
    if n_args != 3:
        print(f'{n_args - 1} argumentos foram recebidos, mas 2 são esperados')

    main_with_args(sys.argv[1], sys.argv[2])


def main_with_args(url, path):
    crawlable_reference_with_anchor_meta_info = \
        crawlable_reference_with_anchor_meta_info_from_url(Url(url))

    node = Node(crawlable_reference_with_anchor_meta_info)

    graph = Graph(
        ListNodeRepository([node]),
        ListEdgeRepository()
    )

    bfs_graph_iterable = BfsGraphIterable(graph, node)

    consumer = BsDownloadConsumer(Path(path), CounterNamer())

    crawler_package = CrawlerPackage(
        graph=graph,
        frontier_item_consumer=bfs_graph_iterable,
        crawlable_consumer=consumer
    )

    OnePassCrawler(crawler_package).crawl()


if __name__ == '__main__':
    #main_with_args('http://google.com', '/home/co/Personal/Study/2020.1/recuperacao-de-informacao/downloads/')
    main()
