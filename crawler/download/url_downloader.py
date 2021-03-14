import requests as rq


class UrlDownloader:
    @staticmethod
    def download_text(url):
        return rq.get(url.text).text
