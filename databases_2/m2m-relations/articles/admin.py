from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tags, TagsArticles


class TagsInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            form.cleaned_data
            print(form)
            print("\n in form \n")
            if form.cleaned_data.get("is_main"):
                return super().clean()
            else:
                raise ValidationError('Укажите главный тэг')
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            raise ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода

class InlineTags(admin.TabularInline):
    model = TagsArticles
    formset = TagsInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (InlineTags,)

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):    
    inlines = (InlineTags,)

    
