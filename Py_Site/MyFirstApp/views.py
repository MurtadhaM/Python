from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
import Spider as Spider


def index(request):
    s = Spider.Spider('https://charlotte.edu', 5)
    s.print_log()

    return HttpResponse(s.urls)

    # print(s.external_urls)


def template(request):
    return render(request, 'index.html')
