from django.urls import path
from . import views


urlpatterns = [
    path("welcome", views.welcome_view),
    path("topics", views.topic_list),
    path("topic/<int:id>", views.topic_detail),
    path("categories", views.category_list),
    path("category/<int:id>", views.category_detail),
]