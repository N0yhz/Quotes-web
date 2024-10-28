import json
from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient('mongodb+srv://n0yhz:module08@qouteset1.13lvt.mongodb.net/')

db = client.hw10

with open('utils/quotes.json', 'r', encoding ='utf-8') as file:
    quotes = json.load(file)

for quote in quotes:
    # Check if 'author' and 'quote' keys are in the quote dictionary
    author_name = quote.get('author')
    quote_text = quote.get('quote')
    
    if author_name and quote_text:  # Proceed only if both keys are present
        author = db.authors.find_one({'name': author_name})
        
        if author:
            db.quotes.insert_one({
                'quote': quote_text,
                'tags': quote.get('tags', []),  # Default to an empty list if 'tags' is missing
                'author': ObjectId(author['_id']),
            })
    else:
        print(f"Skipping quote due to missing 'author' or 'quote': {quote}")
