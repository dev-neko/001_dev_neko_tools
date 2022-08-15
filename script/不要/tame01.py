import json
import re
from collections import OrderedDict
import pprint
import requests
import bs4


"""APIでデータ取得"""
"""
appid="dj00aiZpPXRkUGN0TzJmdkVFeSZzPWNvbnN1bWVyc2VjcmV0Jng9MzA-"
srch_url="https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch?appid="+appid+"&query=nike"
response = requests.get(srch_url)
jsondata = response.json()
print(jsondata["hits"][1]["name"])
"""
"""APIでデータ取得"""

"""検索結果一覧のjsonから商品データ取得"""
"""
f = open("json.json", "r")
jsondata = json.load(f)
# ヒット件数など
jsondata_kekka = jsondata["props"]["initialState"]["bff"]["searchResults"]["items"]["1"][0]["content"]
# 商品URL
jsondata_url = jsondata["props"]["initialState"]["bff"]["searchResults"]["items"]["1"][1]["content"]["items"][0]["url"]
# 画像URL
jsondata_imageurl = jsondata["props"]["initialState"]["bff"]["searchResults"]["items"]["1"][1]["content"]["items"][0]["image"]["imageUrl"]
# 商品名
jsondata_name = jsondata["props"]["initialState"]["bff"]["searchResults"]["items"]["1"][1]["content"]["items"][0]["name"]
# 価格
jsondata_price = jsondata["props"]["initialState"]["bff"]["searchResults"]["items"]["1"][1]["content"]["items"][0]["price"]

print(json.dumps(jsondata_url, indent=2, ensure_ascii=False))
print(json.dumps(jsondata_imageurl, indent=2, ensure_ascii=False))
print(json.dumps(jsondata_name, indent=2, ensure_ascii=False))
print(json.dumps(jsondata_price, indent=2, ensure_ascii=False))
"""
"""検索結果一覧のjsonから商品データ取得"""

"""urlで検索してjson取得"""
srch_url = "https://shopping.yahoo.co.jp/category/2505/50532/list?b=1"
srch_url_parser = requests.get(srch_url)
bs4obj = bs4.BeautifulSoup(srch_url_parser.text,'html.parser')
# タグ内容取得が出来なかったので無理矢理json取得した
bs4obj_tag = str(bs4obj.find("script", type="application/json"))
json_data = bs4obj_tag.replace("<script id=\"__NEXT_DATA__\" type=\"application/json\">", "")
json_data = json_data.replace("</script>", "")
json_data = json.loads(json_data)

# ヒット件数など
json_data_kekka = json_data["props"]["initialState"]["bff"]["searchResults"]["items"]["1"][0]["content"]
# 商品URL
json_data_url = json_data["props"]["initialState"]["bff"]["searchResults"]["items"]["1"][1]["content"]["items"][0]["url"]
# 画像URL
json_data_imageurl = json_data["props"]["initialState"]["bff"]["searchResults"]["items"]["1"][1]["content"]["items"][0]["image"]["imageUrl"]
# 商品名
json_data_name = json_data["props"]["initialState"]["bff"]["searchResults"]["items"]["1"][1]["content"]["items"][0]["name"]
# 価格
json_data_price = json_data["props"]["initialState"]["bff"]["searchResults"]["items"]["1"][1]["content"]["items"][0]["price"]

print(json_data_url)
print(json_data_imageurl)
print(json_data_name)
print(json_data_price)

"""urlで検索してjson取得"""