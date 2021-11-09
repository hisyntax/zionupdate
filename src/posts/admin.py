from django.contrib import admin
from .models import Sermon, Song, Article, Category, Tag, SongMinister, SermonMinister, SermonYear

admin.site.register(Sermon)
admin.site.register(Song)
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(SermonMinister)
admin.site.register(SongMinister)
admin.site.register(SermonYear)