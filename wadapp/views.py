from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.new_releases import New_releases
from .models.customer import Customer



def Home(request):
    products = None
    categories = Category.get_all_categories()
    catgoryID= request.GET.get('category')
    if catgoryID:
        products = Product.get_all_products_by_id(catgoryID)
    else:
        products = Product.get_all_products();

    data= {products: products, categories: categories}
    return render(request, 'Home.html', {'categories': categories})



def category(request):
    products = None
    categories = Category.get_all_categories()
    catgoryID = request.GET.get('category')
    if catgoryID:
        products = Product.get_all_products_by_id(catgoryID)
    else:
        products = Product.get_all_products();

    data = {products: products, categories: categories}


    return render(request, 'category.html', {'products':products})


def bookpage(request):
    name=request.GET.get('name')
    if name:
        products = Product.get_products_by_name(name)
    else:
        products = Product.get_all_products();

    return render(request,'bookpage.html',{'products': products})


def booksdownload(request):
    products=Product.get_all_products()
    return render(request,'booksdownload.html',{'products':products})

def new_releases(request):
    prds1=New_releases.get_all_newreleases()
    return render(request, 'new_releases.html', {'products1': prds1})

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        pswd1=request.POST.get('pswd1')
        customer_mail = Customer.get_by_email(email)
        customer_pswd = Customer.get_by_password(pswd1)
        error_message=None
        if customer_mail:
            pass
            if customer_pswd:
                return Home(request)
            else:
                error_message = 'Email or Password invalid'
        else:
            error_message = 'Email or Password invalid'
    return render(request, 'login.html', {'error': error_message})

def profile(request):
    if request.method == 'GET' :
        return render(request,'profile.html')
    else:
        pd = request.POST
        username = pd.get('username')
        email=pd.get('email')
        pswd1=pd.get('pswd1')
        pswd2=pd.get('pswd2')
        #valid
        value={
            'username' : username,
            'email' : email,
            'pswd1' : pswd1,
            'pswd2' : pswd2
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
            r1=True
            r2=True
            for i in pswd1:
                if i.isupper():
                    r1 = False
                    break
            for j in pswd1:
                if(33<= ord(j) <=47):
                    r2 = False
                    break
                elif(58 <=ord(j) <=64):
                    r2 = False
                    break
            if r2 or r1 :
                error_message="Password must contain a Capital and Special Character"
        if(pswd1 != pswd2):
            error_message = "Both passwords didn't match"
        elif customer.isExists():
            error_message = 'Email already registered..'
        #Saving
        if not error_message:

            customer.register()
            return Home(request)
        else:
            data={
                'error':error_message,
                'values':value
            }
            return render(request, 'profile.html', data)

