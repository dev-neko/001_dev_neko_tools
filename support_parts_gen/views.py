from django.http import HttpResponse
from django.template import loader

def input(request):
	template=loader.get_template("support_parts_gen/input.html")
	return HttpResponse(template.render({},request))

