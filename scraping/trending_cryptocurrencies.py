# from parsel import Selector
# import requests
#
#
# class TrendingCryptocurrencies:
#     URL = 'https://coinmarketcap.com/'
#     LINK_XPATH = '//tr[@style="cursor: pointer;"]/td[@style="text-align:end"]/div/a/text()'
#     NAME_COIN_XPATH = '//tr[@style="cursor: pointer;"]/td/div[@class="sc-a0353bbc-0 gDrtaY"]/text()'
#     UNIVERSAL_COIN_RATE_XPATH = '//tr[@style="cursor: pointer;"]/td[@style="text-align:end"]/div/a/span/text()'
#
#     PLUS_URL = 'https://coinmarketcap.com/trending-cryptocurrencies/'
#
#     def parse_data(self):
#         html = requests.get(url=self.URL).text
#         tree = Selector(text=html)
#         links = tree.xpath(self.LINK_XPATH).extract()
#         for link in links:
#             print(self.PLUS_URL + link)
#
#         return links[:3]
#
#
# if __name__ == "__main__":
#     scraper = TrendingCryptocurrencies()
#     scraper.parse_data()