from django import template

register = template.Library()

@register.filter(name='isInCart')
def isInCart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True

    print(product, cart)
    return False

@register.filter(name='cartQuantity')
def cartQuantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0

@register.filter(name='productTotal')
def productTotal(product, cart):
    return product.price * cartQuantity(product, cart)

@register.filter(name='totalPrice')
def totalCartProduct(products, cart):
    sum = 0
    for p in products:
        sum += productTotal(p, cart)
    return sum