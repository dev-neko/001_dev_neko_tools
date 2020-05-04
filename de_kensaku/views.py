

import re
import urllib.parse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils.datastructures import MultiValueDictKeyError

def input(request):
	template = loader.get_template("de_kensaku/input.html")
	return HttpResponse(template.render({}, request))

def output(request):
	srch_url = [
		# サーチエンジン
		['Google','https://www.google.com/search?q=',''],
		['Yahoo!JAPAN','https://search.yahoo.co.jp/search?p=',''],
		['Bing','https://www.bing.com/search?q=',''],
		# オークション・フリマ
		['ヤフオク!','https://auctions.yahoo.co.jp/search/search?p=',''],
		['ラクマ','https://fril.jp/search/',''],
		['メルカリ','https://www.mercari.com/jp/search/?keyword=',''],
		# 動画
		['YouTube','https://www.youtube.com/results?search_query=',''],
		['ニコニコ動画','https://www.nicovideo.jp/search/',''],
		['FC2動画','https://video.fc2.com/search/video/?keyword=',''],
		['dailymotion','https://www.dailymotion.com/search/',''],
		# ショッピング
		['Amazon','https://www.amazon.co.jp/s?k=',''],
		['ヨドバシ.com','https://www.yodobashi.com/?word=',''],
		['Yahoo!ショッピング','https://shopping.yahoo.co.jp/search?p=',''],
		['楽天市場','https://search.rakuten.co.jp/search/mall/',''],
		['LOHACO','https://lohaco.jp/ksearch/?searchWord=',''],
		['楽天西友ネットスーパー','https://sm.rakuten.co.jp/search?keyword=',''],
		['ビックカメラ.com','https://www.biccamera.com/bc/category/?q=','shift-jis'],
		['アイリスプラザ','https://www.irisplaza.co.jp/index.php?KB=SEARCH&CID=&itemnm=','shift-jis'],
		['サンコーレアモノショップ','https://www.thanko.jp/shop/shopbrand.html?search=','euc-jp'],
		# その他
		['Yahoo!知恵袋','https://chiebukuro.yahoo.co.jp/search/?p=',''],
		['note','https://note.mu/search?context=note&mode=search&q=',''],
		['Twitter','https://twitter.com/search?q=',''],
		['Facebook','https://www.facebook.com/search/top/?q=',''],
		['GooglePlay','https://play.google.com/store/search?q=',''],
	]

	input_data = request.POST["srch_str"]
	if request.method == 'POST':
		# enterがクリックされた場合の処理は書かなくても何故かGoogleで検索される
		# →すぐ下のsubmitをyahooにしたらyahooで検索された→すぐ下のsubmitが送信されるらしい

		for fa in srch_url:
			try:
				request.POST[ fa[0] + ".x" ]
			except MultiValueDictKeyError:
				pass
			else:
				if fa[2] == 'shift-jis':
					open_url = fa[1] + urllib.parse.quote(input_data, encoding='shift-jis')
				elif fa[2] == 'euc-jp':
					open_url = fa[1] + urllib.parse.quote(input_data, encoding='euc-jp')
				else:
					open_url = fa[1] + input_data

	return HttpResponseRedirect(open_url)
