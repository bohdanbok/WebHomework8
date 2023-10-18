from models import Tag, Author, Quote
from datetime import datetime
import connect
import json

with open('authors.json', 'r') as authors:
    data = json.load(authors)
    for author in data:
        existing_author = Author.objects(fullname=author['fullname']).first()

        if existing_author:
            pass
        else:
            date = datetime.strptime(author['born_date'], "%B %d, %Y")
            author_obj = Author(fullname=author['fullname'], born_date=date,
                                born_location=author['born_location'],
                                description=author['description'])
            print(author_obj.born_date)
            author_obj.save()

with open('quotes.json', 'r') as quotes:
    data = json.load(quotes)
    for quote in data:
        existing_quote = Quote.objects.filter(quote=quote['quote']).first()
        if existing_quote:
            print("Quote already exists")
        else:
            list_tags = []
            for tag in quote['tags']:
                masculine = Tag(name=tag)
                list_tags.append(masculine)
            quote_obj = Quote(author=quote['author'], quote=quote['quote'], tags=list_tags)
            quote_obj.save()
