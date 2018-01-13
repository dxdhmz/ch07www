# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from mysite import models

# Create your views here.

def index(request):
    products = models.Product.objects.all()
    temp = get_template('index.html')
    html = temp.render(locals())
    return HttpResponse(html)

def show_mobile(request,id):
    try:
        model=models.PModel.objects.get(name=id)
        product = models.Product.objects.get(pmodel=model)
    except:
        pass
    temp = get_template("detail.html")
    html = temp.render(locals())
    return HttpResponse(html)