import re
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


def toppage(request):
		template = loader.get_template("common_page/toppage.html")
		return HttpResponse(template.render({}, request))

def owner(request):
		template = loader.get_template("common_page/owner.html")
		return HttpResponse(template.render({}, request))

def updated(request):
		template = loader.get_template("common_page/updated.html")
		return HttpResponse(template.render({}, request))
