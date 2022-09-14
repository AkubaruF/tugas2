from pdb import post_mortem
from django.contrib import admin

# Register your models here.
from .models import Person, Post
admin.site.register(Person)
admin.site.register(Post)