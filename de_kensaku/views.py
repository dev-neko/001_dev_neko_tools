

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
	# ['検索先名','検索用URL','検索文字の文字コード','カートURL','注文履歴']
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
		#	ショッピング
		['Amazon',
			 'https://www.amazon.co.jp/s?k=',
			 '',
			 'https://uic.jp/calendar/',
			 'https://www.amazon.co.jp/gp/css/order-history'],
		['ヨドバシ.com',
			 'https://www.yodobashi.com/?word=',
			 '',
			 'https://order.yodobashi.com/yc/shoppingcart/index.html',
			 'https://order.yodobashi.com/yc/orderhistory/index.html'],
		['Yahoo!ショッピング',
			 'https://shopping.yahoo.co.jp/search?p=',
			 '',
			 'https://order.shopping.yahoo.co.jp/cgi-bin/cart-form',
			 'https://odhistory.shopping.yahoo.co.jp/cgi-bin/history-list'],
		['楽天市場',
			 'https://search.rakuten.co.jp/search/mall/',
			 '',
			 'https://basket.step.rakuten.co.jp/rms/mall/bs/cart/',
			 'https://order.my.rakuten.co.jp/'],
		['LOHACO',
			 'https://lohaco.jp/ksearch/?searchWord=',
			 '',
			 'https://lohaco.jp/sf/cart/',
			 'https://lohaco.jp/odr/order/purchaseHistoryView/'],
		['楽天西友ネットスーパー',
			 'https://sm.rakuten.co.jp/search?keyword=',
			 '',
			 'https://sm.rakuten.co.jp/step/cart',
			 'https://sm.rakuten.co.jp/mypage/purchase'],
		['ビックカメラ.com',
			 'https://www.biccamera.com/bc/category/?q=',
			 'shift-jis',
			 'https://www.biccamera.com/bc/cart/CCtViewCart_001.jsp',
			 'https://www.biccamera.com/bc/member/CMmOrderHistory.jsp'],
		['アイリスプラザ',
			 'https://www.irisplaza.co.jp/index.php?KB=SEARCH&CID=&itemnm=',
			 'shift-jis',
			 'https://www.irisplaza.co.jp/isc_Cartins.php',
			 'https://www.irisplaza.co.jp/Isc_Rireki.php'],
		['サンコーレアモノショップ',
			 'https://www.thanko.jp/shop/shopbrand.html?search=',
			 'euc-jp',
			 'https://www.thanko.jp/shop/basket.html',
			 'https://www.makeshop.jp/ssl/ssl_confirm/confirm.html'],
		#	オークション・フリマ
		['ヤフオク!',
			'https://auctions.yahoo.co.jp/search/search?p=',
			'',
			'https://auctions.yahoo.co.jp',
			 ''],
		['ラクマ',
			'https://fril.jp/search/',
			'',
			'https://fril.jp',
			 ''],
		['メルカリ',
			'https://www.mercari.com/jp/search/?keyword=',
			'',
			'https://www.mercari.com/jp',
			 ''],
		#	動画
		['YouTube',
			'https://www.youtube.com/results?search_query=',
			'',
			'https://www.youtube.com',
			 ''],
		['ニコニコ動画',
			'https://www.nicovideo.jp/search/',
			'',
			'https://www.nicovideo.jp',
			 ''],
		['FC2動画',
			'https://video.fc2.com/search/video/?keyword=',
			'',
			'https://video.fc2.com',
		 	''],
		['dailymotion',
			'https://www.dailymotion.com/search/',
			'',
			'https://www.dailymotion.com',
		 	''],
		#	チャット
		['AmazonChat',
			'https://www.amazon.co.jp/message-us?origRef=de_poc&muClientName=magus&ref_=de_poc',
			'',
			'',
			''],
		#	その他
		# 検索欄空欄でマイプレイス
		['Googleマップ',
			'https://www.google.co.jp/maps/place/',
			'euc-jp',
			'https://www.google.co.jp/maps/@/data=!4m2!10m1!1e2',
		 	''],
		['Yahoo!知恵袋',
			'https://chiebukuro.yahoo.co.jp/search/?p=',
			'',
			'https://chiebukuro.yahoo.co.jp',
		 	''],
		['note',
			'https://note.mu/search?context=note&mode=search&q=',
			'',
			'https://note.mu',
		 	''],
		['Twitter',
			'https://twitter.com/search?q=',
			'',
			'https://twitter.com',
		 	''],
		['Facebook',
			'https://www.fo_srch_urlcebook.com/search/top/?q=',
			'',
			'https://www.fo_srch_urlcebook.com',
		 	''],
		['GooglePlay',
			'https://play.google.com/store/search?q=',
			'',
			'https://play.google.com',
		 	''],
	]

	input_data = request.POST["srch_str"]
	if request.method == 'POST':
		# enterがクリックされた場合の処理は書かなくても何故かGoogleで検索される
		# →すぐ下のsubmitをyahooにしたらyahooで検索された→すぐ下のsubmitが送信されるらしい

		# http://かhttps://から始まるときはそのページを開く
		if input_data.startswith("http://") or input_data.startswith("https://"):
			open_url = input_data
		else:
			for fo_srch_url in srch_url:
				try:
					# クリックしたアイコン名とfo_srch_url[0].xが一致するまで回す
					request.POST[ fo_srch_url[0] + ".x" ]
				except MultiValueDictKeyError:
					# 全て確認するし、どれかには一致するので例外はpass
					pass
				# どれかに一致したときの処理
				# とりあえずif、elifの後はbreakで処理しないようにした
				else:
					# チャット系のアイコンをクリックした場合は検索欄が空欄でも何か入っていてもチャットのページを開く
					if "Chat" in fo_srch_url[0]:
						open_url = fo_srch_url[1]
					# 検索欄に何も入力されていなかった場合はカートか購入履歴表示
					elif input_data == "":
						if int(request.POST[ fo_srch_url[0] + ".x" ]) < 45:
							open_url = fo_srch_url[3]
						else:
							open_url=fo_srch_url[4]
					# 通常の検索用URLで文字コードを指定して検索
					elif fo_srch_url[2] == 'shift-jis':
						open_url = fo_srch_url[1] + urllib.parse.quote(input_data, encoding='shift-jis')
					# 通常の検索用URLで文字コードを指定して検索
					elif fo_srch_url[2] == 'euc-jp':
						open_url = fo_srch_url[1] + urllib.parse.quote(input_data, encoding='euc-jp')
					# 通常の検索用URLで検索
					else:
						open_url = fo_srch_url[1] + input_data
					break

	return HttpResponseRedirect(open_url)