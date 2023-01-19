import scrapy

from emoji.items import EmojiItem

emoji_url = (
        'https://api.joypixels.com/'
        'emoji-profiles/{slug}/emoji/_/view/all/{codepoint}'
    )
emoji_download_128 = (
        "https://api.joypixels.com/emoji-profiles/{slug}/" 
        "emoji/YgjSl4ohKtl59o07/download/128/_/7.0"
    )
emoji_download_64 = (
        "https://api.joypixels.com/emoji-profiles/{slug}/"
        "emoji/YgjSl4ohKtl59o07/download/64/_/7.0"
    )


class EmojiSpiderSpider(scrapy.Spider):
    name = 'emoji_spider'
    allowed_domains = ['joypixels.com', 'api.joypixels.com']
    start_urls = ['https://api.joypixels.com/emoji-grouped-by-category-v7']

    def parse(self, response):
        data = response.json()
        for category in data['categories']:
            for emoji in category['emojis']:
                yield response.follow(
                    emoji_url.format(
                        slug=emoji['slug'],
                        codepoint=emoji['base_codepoint']
                    ),
                    callback=self.parse_emoji,
                    meta={
                    }
                )

    def parse_emoji(self, response):
        data = response.json()
        emoji = EmojiItem()
        emoji['image_url128'] = emoji_download_128.format(
            slug=data['profile']['slug']
        )
        emoji['image_url64'] = emoji_download_64.format(
            slug=data['profile']['slug']
        )
        emoji['name'] = data['profile']['title']
        yield emoji
