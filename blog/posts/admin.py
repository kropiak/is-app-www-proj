from django.contrib import admin

# modele musimy zaimportować
from .models import Category, Topic

# a następnie zarejestrować (pokazano najprostszy przypadek)
admin.site.register(Category)
admin.site.register(Topic)