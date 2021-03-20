from .crawler import Crawler
from crawler.crawlable_reference.bs_crawlable_reference import BsCrawlableReference
from crawler.crawlable_reference.meta.crawlable_reference_with_anchor_meta_info import CrawlableReferenceWithAnchorMetaInfo
from crawler.crawlable_reference.meta.bs_anchor_meta_info import BsAnchorMetaInfo
from .graph import Node, Edge


class OnePassCrawler(Crawler):
    def __init__(self, crawler_package):
        self.crawler_package = crawler_package
        self.visited_urls = set()

    def adjust_to_result(self, crawlable_reference_node):
        crawlable_reference_with_anchor_meta_info = crawlable_reference_node.value
        frontier = self.crawler_package.frontier

        current_url = crawlable_reference_with_anchor_meta_info.crawlable_reference.url
        crawlable = crawlable_reference_with_anchor_meta_info.crawlable_reference.get()

        new_crawlable_references_with_anchor_meta_info = \
            self.crawlable_references_with_anchors_meta_info_for_crawlable(crawlable)

        nodes = self.nodes_for_references_except_visited_urls(
            new_crawlable_references_with_anchor_meta_info
        )

        edges = self.edges_for_parent_and_children(crawlable_reference_node, nodes)

        frontier.add_nodes(nodes)
        frontier.add_edges(edges)

        self.visited_urls.add(current_url)

    def references_visited_url(self, crawlable_reference_with_anchor_meta_info):
        return crawlable_reference_with_anchor_meta_info \
            .anchor_meta_info \
            .bs_in['href'] in self.visited_urls

    @staticmethod
    def crawlable_references_with_anchors_meta_info_for_crawlable(crawlable=BsCrawlableReference()):
        return {
            CrawlableReferenceWithAnchorMetaInfo(
                crawlable_reference=BsCrawlableReference(bs_anchor.url),
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
    def edges_for_parent_and_children(self, parent, children):
        return [
            Edge(first=parent, second=node)
            for node
            in children
        ]
