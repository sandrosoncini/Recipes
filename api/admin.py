from django.contrib import admin
from django.conf.urls.static import static
from .models import Recipes

# Register your models here.

admin.site.register(Recipes)