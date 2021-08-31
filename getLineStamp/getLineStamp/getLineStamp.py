from dataclasses import dataclass
import requests
import re
import json

class getLineStamp:
    def __init__(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception('Request Error')
        # 男は黙って正規表現
        reg_json = r'<script type="application/ld\+json">\s([\s\S]*?)\s</script>'
        reg_img = r'<span class="mdCMN09Image" style="background-image:url\((.*?)(;compress=true)?\);"></span>'
        content = json.loads(re.findall(reg_json, response.text)[0])
        self.stamp = [attribute[0] for attribute in re.findall(reg_img, response.text)]
        self.content =  getLineStampData(
            content["@context"],
            content["@type"],
            content["sku"],
            content["url"],
            content["name"],
            content["description"],
            content["image"],
            content["offers"],
        )

@dataclass
class getLineStampData:
    context: str = None
    type: str = None
    sku: str = None
    url: str = None
    name: str = None
    description: str = None
    image: str = None
    offers_dict: dict = None

    @property
    def offers(self):
        return getLineStampDataOffers(
            self.offers_dict["@type"],
            int(self.offers_dict["price"]),
            self.offers_dict["priceCurrency"],
            self.offers_dict["url"],
        )

@dataclass
class getLineStampDataOffers:
    type: str = None
    price: str = None
    priceCurrency: str = None
    url: str = None
