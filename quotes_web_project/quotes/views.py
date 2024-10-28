from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Quote, Tag

from .utils import get_mongodb

# Create your views here.

def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    try:
        quotes_on_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        quotes_on_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        quotes_on_page = paginator.page(paginator.num_pages)
    return render( request, 'quotes/index.html', context={'quotes': quotes_on_page})

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'quotes/tag_list.html', context={'tag': tags})

def quotes_by_tag(request, tag_id):
    tags = get_object_or_404(Tag, id =tag_id)
    quotes = Quote.objects.filter(tag=tags)
    return render(request, 'quotes/quotes_by_tag.html', context={'quote': quotes, 'tag': tags})