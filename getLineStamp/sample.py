from getLineStamp import getLineStamp


if __name__ == '__main__':
    LineStamp = getLineStamp.getLineStamp("https://store.line.me/stickershop/product/23822/ja")
    print(LineStamp.stamp[0])
    print(LineStamp.content.context)
    print(LineStamp.content.type)
    print(LineStamp.content.sku)
    print(LineStamp.content.url)
    print(LineStamp.content.name)
    print(LineStamp.content.description)
    print(LineStamp.content.image)
    print(LineStamp.content.offers.type)
    print(LineStamp.content.offers.price)
    print(LineStamp.content.offers.priceCurrency)
    print(LineStamp.content.offers.url)