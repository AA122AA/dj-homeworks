from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Tags(models.Model):

    tag = models.CharField(max_length=50)
    articles = models.ManyToManyField(
        Article, 
        related_name = "tags", 
        through='TagsArticles'
        )

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.tag
    
class TagsArticles(models.Model):

    article = models.ForeignKey(
        Article,
        verbose_name="Статьи",
        on_delete=models.CASCADE
        )
    tags = models.ForeignKey(
        Tags,
        verbose_name="Тэг",
        on_delete=models.CASCADE
        )
    is_main = models.BooleanField(
        verbose_name="Главный тэг",
        blank=True, null=True
        )
