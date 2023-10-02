from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Reporter, Article
from datetime import date

# Create your views here.


def create(request):
    rep = Reporter(first_name='Juanjo', last_name='Ruiz',
                   email='jua@gmail.com')
    rep.save()
    art = Article(headline='Articulo 1',  pub_date=date.today(), reporter=rep)
    art.save()
    art2 = Article(headline='Articulo 2',
                   pub_date=date.today(), reporter=rep)
    art2.save()
    art3 = Article(headline='Articulo 3',
                   pub_date=date.today(), reporter=rep)
    art3.save()

    # result = art.reporter.first_name
    result = rep.article_set.all()
    result = rep.article_set.filter(headline='Articulo 2')
    result = rep.article_set.count()
    return HttpResponse(result)
