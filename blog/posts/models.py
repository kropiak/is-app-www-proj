from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(null=True, blank=True)
    # Ctrl + / - dodanie/usunięcie komentarza

class Topic(models.Model):
    name = models.CharField(max_length=60)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"Topic : {self.name}, dodany {self.created}, w kategorii {self.category.name}." 
    
    def __str__(self):
        return self.name

class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.content[:20] + "..."

    # Shift + Alt + strzałki góra/dół - powielanie linii, w której znajduje się karetka
