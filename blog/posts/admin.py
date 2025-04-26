from django.contrib import admin

# modele musimy zaimportować
from .models import Category, Kategoria, Produkt, Topic, Post


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "modified_at"]

# a następnie zarejestrować (pokazano najprostszy przypadek)
admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Produkt)
admin.site.register(Kategoria)
admin.site.register(Post, PostAdmin)

# C - CREATE
# R - RETRIEVE
# U - UPDATE
# D - DELETE


# SOLID - akronim używany w programowaniu obiektowym
# O - OPEN/CLOSED - otwarte na rozszerzanie, ale zamknięty na modyfikację