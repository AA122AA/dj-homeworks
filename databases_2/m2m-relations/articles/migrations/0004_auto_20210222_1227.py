# Generated by Django 3.1.2 on 2021-02-22 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_tagsarticles_is_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='articles',
            field=models.ManyToManyField(through='articles.TagsArticles', to='articles.Article'),
        ),
        migrations.AlterField(
            model_name='tagsarticles',
            name='tags',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='articles.tags', verbose_name='Тэг'),
        ),
    ]
