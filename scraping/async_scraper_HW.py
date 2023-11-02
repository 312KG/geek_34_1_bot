import httpx
from parsel import Selector
import asyncio


class AsyncNewsScraper:
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        # 'Referer': 'https://24.kg/',
        # 'Sec-Purpose': 'prefetch',
        'Connection': 'keep-alive',
    }
    URL = 'https://24.kg/obschestvo/page_{page}/'
    LINK_XPATH = '//div[@class="one"]/div/a/@href'
    PLUS_URL = 'https://24.kg/'
    DATE_XPATH = '//div[@class="one"]/div[@class="time"]/text()'

    async def async_generator(self, limit):
        for page in range(1, limit + 1):
            yield page

    async def parse_pages(self):
        async with httpx.AsyncClient(headers=self.HEADERS) as client:
            async for page in self.async_generator(limit=5):
                await self.get_url(
                    client=client,
                    url=self.URL.format(
                        page=page
                    )
                )

    async def get_url(self, client, url):
        response = await client.get(url)
        print(response.url)
        await self.scrape_links(html=response.text, client=client)

    async def scrape_links(self, html, client):
        tree = Selector(text=html)
        links = tree.xpath(self.LINK_XPATH).extract()
        for link in links:
            print(link)

if __name__ == "__main__":
    scraper = AsyncNewsScraper()
    asyncio.run(scraper.parse_pages())
