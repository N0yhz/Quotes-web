from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .utils import get_mongodb
from .forms import AuthorForm, QuotesForm
from .models import Author, Quote

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

@login_required
def quote(request):
    author = Author.objects.all()

    if request.method == 'POST':
        form = QuotesForm(request.POST)
        if form.is_valid():
            new_quote = form.save()

            choice_author = Author.objects.filter(name__in=request.POST.getlist('author'))
            for tag in choice_author.iterator():
                new_quote.author.add(tag)

            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/quotes.html', {"auhtor": author, 'form': form})

    return render(request, 'quotes/quotes.html', {"author": author, 'form': QuotesForm()})


@login_required
def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/author.html', {'form': form})

    return render(request, 'quotes/author.html', {'form': AuthorForm()})

def quotes_by_tag(request, tag):
    quotes = Quote.objects.filter(tags__name= tag)
    return render(request, 'quotes/quotes_by_tag.html', {'quotes': quotes, 'tag': tag})

def add_quote(request): 
    if request.method == 'POST': 
        form = QuotesForm(request.POST) 
        if form.is_valid():
            form.save() 
            return redirect(to='quotes:root') 
    else: 
        form = QuotesForm() 
    return render(request, 'quotes/add_quote.html', {'form': form})