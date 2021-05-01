from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if id == str(product.id):
            return True;
    return False;


@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if id == str(product.id):
            return cart.get(id);
    return 0;


@register.filter(name='price_total')
def price_total(product, cart):
    return product.price * cart_quantity(product, cart)


@register.filter(name='ubook_price_total')
def ubook_price_total(usedbook, cart):
    return usedbook.price * cart_quantity(usedbook, cart)


@register.filter(name='newbook_price_total')
def newbook_price_total(newbook, cart):
    return newbook.price * cart_quantity(newbook, cart)


@register.filter(name='total_cart_price')
def total_cart_price(books, cart):
    sum1 = 0;
    sum2 = 0;
    sum3 = 0;
    products = books[0]
    usedbooks = books[1]
    newbooks = books[2]

    for p in products:
        sum1 += price_total(p, cart)
    for q in usedbooks:
        sum2 += ubook_price_total(q, cart)
    for r in newbooks:
        sum3 += newbook_price_total(r, cart)

    return sum1 + sum2 + sum3

@register.filter(name='find_by_price')
def find_by_price(order):
    if order.price == order.product.price:
        name = order.product.name
    elif order.price == order.usedbook.price:
        name = order.usedbook.name
    else:
        name = order.newbook.name
    return name

@register.filter(name='find_by_image')
def find_by_image(order):
    if order.price == order.product.price:
        image = order.product.image
    elif order.price == order.usedbook.price:
        image = order.usedbook.image
    else:
        image = order.newbook.image
    return image.url