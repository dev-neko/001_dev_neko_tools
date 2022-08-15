"""
requestsを使用してGoogle検索結果をスクレイピング
"""


import requests

url = 'https://www.google.co.jp/search'

# グーグルへ接続
req = requests.get(url, params={'q': 'パイソン'})

# アドレス取得
aaa=req.url
print(aaa)
#[結果] 'https://www.google.co.jp/search?q=%E3%83%91%E3%82%A4%E3%82%BD%E3%83%B3'

# 検索結果取得
bbb=req.text
print(bbb)