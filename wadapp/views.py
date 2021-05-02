from django.shortcuts import render, redirect

# Create your views here.

from .models.product import Product
from .models.category import Category
from .models.main_books import Main_book
from .models.new_releases import New_releases
from .models.customer import Customer
from .models.orders import Order
from .models.downloadbooks import DownloadBook
from .models.usedbooks import Usedbook
from django.views import View
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages, auth
from django.http import *


class Home(View):

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1

                else:
                    cart[product] = quantity + 1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('Cart', request.session['cart'])
        return redirect('Home')

    def get(self, request):

        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        categories = Category.get_all_categories()
        mainbooks = Main_book.get_all_main_books()

        newproducts = New_releases.get_all_newreleases()

        return render(request, 'Home.html',
                      {'categories': categories, 'main_books': mainbooks, 'newproducts': newproducts})


def category(request):
    products = None
    categories = Category.get_all_categories()
    catgoryID = request.GET.get('category')
    if catgoryID:
        products = Product.get_all_products_by_id(catgoryID)
    else:
        products = Product.get_all_products();

    data = {products: products, categories: categories}

    return render(request, 'category.html', {'products': products})


def bookpage(request):
    name = request.GET.get('name')
    if name:
        products = Product.get_products_by_name(name)
    else:
        products = Product.get_all_products();

    return render(request, 'bookpage.html', {'products': products})


def newbookpage(request):
    name = request.GET.get('name')
    if name:
        products1 = New_releases.get_newreleases_by_name(name)
    else:
        products1 = New_releases.get_all_newreleases()

    return render(request, 'newbookpage.html', {'products1': products1})


def downloadbooks(request):
    dlbooks = DownloadBook.get_all_downloadbooks()
    return render(request, 'downloadbooks.html', {'dlbooks': dlbooks})


def new_releases(request):
    prds1 = New_releases.get_all_newreleases()
    return render(request, 'new_releases.html', {'products1': prds1})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        pswd1 = request.POST.get('pswd1')
        customer_mail = Customer.get_by_email(email)
        customer_pswd = Customer.get_by_password(pswd1)
        error_message = None
        if customer_mail:
            pass
            if customer_pswd:
                email = request.session['email'] = customer_mail.email
                return redirect('Home')
            else:
                error_message = 'Email or Password invalid'
        else:
            error_message = 'Email or Password invalid'
    return render(request, 'login.html', {'error': error_message})


def profile(request):
    if request.method == 'GET':
        return render(request, 'profile.html')
    else:
        pd = request.POST
        username = pd.get('username')
        email = pd.get('email')
        pswd1 = pd.get('pswd1')
        pswd2 = pd.get('pswd2')
        # valid
        value = {
            'username': username,
            'email': email,
            'pswd1': pswd1,
            'pswd2': pswd2
        }
        error_message = None
        customer = Customer(
            username=username,
            email=email,
            pswd1=pswd1,
            pswd2=pswd2
        )
        if len(pswd1) < 5:
            error_message = "Length must be greater than 5"
        else:
            r1 = True
            r2 = True
            for i in pswd1:
                if i.isupper():
                    r1 = False
                    break
            for j in pswd1:
                if (33 <= ord(j) <= 47):
                    r2 = False
                    break
                elif (58 <= ord(j) <= 64):
                    r2 = False
                    break
            if r2 or r1:
                error_message = "Password must contain a Capital and Special Character"
        if (pswd1 != pswd2):
            error_message = "Both passwords didn't match"
        elif customer.isExists():
            error_message = 'Email already registered..'
        # Saving
        if not error_message:

            customer.register()
            email = request.session['email'] = customer.email
            return Home(request)
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'profile.html', data)


def logout(request):
    request.session.clear()
    return redirect('login')


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        usedbooks = Usedbook.get_usedbooks_by_id(ids)
        newbooks = New_releases.get_newreleases_by_id(ids)
        books = [products, usedbooks, newbooks]

        print(books)
        return render(request, 'cart.html',
                      {'books': books, 'products': products, 'usedbooks': usedbooks, 'newbooks': newbooks})


def search(request):
    if request.method == 'POST':
        srch = request.POST.get('srh')
        if srch:
            match = Product.objects.filter(Q(name__icontains=srch))
            if match:
                return render(request, 'search.html', {'sr': match})
            else:
                return render(request, 'notfound.html')

        else:
            return HttpResponseRedirect("/")
    return render(request, 'search.html')


class checkout(View):
    def post(self, request):
        pd = request.POST
        email = pd.get('email')
        print(email)
        customer = Customer.get_by_email(email)
        cart = request.session.get('cart')
        print(request.POST)
        print(customer)

        products = Product.get_products_by_id(list(cart.keys()))
        usedbooks = Usedbook.get_usedbooks_by_id(list(cart.keys()))
        newbooks = New_releases.get_newreleases_by_id(list(cart.keys()))

        books = [products, usedbooks, newbooks]

        print(cart, books)

        for product in products:
            order = Order(product=product,
                          customer=customer,
                          quantity=cart.get(str(product.id)),
                          price=product.price,
                          address=request.POST.get('address'),
                          phone=request.POST.get('phone'))
            order.placeOrder();
            order.save()

        for usedbook in usedbooks:
            order = Order(usedbook=usedbook,
                          customer=customer,
                          quantity=cart.get(str(usedbook.id)),
                          price=usedbook.price,
                          address=request.POST.get('address'),
                          phone=request.POST.get('phone'))
            order.placeOrder();
            order.save()
        for newbook in newbooks:
            order = Order(newbook=newbook,
                          customer=customer,
                          quantity=cart.get(str(newbook.id)),
                          price=newbook.price,
                          address=request.POST.get('address'),
                          phone=request.POST.get('phone'))
            order.placeOrder();
            order.save()

        request.session['cart'] = {}
        return redirect('cart')

    def get(self, request):
        return render(request, 'checkout.html')


class orders(View):

    def get(self, request):
        email = request.session.get('email')
        print(email)
        customer = Customer.get_by_email(email)

        print(customer)

        orders = Order.get_orders_by_customer(str(customer.id))

        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        usedbooks = Usedbook.get_usedbooks_by_id(list(cart.keys()))
        newbooks = New_releases.get_newreleases_by_id(list(cart.keys()))

        return render(request, 'orders.html', {'orders': orders,'products':products,'usedbooks': usedbooks,'newbooks': newbooks})


def myaccount(request):
    email = request.session.get('email')
    return render(request, 'myaccount.html', {'email': email})


def usedbooks(request):
    name = request.GET.get('name')
    if name:
        usedbooks = Usedbook.get_usedbooks_by_name(name)
    else:
        usedbooks = Usedbook.get_all_usedbooks()

    return render(request, 'usedbooks.html', {'usedbooks': usedbooks})


def returnbook(request):
    return render(request, 'returnbook.html')


def refund(request):
    return render(request, 'refund.html')


def displaymsg(request):
    return render(request, 'displaymsg.html')
