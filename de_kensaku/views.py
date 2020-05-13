

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
	# ショッピング系
	# ['検索先名','検索用URL','検索文字の文字コード','カートURL']
	# それ以外
	# ['検索先名','検索用URL','検索文字の文字コード','トップページURL']
	srch_url = [
		#	サーチエンジン
		['Google'
			,'https://www.google.com/search?q=',
			'',
			''],
		['Yahoo!JAPAN',
			'https://search.yahoo.co.jp/search?p=',
			'',
			''],
		['Bing',
			'https://www.bing.com/search?q=',
			'',
			''],
		['URLを直接開く',
			'',
			'',
			''],
		#	オークション・フリマ
		['ヤフオク!',
			'https://auctions.yahoo.co.jp/search/search?p=',
			'',
			'https://auctions.yahoo.co.jp'],
		['ラクマ',
			'https://fril.jp/search/',
			'',
			'https://fril.jp'],
		['メルカリ',
			'https://www.mercari.com/jp/search/?keyword=',
			'',
			'https://www.mercari.com/jp'],
		#	動画
		['YouTube',
			'https://www.youtube.com/results?search_query=',
			'',
			'https://www.youtube.com'],
		['ニコニコ動画',
			'https://www.nicovideo.jp/search/',
			'',
			'https://www.nicovideo.jp'],
		['FC2動画',
			'https://video.fc2.com/search/video/?keyword=',
			'',
			'https://video.fc2.com'],
		['dailymotion',
			'https://www.dailymotion.com/search/',
			'',
			'https://www.dailymotion.com'],
		#	ショッピング
		['Amazon',
			'https://www.amazon.co.jp/s?k=',
			'',
			'https://www.amazon.co.jp/gp/cart/view.html'],
		['ヨドバシ.com',
			'https://www.yodobashi.com/?word=',
			'',
			'https://order.yodobashi.com/yc/shoppingcart/index.html'],
		['Yahoo!ショッピング',
			'https://shopping.yahoo.co.jp/search?p=',
			'',
			'https://order.shopping.yahoo.co.jp/cgi-bin/cart-form'],
		['楽天市場',
			'https://search.rakuten.co.jp/search/mall/',
			'',
			'https://basket.step.rakuten.co.jp/rms/mall/bs/cart/'],
		['LOHACO',
			'https://lohaco.jp/ksearch/?searchWord=',
			'',
			'https://lohaco.jp/sf/cart/'],
		['楽天西友ネットスーパー',
			'https://sm.rakuten.co.jp/search?keyword=',
			'',
			'https://sm.rakuten.co.jp'],
		['ビックカメラ.com',
			'https://www.biccamera.com/bc/category/?q=',
			'shift-jis',
			'https://www.biccamera.com/bc/cart/CCtViewCart_001.jsp'],
		['アイリスプラザ',
			'https://www.irisplaza.co.jp/index.php?KB=SEARCH&CID=&itemnm=',
			'shift-jis',
			'https://www.irisplaza.co.jp/isc_Cartins.php'],
		['サンコーレアモノショップ',
			'https://www.thanko.jp/shop/shopbrand.html?search=',
			'euc-jp',
			'https://www.thanko.jp/shop/basket.html'],
		#	その他
		['Yahoo!知恵袋',
			'https://chiebukuro.yahoo.co.jp/search/?p=',
			'',
			'https://chiebukuro.yahoo.co.jp'],
		['note',
			'https://note.mu/search?context=note&mode=search&q=',
			'',
			'https://note.mu'],
		['Twitter',
			'https://twitter.com/search?q=',
			'',
			'https://twitter.com'],
		['Facebook',
			'https://www.facebook.com/search/top/?q=',
			'',
			'https://www.facebook.com'],
		['GooglePlay',
			'https://play.google.com/store/search?q=',
			'',
			'https://play.google.com'],
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
				if input_data == "":
					open_url = fa[3]
				elif fa[2] == 'shift-jis':
					open_url = fa[1] + urllib.parse.quote(input_data, encoding='shift-jis')
				elif fa[2] == 'euc-jp':
					open_url = fa[1] + urllib.parse.quote(input_data, encoding='euc-jp')
				else:
					open_url = fa[1] + input_data

	return HttpResponseRedirect(open_url)
