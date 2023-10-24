from scrapy import Spider

from locations.dict_parser import DictParser


class RonJonSurfShopSpider(Spider):
    name = "ron_jon_surf_shop"
    item_attributes = {"brand": "Ron Jon Surf Shop", "brand_wikidata": "Q7363993"}
    allowed_domains = ["www.ronjonsurfshop.com"]
    start_urls = ["https://www.ronjonsurfshop.com/ajax/store-locator?searchText=&pagesize=15&pageNumber=1"]

    def parse(self, response):
        for data in response.json()["results"]:
            item = DictParser.parse(data)

            if not data["address1"]:
                item["addr_full"] = data["address2"]
            else:
                item["addr_full"] = data["address1"]

            item["website"] = response.urljoin(data["url"])

            yield item
