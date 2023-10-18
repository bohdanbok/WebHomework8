from datetime import datetime

from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import DateTimeField, EmbeddedDocumentField, ListField, StringField, \
    ReferenceField


class Tag(EmbeddedDocument):
    name = StringField()


class Author(Document):
    fullname = StringField()
    born_date = DateTimeField()
    born_location = StringField()
    description = StringField()
    meta = {'allow_inheritance': True}


class Quote(Document):
    author = ReferenceField(Author)
    quote = StringField()
    tags = ListField()
    meta = {'allow_inheritance': True}
