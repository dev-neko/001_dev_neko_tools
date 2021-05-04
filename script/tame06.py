import bs4,requests,re

src_url="https://auctions.yahoo.co.jp/seller/sunsmile_happiness999?sid=sunsmile_happiness999&b=1&n=20&mode=2"
src_url_parser=requests.get(src_url)
bs4obj=bs4.BeautifulSoup(src_url_parser.text,'html.parser')
# 出品者名
# auc_seller=bs4obj.find("span",attrs={'class':'seller__name'}).text
auc_seller=None
# 出品者のレート
auc_rating=None
try:
	for list_items in bs4obj.find("div",attrs={'id':'list01'}).find_all("tr",attrs={'class':''}):
		if list_items.find("td",attrs={'class':'i'}):
			# 画像URL
			auc_imgurl=list_items.find("img",attrs={'':''}).get('src')
			# オークション名
			auc_title=list_items.find("h3",attrs={'':''}).find("a",attrs={'':''}).text
			# URL
			auc_url=list_items.find("h3",attrs={'':''}).find("a",attrs={'':''}).get('href')
			# 現在価格
			auc_price=list_items.find("td",attrs={'class':'pr1'}).text.replace(",","").replace("円","").replace("\n","")
			# 即決価格
			auc_pricewin=list_items.find("td",attrs={'class':'pr2'}).text.replace(",","").replace("円","").replace("\n","")
			# 入札数
			auc_bid=list_items.find("td",attrs={'class':'bi'}).text.replace("\n","")
			# 残り時間 auc_time
			auc_time=list_items.find("td",attrs={'class':'ti'}).text.replace("\n","")
			print(auc_title)
			print("------------------------------")
except AttributeError:
	print("該当なし")
