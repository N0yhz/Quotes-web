import os
import django
from pymongo import MongoClient

# from pymongo import MongoClient
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes_web_project.settings")
django.setup()

from quotes.models import Quote, Tag, Author 

client = MongoClient('mongodb+srv://n0yhz:module08@qouteset1.13lvt.mongodb.net/')

db = client.hw10

authors = db.authors.find()

for author in authors:
    Author.objects.get_or_create(
        name = author['name'],
        born_date = author['born_date'],
        born_location = author['born_location'],
        description = author['description']
    )

quotes = db.quotes.find()

for quote in quotes:
    tags = []
    for tag in quote['tags']:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)
    
    exist_quote =bool(len(Quote.objects.filter(quote=quote['quote'])))

    if not exist_quote:
        author = db.authors.find_one({'_id': quote['author']})
        a = Author.objects.get(name=author['name'])
        q = Quote.objects.create(
            quote=quote['quote'],
            author=a,
        )
        for tag in tags:
            q.tags.add(tag)