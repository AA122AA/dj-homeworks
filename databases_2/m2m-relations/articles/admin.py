from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tags, TagsArticles


class TagsInlineFormset(BaseInlineFormSet):
    def clean(self):
        arr_main = []
        for form in self.forms:
            print("\n", form.cleaned_data, "\n")
            if form.cleaned_data.get("is_main"):
                arr_main.append(form.cleaned_data)
            if form.cleaned_data.get("article"):
                pass
            else:
                return super().clean()
        if len(arr_main) > 1:
            raise ValidationError('Главный тэг может быть только один')
        elif len(arr_main) == 0:
            raise ValidationError('Выберите главный тэг')
        else:
            return super().clean()

class InlineTags(admin.TabularInline):
    model = TagsArticles
    formset = TagsInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (InlineTags,)

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):    
    inlines = (InlineTags,)

    
