
from django.urls import path
from .import views

urlpatterns = [
    path('', views.Home,name='Home'),path('category',views.category,name='category'),path('bookpage',views.bookpage,name='bookpage'),
    path('booksdownload',views.booksdownload,name='booksdownload'),
]