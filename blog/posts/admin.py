from django.contrib import admin

# modele musimy zaimportować
from .models import Category, Topic

# a następnie zarejestrować (pokazano najprostszy przypadek)
admin.site.register(Category)
admin.site.register(Topic)

# C - CREATE
# R - RETRIEVE
# U - UPDATE
# D - DELETE


# SOLID - akronim używany w programowaniu obiektowym
# O - OPEN/CLOSED - otwarte na rozszerzanie, ale zamknięty na modyfikację