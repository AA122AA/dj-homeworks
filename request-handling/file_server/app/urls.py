from app.views import file_list, file_content
from django.urls import path, register_converter
from datetime import datetime

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам

class DateConvertor:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value):
        return datetime.strptime(value, "%Y-%m-%d")

    def to_url(self, value:datetime):
        return value.strftime("%Y-%m-%d")

register_converter(DateConvertor, "datetime")
urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    path("", file_list, name='file_list'),
    path("<datetime:date>/", file_list, name='file_list'),    # задайте необязательный параметр "date"
                                      # для детальной информации смотрите HTML-шаблоны в директории templates
    path("content/<str:name>/", file_content, name='file_content'),
]
