from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import bs4,requests,re



def ya_src_tool(request):
	# env = Environment(loader=FileSystemLoader('./templates/work_apps'))
	# template = env.get_template('ya_src_tool.html')
	# return HttpResponse(template.render(request, jinja_data_auccat=auccat_dic))

	# template=loader.get_template('work_apps/ya_src_tool.html')
	# return HttpResponse(template.render(auccat_dic))

	template = loader.get_template("work_apps/ya_src_tool.html")
	return HttpResponse(template.render({}, request))

def output(request):
	# テンプレへ渡す辞書
	django_template_data=[]
	#
	va="&va="+request.POST["va"]
	vo="&vo="+request.POST["vo"]
	ve="&ve="+request.POST["ve"]
	ngram="&ngram="+request.POST["radio_ngram"]
	condition=''.join(request.POST.getlist("check_condition"))
	abatch="&abatch="+request.POST["radio_abatch"]
	fixed="&fixed="+request.POST["radio_fixed"]
	auccat="&auccat="+request.POST["radio_auccat"]
	aucminprice="&aucminprice="+request.POST["aucminprice"]
	aucmaxprice="&aucmaxprice="+request.POST["aucmaxprice"]
	aucmin_bidorbuy_price="&aucmin_bidorbuy_price="+request.POST["aucmin_bidorbuy_price"]
	aucmax_bidorbuy_price="&aucmax_bidorbuy_price="+request.POST["aucmax_bidorbuy_price"]
	check_istatus="&istatus="+','.join(request.POST.getlist("check_istatus"))
	# 出品地域
	if request.POST.getlist("check_loc_cd")[0] == "0":
		loc_cd="&loc_cd=0"
	else:
		loc_cd="&loc_cd="+','.join(request.POST.getlist("check_loc_cd"))
	# 表示件数と解析ページ数から&b=を計算
	dispn=request.POST["radio_dispn"]
	analysis_pages=request.POST["analysis_pages"]
	if analysis_pages!="1":
		analysis_pages=1+int(dispn)*(int(analysis_pages)-1)
	dispn_anap="&n="+str(dispn)+"&b="+str(analysis_pages)
	# 追加のフィルタ
	post_auto_ext=request.POST["radio_auto_ext"]
	post_rate=request.POST["radio_rate"]
	post_exclude_id=request.POST["exclude_id"].split(',')

	# URLからソースを取得
	src_url="https://auctions.yahoo.co.jp/search/search?"+va+vo+ve+ngram+condition+abatch+auccat+aucminprice+aucmaxprice+aucmin_bidorbuy_price+aucmax_bidorbuy_price+check_istatus+loc_cd+dispn_anap+fixed+"&mode=2"
	# src_url="https://auctions.yahoo.co.jp/search/search?va=AAA%E7%B4%9A%E5%A4%A9%E7%84%B6%E3%83%AC%E3%82%A4%E3%83%B3%E3%83%9C%E3%83%BC%E6%B0%B4%E6%99%B6%E5%8E%9F%E7%9F%B3160B3-72B12b&exflg=1&b=1&n=50&mode=2&auccat=&tab_ex=commerce&ei=utf-8&aq=-1&oq=&sc_i=&exflg=1&p=AAA%E7%B4%9A%E5%A4%A9%E7%84%B6%E3%83%AC%E3%82%A4%E3%83%B3%E3%83%9C%E3%83%BC%E6%B0%B4%E6%99%B6%E5%8E%9F%E7%9F%B3&x=0&y=0"
	src_url_parser=requests.get(src_url)
	bs4obj=bs4.BeautifulSoup(src_url_parser.text,'html.parser')
	# print(bs4obj)
	# 検索結果一覧ページから取得できる情報を取得
	for list_items in bs4obj.find_all("li",attrs={'class':'Product'}):
		# 画像URL
		auc_imgurl=list_items.find("img",attrs={'class':'Product__imageData'}).get('src')
		# オークション名
		auc_title=list_items.find("a",attrs={'class':'Product__titleLink'}).text
		# URL
		auc_url=list_items.find("a",attrs={'class':'Product__titleLink'}).get('href')
		# 出品者名
		auc_seller=list_items.find("a",attrs={'class':'Product__seller'}).text
		# 出品者のレート
		# 新規はレート無しなのでそれを考慮
		auc_rating=list_items.find("a",attrs={'class':'Product__rating'})
		if auc_rating:
			auc_rating=auc_rating.text
		else:
			auc_rating="0%"
		# 現在価格
		auc_price=list_items.find("span",attrs={'class':'Product__priceValue u-textRed'}).text.replace(",","").replace("円","")
		# 即決価格
		if list_items.select('span[class="Product__priceValue"]'):
			auc_pricewin=list_items.select('span[class="Product__priceValue"]')[0].text.replace(",","").replace("円","")
		else:
			auc_pricewin="-"
		# 入札数
		auc_bid=list_items.find("a",attrs={'class':'Product__bid'}).text
		# 残り時間(auc_time)は「残り日数か時間」と「終了日時」か「残り分」だけの組み合わせなので
		# 「終了日時」があれば「残り日数か時間」と「終了日時」を表示
		# 「終了日時」がなければ「残り分」だけ表示
		auc_time_dayhormin=list_items.find("span",attrs={'class':'Product__time'}).text
		auc_time_detail=list_items.find("span",attrs={'class':'u-textGray u-fontSize10'})
		if auc_time_detail:
			auc_time=auc_time_dayhormin+auc_time_detail.text
		else:
			auc_time=auc_time_dayhormin
		# 現在価格と即決価格が同じならば定額、異なればオークションと判断して
		# オークションの場合だけ自動延長の有無を確認
		# URLからソースを取得
		if auc_price!=auc_pricewin:
			src_url_auto_ext=auc_url
			src_url_parser=requests.get(src_url_auto_ext)
			bs4obj2=bs4.BeautifulSoup(src_url_parser.text,'html.parser')
			# 自動延長の有無
			auc_auto_ext\
			=bs4obj2.find("ul",attrs={'class':'ProductDetail__items ProductDetail__items--primary'}).find_all("dd",attrs=
				{'class':'ProductDetail__description'})[3].text.replace("：","")
		else:
			auc_auto_ext="定額のオークション"

		# print("--------------全体----------------")
		# print(auc_auto_ext)
		# print(auc_rating)
		# print(auc_seller)
		# print("--------------フィルタ----------------")

		# ヤフオク標準検索機能以外の条件でスクレイピングしてフィルタ
		if ((post_auto_ext!="OFF") and (post_rate!="OFF") and (post_exclude_id[0]!="OFF")):
			# print("すべてON")
			if ((auc_auto_ext=="なし") and (float(auc_rating.replace("%",""))>float(post_rate)) and (
				auc_seller not in post_exclude_id)):
				# print(auc_title)
				# print(auc_url)
				django_template_data.append({'画像URL':auc_imgurl,'オク名':auc_title,'オクURL':auc_url,'出品者ID':auc_seller,'評価レート':auc_rating,'現在価格':auc_price,'即決価格':auc_pricewin,'入札数':auc_bid,'残り時間':auc_time,'自動延長':auc_auto_ext,})
		elif ((post_auto_ext!="OFF") and (post_rate!="OFF")):
			# print("abがON")
			if ((auc_auto_ext=="なし") and (float(auc_rating.replace("%",""))>float(post_rate))):
				# print(auc_title)
				# print(auc_url)
				django_template_data.append({'画像URL':auc_imgurl,'オク名':auc_title,'オクURL':auc_url,'出品者ID':auc_seller,'評価レート':auc_rating,'現在価格':auc_price,'即決価格':auc_pricewin,'入札数':auc_bid,'残り時間':auc_time,'自動延長':auc_auto_ext,})
		elif ((post_auto_ext!="OFF") and (post_exclude_id[0]!="OFF")):
			# print("acがON")
			if ((auc_auto_ext=="なし") (auc_seller not in post_exclude_id)):
				# print(auc_title)
				# print(auc_url)
				django_template_data.append({'画像URL':auc_imgurl,'オク名':auc_title,'オクURL':auc_url,'出品者ID':auc_seller,'評価レート':auc_rating,'現在価格':auc_price,'即決価格':auc_pricewin,'入札数':auc_bid,'残り時間':auc_time,'自動延長':auc_auto_ext,})
		elif ((post_rate!="OFF") and (post_exclude_id[0]!="OFF")):
			# print("bcがON")
			if ((float(auc_rating.replace("%",""))>float(post_rate)) and (auc_seller not in post_exclude_id)):
				# print(auc_title)
				# print(auc_url)
				django_template_data.append({'画像URL':auc_imgurl,'オク名':auc_title,'オクURL':auc_url,'出品者ID':auc_seller,'評価レート':auc_rating,'現在価格':auc_price,'即決価格':auc_pricewin,'入札数':auc_bid,'残り時間':auc_time,'自動延長':auc_auto_ext,})
		elif (post_auto_ext!="OFF"):
			# print("aがON")
			if (auc_auto_ext=="なし"):
				# print(auc_title)
				# print(auc_url)
				django_template_data.append({'画像URL':auc_imgurl,'オク名':auc_title,'オクURL':auc_url,'出品者ID':auc_seller,'評価レート':auc_rating,'現在価格':auc_price,'即決価格':auc_pricewin,'入札数':auc_bid,'残り時間':auc_time,'自動延長':auc_auto_ext,})
		elif (post_rate!="OFF"):
			# print("bがON")
			if (float(auc_rating.replace("%",""))>float(post_rate)):
				# print(auc_title)
				# print(auc_url)
				django_template_data.append({'画像URL':auc_imgurl,'オク名':auc_title,'オクURL':auc_url,'出品者ID':auc_seller,'評価レート':auc_rating,'現在価格':auc_price,'即決価格':auc_pricewin,'入札数':auc_bid,'残り時間':auc_time,'自動延長':auc_auto_ext,})
		elif (post_exclude_id[0]!="OFF"):
			# print("cがON")
			if (auc_seller not in post_exclude_id):
				# print(auc_title)
				# print(auc_url)
				django_template_data.append({'画像URL':auc_imgurl,'オク名':auc_title,'オクURL':auc_url,'出品者ID':auc_seller,'評価レート':auc_rating,'現在価格':auc_price,'即決価格':auc_pricewin,'入札数':auc_bid,'残り時間':auc_time,'自動延長':auc_auto_ext,})
		else:
			# print("すべてOFF")
			# print(auc_title)
			# print(auc_url)
			django_template_data.append({'画像URL':auc_imgurl,'オク名':auc_title,'オクURL':auc_url,'出品者ID':auc_seller,'評価レート':auc_rating,'現在価格':auc_price,'即決価格':auc_pricewin,'入札数':auc_bid,'残り時間':auc_time,'自動延長':auc_auto_ext,})

	# print("--------------終了----------------")

	django_template_data_sub={'検索URL':src_url,
														}

	# オークションデータ
	django_template_data={'auc_data':django_template_data,
												'sub_data':django_template_data_sub,
												}
	# 検証用データ


	# env = Environment(loader=FileSystemLoader('./templates/work_apps'))
	# template = env.get_template('output.html')
	# return HttpResponse(template.render(jinja_data=data))

	template=loader.get_template('work_apps/output.html')
	return HttpResponse(template.render(django_template_data))



def ya_src_tool_v2(request):
	template = loader.get_template("work_apps/ya_src_tool_v2.html")
	return HttpResponse(template.render({}, request))

def output_v2(request):
	# テンプレへ渡す辞書
	auc_data_dict=[]
	# 何曜日の何時までに終了か指定
	post_e_wday=request.POST["select_e_wday"]
	post_e_time=request.POST["select_e_time"]
	e_wday_e_time="&e_wday="+post_e_wday+"&e_time="+post_e_time
	# ヤフオクで絞り込んだURL
	post_src_url=request.POST["src_raw_url"]
	# 表示件数と解析ページ数から&b=を計算 URLから表示件数取得バージョン
	# &b= も &n= もすでにURLに含まれているとする
	post_dispn=re.search(r'&n=([0-9]*)',post_src_url).groups()[0]
	post_analysis_pages=request.POST["analysis_pages"]
	if post_analysis_pages!="1":
		post_analysis_pages=1+int(post_dispn)*(int(post_analysis_pages)-1)
	# bs4で解析するURL
	src_url=re.sub(r'&b=[0-9]*',"&b="+str(post_analysis_pages),post_src_url)+e_wday_e_time
	# 追加のフィルタ
	post_auto_ext=request.POST["radio_auto_ext"]
	post_rate=request.POST["radio_rate"]
	post_exclude_id=request.POST["exclude_id"].split(',')
	post_exclude_titledesc=request.POST["exclude_titledesc"].split(' ')

	# URLからソースを取得
	src_url_parser=requests.get(src_url)
	bs4obj=bs4.BeautifulSoup(src_url_parser.text,'html.parser')
	# print(bs4obj)
	# 検索結果一覧ページから取得できる情報を取得
	for list_items in bs4obj.find_all("li",attrs={'class':'Product'}):
		# 画像URL
		auc_imgurl=list_items.find("img",attrs={'class':'Product__imageData'}).get('src')
		# オークション名
		auc_title=list_items.find("a",attrs={'class':'Product__titleLink'}).text
		# URL
		auc_url=list_items.find("a",attrs={'class':'Product__titleLink'}).get('href')
		# 出品者名
		auc_seller=list_items.find("a",attrs={'class':'Product__seller'}).text
		# 出品者のレート
		# 新規はレート無しなのでそれを考慮
		auc_rating=list_items.find("a",attrs={'class':'Product__rating'})
		if auc_rating:
			auc_rating=auc_rating.text
		else:
			auc_rating="0%"
		# 現在価格
		auc_price=list_items.find("span",attrs={'class':'Product__priceValue u-textRed'}).text.replace(",","").replace("円","")
		# 即決価格
		if list_items.select('span[class="Product__priceValue"]'):
			auc_pricewin=list_items.select('span[class="Product__priceValue"]')[0].text.replace(",","").replace("円","")
		else:
			auc_pricewin="-"
		# 入札数
		auc_bid=list_items.find("a",attrs={'class':'Product__bid'}).text
		# 残り時間(auc_time)は「残り日数か時間」と「終了日時」か「残り分」だけの組み合わせなので
		# 「終了日時」があれば「残り日数か時間」と「終了日時」を表示
		# 「終了日時」がなければ「残り分」だけ表示
		auc_time_dayhormin=list_items.find("span",attrs={'class':'Product__time'}).text
		auc_time_detail=list_items.find("span",attrs={'class':'u-textGray u-fontSize10'})
		if auc_time_detail:
			auc_time=auc_time_dayhormin+auc_time_detail.text
		else:
			auc_time=auc_time_dayhormin

		# オークションの詳細ページを解析
		auc_url_parser=requests.get(auc_url)
		bs4obj_auc_url=bs4.BeautifulSoup(auc_url_parser.text,'html.parser')
		# 現在価格と即決価格が同じならば定額、異なればオークションと判断して
		# オークションの場合だけ自動延長の有無を確認
		# 自動延長の有無 auc_auto_ext
		if auc_price!=auc_pricewin:
				auc_auto_ext=bs4obj_auc_url.find("ul",attrs={'class':'ProductDetail__items ProductDetail__items--primary'}).find_all("dd",attrs=
				{'class':'ProductDetail__description'})[3].text.replace("：","")
		else:
			auc_auto_ext="定額のオークション"
		# 商品説明 auc_desc
		auc_desc=bs4obj_auc_url.find("div",attrs={'class':'ProductExplanation__commentArea'}).text
		# タイトルと商品説明で除外キーワードが部分一致しているか判定 auc_title_desc
		auc_title_desc="なし"
		for fo_post_exclude_titledesc in post_exclude_titledesc:
			if fo_post_exclude_titledesc in (auc_title+auc_desc):
				auc_title_desc="あり"
				break

		# ヤフオク標準検索機能以外の条件でスクレイピングしてフィルタ
		filter_flags=[]
		filter_judge=[]
		filter_flags.append("1") if post_auto_ext!="OFF" else filter_flags.append("0")
		filter_flags.append("1") if post_rate!="OFF" else filter_flags.append("0")
		filter_flags.append("1") if post_exclude_id[0]!="OFF" else filter_flags.append("0")
		filter_flags.append("1") if post_exclude_titledesc[0]!="OFF" else filter_flags.append("0")
		# 自動延長のフィルタ
		if filter_flags[0]=="1":
			if (auc_auto_ext=="なし"):
				filter_judge.append("OK")
			else:
				filter_judge.append("NG")
		else:
			filter_judge.append("OK")
		# 評価レートフィルタ
		if filter_flags[1]=="1":
			if (float(auc_rating.replace("%",""))>float(post_rate)):
				filter_judge.append("OK")
			else:
				filter_judge.append("NG")
		else:
			filter_judge.append("OK")
		# 出品者IDフィルタ
		if filter_flags[2]=="1":
			if (auc_seller not in post_exclude_id):
				filter_judge.append("OK")
			else:
				filter_judge.append("NG")
		else:
			filter_judge.append("OK")
		# タイトルと商品説明で部分一致除外フィルタ
		if filter_flags[3]=="1":
			if (auc_title_desc=="なし"):
				filter_judge.append("OK")
			else:
				filter_judge.append("NG")
		else:
			filter_judge.append("OK")

		print(filter_flags)
		print(filter_judge)
		print(auc_url)

		# filter_judgeにNGが含まれていなければappendする
		if "NG" not in filter_judge:
			auc_data_dict.append({'画像URL':auc_imgurl,'オク名':auc_title,'オクURL':auc_url,'出品者ID':auc_seller,'評価レート':auc_rating,'現在価格':auc_price,'即決価格':auc_pricewin,'入札数':auc_bid,'残り時間':auc_time,'自動延長':auc_auto_ext,})


	# サブの1次元辞書データ
	auc_data_sub_dict={'検索URL':src_url,}
	# Djangoテンプレートへ渡すデータ
	django_template_data={'auc_data':auc_data_dict,
												'sub_data':auc_data_sub_dict,
												}
	# print(django_template_data)

	template=loader.get_template('work_apps/output_v2.html')
	return HttpResponse(template.render(django_template_data))
