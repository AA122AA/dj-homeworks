from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin

from .models import Article, Tags, TagsArticles

class InlineTags(admin.TabularInline):
    model = TagsArticles
    # extra =1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (InlineTags,)

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):    
    inlines = (InlineTags,)

    
