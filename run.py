from scrapy.crawler import CrawlerProcess

from emoji.spiders.emoji_spider import EmojiSpiderSpider


def start_process():
    process = CrawlerProcess(
        settings={
            'FILES_STORE': 'emoji/images',
            'ITEM_PIPELINES': {
                'emoji.pipelines.EmojiPipeline': 300,
            }
        }
    )
    process.crawl(EmojiSpiderSpider)
    process.start()


if __name__ == '__main__':
    start_process()
