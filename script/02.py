"""
Google Custom Search JSON API を利用して検索結果をjsonで取得する
"""

# 返却された検索結果の読み取りにつかう
# import json
# APIへのアクセスにつかう
from googleapiclient.discovery import build

def GCSJA(query,):
	"""
	:param query:検索するキーワード
	:return:
	"""

	# カスタム検索エンジンID
	CUSTOM_SEARCH_ENGINE_ID="b07c8dc653c744742"
	# API キー
	API_KEY="AIzaSyAPL3quKfeZc1dYhPHNXaPzBJeVLBi9Gd4"

	# APIでやりとりするためのリソースを構築
	# https://googleapis.github.io/google-api-python-client/docs/epy/googleapiclient.discovery-pysrc.html#build
	search=build("customsearch","v1",developerKey=API_KEY)

	# Google Custom Search から結果を取得
	# https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list
	result=search.cse().list(q=query,
	                         cx=CUSTOM_SEARCH_ENGINE_ID,
	                         lr='lang_ja',
	                         num=10,
	                         start=1,
	                         ).execute()

	# json形式の結果を整形
	# organized_result=json.dumps(result,ensure_ascii=False,indent=4)
	# コマンドラインに取得したjsonレスポンスを出力
	# print(organized_result)
	# print(result["items"])

	# for i in result["items"]:
	# 	print('------------------------------')
	# 	print(i['title'])
	# 	print(i['link'])
	# 	print(i['snippet'])

	return result

if __name__=='__main__':
	# 検索するキーワード
	query="猫 花"
	result=GCSJA(query,)
	# 内容表示
	for i in result["items"]:
		print('------------------------------')
		print(i['title'])
		print(i['link'])
		print(i['snippet'])
