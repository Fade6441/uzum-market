import json

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.models import AnonymousUser
from django.contrib import messages
from django.db.models import Q
from .models import Product, Cart, CartItem
from users.models import CustomUser, UserTypeChoices


def product_list(request):
    products = Product.objects.all()
    search_q = request.GET.get('q')
    if search_q:
        products = Product.objects.filter(
            Q(name__icontains=search_q) | Q(description__icontains=search_q)
        )


    context = {
        'products': products
    }
    

    return render(request, 'products/product-list.html', context=context)


def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product': product
    }
    return render(request, 'products/product-detail.html', context=context)


def add_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')
        quantity = data.get('quantity')

        product = get_object_or_404(Product, id=product_id)
        # product = Product.objects.get(id=product_id)

        cart, created = Cart.objects.get_or_create(user=request.user, is_active=True)
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not item_created:
            cart_item.quantity += 1
        else:
            cart_item.quantity = 1

        cart_item.save()
        
        return JsonResponse(data={'status':'okey'})

    return JsonResponse(data={'status':'error'})


def delete_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')


        product = get_object_or_404(Product, id=product_id)
        # product = Product.objects.get(id=product_id)

        cart, created = Cart.objects.get_or_create(user=request.user, is_active=True)
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

        if request.method == 'POST':
            product.delete()
            return redirect('product_list')

        cart_item.save()
        
    return render(request, 'confirm_delete.html', context={'product':product})


def user_cart(request):
    if request.method == "GET":
        user: CustomUser = request.user

        if isinstance(user, AnonymousUser):
            messages.info(request, "Oldin login qilgin {}")
            return redirect("users:login")



        cart = Cart.objects.get(user=user, is_active=True)
        context = {
            'cart': cart
        }

        return render(
            request, 
            template_name='products/user_cart.html', 
            context=context)