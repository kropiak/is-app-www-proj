from django.urls import path, include
from . import api_views

# pamiętaj, że te reguły, mimo, że bardzo podobne do zdefiniowanych w poprzednich
# zadaniach dotyczą endpointów dla REST API, a nie widoków dla szablonów HTML
urlpatterns = [
    path('topics/', api_views.topic_list),
    path('topics/<int:pk>/', api_views.topic_detail),
    path('topics/update/<int:pk>/', api_views.topic_update_delete),
    path('topics/delete/<int:pk>/', api_views.topic_update_delete),
    path('topics/search/<str:keyword>/', api_views.find_topic_by_keyword),
    path('categories/', api_views.category_list),
    path('categories/<int:pk>/', api_views.category_detail),
    path('posts/', api_views.PostList.as_view()),
]