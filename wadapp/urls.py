
from django.urls import path
from .import views

urlpatterns = [
    path('', views.login, name='login'),
    path('profile', views.profile, name='profile'),
    path('Home', views.Home,name='Home'),path('category',views.category,name='category'),path('bookpage',views.bookpage,name='bookpage'),
    path('booksdownload',views.booksdownload,name='booksdownload'),path('new_releases', views.new_releases, name='new_releases'),
]