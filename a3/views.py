from django.shortcuts import render
from newsapi import NewsApiClient
from django.http import HttpResponse
import requests
from .models import Read
# Create your views here.

#def news_view(request):
#    newsapi = NewsApiClient(api_key='b87e1090881c4999ac72b942dfab89dc')

#    response = newsapi.get_top_headlines(country='jp',
                                         #category='science')
#    return render(request, "read.html", {"response": response})


def news_view(request):
    # BBC news api
    # following query parameters are used
    # source, sortBy and apiKey
    query_params = {
        "country": "jp",
        "category": "science",
        "apiKey": "b87e1090881c4999ac72b942dfab89dc"
    }
    main_url = "https://newsapi.org/v2/top-headlines"

    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_page = res.json()

    # getting all articles in a string article
    article = open_page["articles"]

    # empty list which will
    # contain all trending news
    title = []
    description = []

    for ar in article:
        title.append(ar["title"])
    for ar in article:
        description.append(ar["description"])

    for i in range(len(title)):
        # printing all trending news
        print(i + 1, title[i])
        print(description[i])

    obj_2 = Read.objects.all()
    return render(request, "read.html", {'obj_2': obj_2})
