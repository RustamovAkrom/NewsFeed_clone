from django.shortcuts import render

from apps.news.models import New


def home_page(request):
    news = New.objects.all()
    context = {
        "news": news,
    }
    return render(request, 'news/index.html', context=context)


def contact_page(request):
    return render(request, 'news/contact.html')


def single_page(request, id):
    new = New.objects.get(id=id)
    news = New.objects.all()
    return render(request, 'news/single_page.html', {"new":new, "news":news})


def page_notfound(request):
    return render(request, 'news/404.html')

def about(request):
    return render(request , 'news/about.html')