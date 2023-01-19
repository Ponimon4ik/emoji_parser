from os import path

from scrapy import Request
from scrapy.pipelines.images import FilesPipeline


class EmojiPipeline(FilesPipeline):

    def get_media_requests(self, item, info):
        yield Request(
            url=item['image_url64'],
            meta={
                'name': item['name'],
                'size': 64
            }
        )
        yield Request(
            url=item['image_url128'],
            meta={
                'name': item['name'],
                'size': 128
            }
        )

    def file_path(self, request, response=None, info=None):
        name = request.meta['name'].replace(' ', '')
        size = request.meta['size']
        return path.join(f'{size}', f'{name}.png')
