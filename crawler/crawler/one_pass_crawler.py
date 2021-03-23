from .crawler import Crawler
from crawler import Url
from crawler.crawlable_reference.bs_crawlable_reference import BsCrawlableReference
from crawler import BsCrawlable
from crawler.crawlable_reference.meta.crawlable_reference_with_anchor_meta_info import CrawlableReferenceWithAnchorMetaInfo
from crawler.crawlable_reference.meta.bs_anchor_meta_info import BsAnchorMetaInfo
from urllib.parse import urljoin
from .graph import Node, Edge


class OnePassCrawler(Crawler):
    def __init__(self, crawler_package):
        self.crawler_package = crawler_package
        self.visited_urls = set()

    def adjust_to_result(self, crawlable_reference_node):
        crawlable_reference_with_anchor_meta_info = crawlable_reference_node.value
        graph = self.crawler_package.graph

        current_url = crawlable_reference_with_anchor_meta_info.crawlable_reference.url
        crawlable = crawlable_reference_with_anchor_meta_info.crawlable_reference.get()

        new_crawlable_references_with_anchor_meta_info = \
            self.crawlable_references_with_anchors_meta_info_for_crawlable(crawlable)

        nodes = self.nodes_for_references_except_visited_urls(
            new_crawlable_references_with_anchor_meta_info
        )

        edges = self.edges_for_parent_and_children(crawlable_reference_node, nodes)

        graph.add_nodes(nodes)
        graph.add_edges(edges)

        self.crawler_package.crawlable_consumer.consume(crawlable)

        self.visited_urls.add(current_url)

    def references_visited_url(self, crawlable_reference_with_anchor_meta_info):
        return crawlable_reference_with_anchor_meta_info \
            .crawlable_reference \
            .url in self.visited_urls

    @staticmethod
    def crawlable_references_with_anchors_meta_info_for_crawlable(crawlable=BsCrawlable()):
        return {
            CrawlableReferenceWithAnchorMetaInfo(
                crawlable_reference=BsCrawlableReference(Url(urljoin(crawlable.url.text, bs_anchor.url.text))),
                anchor_meta_info=BsAnchorMetaInfo(
                    bs_parent=bs_anchor.bs.parent,
                    bs_in=bs_anchor.bs
                )
            )
            for bs_anchor
            in crawlable.get_anchors()
        }

    def nodes_for_references_except_visited_urls(self, crawlable_references_with_anchor_meta_info):
        return [
            Node(ref)
            for ref
            in crawlable_references_with_anchor_meta_info
            if not self.references_visited_url(ref)
        ]

    @staticmethod
    def edges_for_parent_and_children(parent, children):
        return [
            Edge(first=parent, second=node)
            for node
            in children
        ]
