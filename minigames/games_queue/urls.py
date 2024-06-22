from django.urls import path
from games_queue.views import index

urlpatterns = [
    path('', index, name='index'),
]
