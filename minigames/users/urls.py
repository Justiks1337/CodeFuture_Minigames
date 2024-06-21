from django.urls import path

from users.views import new_user, download_avatar

urlpatterns = [
    path('new_user', new_user),
    path('add_avatar', download_avatar),
]