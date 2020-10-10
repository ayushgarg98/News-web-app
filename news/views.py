from django.shortcuts import render
from newsapi import NewsApiClient
from django.http import JsonResponse
import json


def index(request):
    newsapi = NewsApiClient(api_key='API-KEY')
    top_headlines = newsapi.get_top_headlines(language='en',
                                              country='in')

    articles = top_headlines['articles']

    desc = []
    news = []
    img = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])

    mylist = zip(news, desc, img,url)

    return render(request, 'index.html', context={"mylist": mylist})


def international(request):
    newsapi = NewsApiClient(api_key='API-KEY')
    top_headlines = newsapi.get_top_headlines(language='en')

    articles = top_headlines['articles']

    desc = []
    news = []
    img = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])

    mylist = zip(news, desc, img,url)

    return render(request, 'international.html', context={"mylist": mylist})


def sports(request):
    newsapi = NewsApiClient(api_key='API-KEY')
    top_headlines = newsapi.get_top_headlines(language='en',
                                              country='in',
                                              category='sports')

    articles = top_headlines['articles']

    desc = []
    news = []
    img = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])

    mylist = zip(news, desc, img,url)

    return render(request, 'sports.html', context={"mylist": mylist})


def business(request):
    newsapi = NewsApiClient(api_key='API-KEY')
    top_headlines = newsapi.get_top_headlines(language='en',
                                              country='in',
                                              category='business')

    articles = top_headlines['articles']

    desc = []
    news = []
    img = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])

    mylist = zip(news, desc, img,url)

    return render(request, 'business.html', context={"mylist": mylist})


def technology(request):
    newsapi = NewsApiClient(api_key='API-KEY')
    top_headlines = newsapi.get_top_headlines(language='en',
                                              country='in',
                                              category='technology')

    articles = top_headlines['articles']

    desc = []
    news = []
    img = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])

    mylist = zip(news, desc, img,url)

    return render(request, 'tech.html', context={"mylist": mylist})


def search(request, q):
    newsapi = NewsApiClient(api_key='API-KEY')
    top_headlines = newsapi.get_top_headlines(language='en',
                                              q=q)

    articles = top_headlines['articles']

    desc = []
    news = []
    img = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])

    mylist = zip(news, desc, img, url)
    # json_string = json.dumps(mylist)
    return render(request, 'search.html', context={"mylist": mylist})
