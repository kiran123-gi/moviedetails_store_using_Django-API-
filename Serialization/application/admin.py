from django.contrib import admin
from .models import MovieModels
class MovieAdmin(admin.ModelAdmin):
    list_display = ['sno','name','hero','heroine','director','music']
admin.site.register(MovieModels,MovieAdmin) 