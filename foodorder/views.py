from django.shortcuts import render,redirect
from .models import OurSpeciality
from .models import TodaySpecial
from .models import Product,Orders
from .models import Category
from django.views import View
from middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator
from useraccounts.models import UserProfile

# Create your views here.

class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        quantity = cart.get(product)
        if cart:
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                        request.session['cart'] = cart
                        return redirect('carts')
                else:
                    cart[product] = quantity + 1
                    request.session['cart'] = cart
                    return redirect('carts')
            else:
                cart[product] = 1
        else:
            cart={}
            cart[product] = 1
        request.session['cart']=cart
        print("hello:", request.session.get('user'))
        print(product)
        print("hello:", request.session.get('email'))
        print(request.session['cart'])
        return redirect('index')

    def get(self, request):
        spec = OurSpeciality.objects.all()
        todaySpec = TodaySpecial.objects.all()
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        product = Product.get_all_products()
        category = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            product = Product.get_all_products_by_categoryid(categoryID)
        else:
            product = Product.get_all_products()
        print("hii:", request.session.get('username'))
        data = {}
        data['product'] = product
        data['category'] = category
        return render(request, 'index.html', data)




class Products(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        quantity = cart.get(product)
        if cart:
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                        request.session['cart'] = cart
                        return redirect('carts')
                else:
                    cart[product] = quantity + 1
                    request.session['cart'] = cart
                    return redirect('carts')
            else:
                cart[product] = 1
        else:
            cart={}
            cart[product] = 1
        request.session['cart']=cart
        print("hello:", request.session.get('user'))
        print(product)
        print("hello:", request.session.get('email'))
        print(request.session['cart'])
        return redirect('product')
    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        product = Product.get_all_products()
        category = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            product = Product.get_all_products_by_categoryid(categoryID)
        else:
            product = Product.get_all_products()
        print("hii:", request.session.get('username'))
        data={}
        data['product']= product
        data['category']=category
        return render(request, 'product.html', data)


class Carts(View):
    def post(self, request):
        return redirect('carts')
    def get(self,request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        return render(request, 'carts.html',{'products':products})


class Checkout(View):
    def post(self, request):
        address =request.POST.get('address')
        phone = request.POST.get('phone')
        user_id = request.session.get('user_id')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address,phone,user_id,cart,products)
        for product in products:
            orders = Orders(user_id=user_id,product=product,
                            price=product.price,
                            address=address,
                            quantity=cart.get(str(product.id)),
                            phone=phone)
            orders.save()
        request.session['cart']={}
        return redirect('carts')

class Order(View):
    @method_decorator(auth_middleware)
    def get(self,request):
        user_id=request.session.get('user_id')
        order = Orders.get_orders_by_user(user_id)
        print(order)
        return render(request, 'orders.html',{'order':order})


