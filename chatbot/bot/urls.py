from django.urls import path
from .views import index_new

urlpatterns = [
    path('', index_new, name = 'index_new'),
    # path('room/<str:username>/', chat_room, name = 'chat_room'),
]
