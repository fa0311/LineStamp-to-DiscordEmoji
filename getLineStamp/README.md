# getLineStamp

LINE スタンプの情報を取得するライブラリです<br>
<br>

## Usage

```python
from getLineStamp import getLineStamp
LineStamp = getLineStamp.getLineStamp("https://store.line.me/stickershop/product/23822/ja")

# stamp url
print(LineStamp.stamp[0])
# @context
print(LineStamp.content.context)
# @type
print(LineStamp.content.type)
# package id
print(LineStamp.content.sku)
# package url
print(LineStamp.content.url)
# package name
print(LineStamp.content.name)
# package description
print(LineStamp.content.description)
# package image
print(LineStamp.content.image)
# offer @type
print(LineStamp.content.offers.type)
# offer price
print(LineStamp.content.offers.price)
# offer price currency
print(LineStamp.content.offers.priceCurrency)
# offer url
print(LineStamp.content.offers.url)
```
