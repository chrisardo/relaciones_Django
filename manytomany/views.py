from django.shortcuts import render
from turtle import title
from django.http import HttpResponse
from .models import Article, Publication

# Create your views here.


def create(request):
    '''
    art1 = Article(headline="Articulo 1")
    art1.save()
    art2 = Article(headline="Articulo 2")
    art2.save()
    art3 = Article(headline="Articulo 3")
    art3.save()
    pub1 = Publication(title="Publicacion 1")
    pub1.save()
    pub1 = Publication(title="Publicacion 1")
    pub1.save()
    pub2 = Publication(title="Publicacion 2")
    pub2.save()
    pub3 = Publication(title="Publicacion 3")
    pub3.save()
    pub4 = Publication(title="Publicacion 4")
    pub4.save()
    pub5 = Publication(title="Publicacion 5")
    pub5.save()
    pub6 = Publication(title="Publicacion 6")
    pub6.save()

    # Haciendo las relaciones
    art1.publications.add(pub1)
    art1.publications.add(pub2)
    art1.publications.add(pub3)
    art2.publications.add(pub4)
    art2.publications.add(pub5)
    art3.publications.add(pub6)
        result = art1.publications.all()
    '''
    pub1 = Publication.objects.get(id=2)
    result = pub1.article_set.all()
# art1.publications.remove(pub1) ->Remover el articulo de diche relacion

    return HttpResponse(result)
