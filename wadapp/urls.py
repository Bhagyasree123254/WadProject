from django.urls import path
from . import views
from .views import Home, logout, Cart ,checkout,orders

urlpatterns = [
    path('', views.login, name='login'),
    path('profile', views.profile, name='profile'),
    path('Home', Home.as_view(), name='Home'),
    path('category', views.category, name='category'),
    path('bookpage', views.bookpage, name='bookpage'),
    path('newbookpage', views.newbookpage, name='newbookpage'),
    path('downloadbooks', views.downloadbooks, name='downloadbooks'),
    path('new_releases', views.new_releases, name='new_releases'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name="cart"),
    path('search', views.search, name='search'),
    path('myaccount', views.myaccount, name='myaccount'),
    path('checkout', checkout.as_view(), name="checkout"),
    path('orders', orders.as_view(), name="orders"),

]
