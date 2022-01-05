from django.contrib import admin
from .models import Post

admin.site.register(Post)


# """ documentation

# imports the whole admin framework included in django

# then imports the Post class from models.py. The model.py is python code that interacts with database (ORM/ database-abstraction API ???) 

# "models" refers to database

# """

