from django.db import models


class TimestampFields(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    
    class Meta:
        abstract = True
        #abstract = True - сообщает о том, что не нужно 
        #создавать таблицу на основе этого класса. 
        #Если не указать этот флаг, то создастся таблица 
        #TimestampFields. Поля в этой таблице будут связаны
        # автоматически созданным OneToOneField.  


class Project(TimestampFields):
    """Объект на котором проводят измерения."""

    name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()


class Measurement(TimestampFields):
    """Измерение температуры на объекте."""

    value = models.FloatField()
    project = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE, 
        related_name="project"
        )
    image = models.ImageField(upload_to="photos/",null=True)
