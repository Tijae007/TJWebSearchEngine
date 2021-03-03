from django.urls import path

from .views import Home, Search
app_name = 'search_app'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('search/', Search.as_view(), name='search'),
]

