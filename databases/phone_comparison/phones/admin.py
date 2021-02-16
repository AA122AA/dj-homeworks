from django.contrib import admin
from .models import Nokia, Samsung, Apple

admin.site.register(Samsung)
admin.site.register(Apple)
admin.site.register(Nokia)

# Register your models here.
