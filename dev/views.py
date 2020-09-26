from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.template import loader
import json


def slider(request):
		template = loader.get_template("dev/slider.html")
		return HttpResponse(template.render({}, request))

def for_ajax(request):    # AJAXに答える関数
	if request.method == 'POST':
		txt = request.POST['your_txt']  # POSTデータを取得して
		print(txt)
		response = txt + "!!!"  # 加工
		# response = json.dumps({'your_surprise_txt':surprise_txt,})  # JSON形式に直して・・
		# 返す。JSONはjavascript扱いなのか・・
		return HttpResponse(response)
	else:
		raise Http404  # GETリクエストを404扱いにしているが、実際は別にしなくてもいいかも

def kihu_parts_gen(request):
	template=loader.get_template("dev/kihu_parts_gen.html")
	return HttpResponse(template.render({},request))

def modal01(request):
	template=loader.get_template("dev/modal01.html")
	return HttpResponse(template.render({},request))

def tame(request):
	template=loader.get_template("dev/tame.html")
	return HttpResponse(template.render({},request))

