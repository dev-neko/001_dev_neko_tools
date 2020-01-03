import re
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


def input(request):
	template = loader.get_template("de_kensaku/input.html")
	return HttpResponse(template.render({}, request))

def output(request):
	# サーチエンジン
	srch_url_srcheng = [
		'https://www.google.com/search?q=',
		'https://search.yahoo.co.jp/search?p=',
		'https://www.bing.com/search?q='
	]
	# オークション・フリマ
	srch_url_aucfri = [
		'https://auctions.yahoo.co.jp/search/search?p=',
		'https://fril.jp/search/',
		'https://www.mercari.com/jp/search/?keyword='
	]
	# 動画
	srch_url_video = [
		'https://www.youtube.com/results?search_query=',
		'https://www.nicovideo.jp/search/',
		'https://video.fc2.com/search/video/?keyword=',
		'https://www.dailymotion.com/search/'
	]
	srch_url_shop = [
		# ショッピング
		'https://shopping.yahoo.co.jp/search?p=',
		'https://search.rakuten.co.jp/search/mall/',
		'https://www.amazon.co.jp/s?k=',
		'https://www.yodobashi.com/?word=',
		'https://lohaco.jp/ksearch/?searchWord=',
		'https://sm.rakuten.co.jp/search?keyword=',
		# ビックカメラ、価格.comは日本語では検索できないぽい
		# 'https://kakaku.com/search_results/'
		# 'https://www.biccamera.com/bc/category/?q=',
	]
	# その他
	srch_url_other = [
		'https://chiebukuro.yahoo.co.jp/search/?p=',
		'https://note.mu/search?context=note&mode=search&q=',
		'https://twitter.com/search?q=',
		'https://www.facebook.com/search/top/?q='
	]

	input_data = request.POST["srch_str"]
	request_POST = str(request.POST)
	if request.method == 'POST':
		# enterがクリックされた場合の処理は書かなくても何故かGoogleで検索される
		# →すぐ下のsubmitをyahooにしたらyahooで検索された→すぐ下のsubmitが送信されるらしい

		# サーチエンジン
		if re.search('Google', request_POST):
			open_url = srch_url_srcheng[0] + input_data
		elif re.search('Yahoo!JAPAN', request_POST):
			open_url = srch_url_srcheng[1] + input_data
		elif re.search('Bing', request_POST):
			open_url = srch_url_srcheng[2] + input_data
		# オークション・フリマ
		elif re.search('ヤフオク!', request_POST):
			open_url = srch_url_aucfri[0] + input_data
		elif re.search('ラクマ', request_POST):
			open_url = srch_url_aucfri[1] + input_data
		elif re.search('メルカリ', request_POST):
			open_url = srch_url_aucfri[2] + input_data
		# 動画サービス
		elif re.search('YouTube', request_POST):
			open_url = srch_url_video[0] + input_data
		elif re.search('ニコニコ動画', request_POST):
			open_url = srch_url_video[1] + input_data
		elif re.search('FC2動画', request_POST):
			open_url = srch_url_video[2] + input_data
		elif re.search('dailymotion', request_POST):
			open_url = srch_url_video[3] + input_data
		# ショッピング
		elif re.search('Yahoo!ショッピング', request_POST):
			open_url = srch_url_shop[0] + input_data
		elif re.search('楽天市場', request_POST):
			open_url = srch_url_shop[1] + input_data
		elif re.search('Amazon', request_POST):
			open_url = srch_url_shop[2] + input_data
		elif re.search('ヨドバシ.com', request_POST):
			open_url = srch_url_shop[3] + input_data
		elif re.search('LOHACO', request_POST):
			open_url = srch_url_shop[4] + input_data
		elif re.search('楽天西友ネットスーパー', request_POST):
			open_url = srch_url_shop[5] + input_data
		# その他
		elif re.search('Yahoo!知恵袋', request_POST):
			open_url = srch_url_other[0] + input_data
		elif re.search('note', request_POST):
			open_url = srch_url_other[1] + input_data
		elif re.search('Twitter', request_POST):
			open_url = srch_url_other[2] + input_data
		elif re.search('Facebook', request_POST):
			open_url = srch_url_other[3] + input_data
	return HttpResponseRedirect(open_url)