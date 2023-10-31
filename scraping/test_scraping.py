from parsel import Selector
import requests


class NewsScraper:
    URL = 'https://24.kg/'
    LINK_XPATH = '//div[@class="one"]/div/a/@href'
    PLUS_URL = 'https://24.kg/'
    DATE_XPATH = '//div[@class="one"]/div[@class="time"]/text()'

    def parse_data(self):
        html = requests.get(url=self.URL).text
        tree = Selector(text=html)
        links = tree.xpath(self.LINK_XPATH).extract()
        for link in links:
            print(self.PLUS_URL + link)

        return links[:5]


if __name__ == "__main__":
    scraper = NewsScraper()
    scraper.parse_data()

