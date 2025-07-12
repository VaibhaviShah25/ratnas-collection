from decimal import Decimal  # ⬅️ Add this at the top
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Cart, Order, Product, DeliveryDetails
from .forms import ContactQueryForm
from django.contrib.auth.decorators import login_required
from django import template



# Create your views here.


def homec(request):
    context = {'user':request.user, 'products':Product.objects.all()}
    return render(request, 'homec.html',context)

def loginc(request):
    if request.method == "POST": # Checking this condition is important because by default request.method is GET which returns None value in request.POST.get('username')
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            User.objects.get(username=username)
        except:
            messages.error(request,"User does not exist")
        user = authenticate(request,username=username,password=password)   # authenticate is used to check if the user is valid or not
        if user is not None:                                                # if user is valid it returns User object else it returns None
            login(request,user)  
            return redirect('homec')
        else:
            messages.error(request,"Username or Password is incorrect")
        
    context = {}
    return render(request,"loginc.html",{"page":"login"})
    return render(request, 'loginc.html')

def logoutc(request):
    logout(request)
    return redirect('loginc')  # redirect to login page after logout

def registerc(request):
    form = UserCreationForm() # this is the default form provided by django for user registration
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False) # commit = False means we need to work on current user object and not save it in the database
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('homec')
        else:
            messages.error(request,"An error occured during registration")
    return render(request,"loginc.html",{"page":"register","form":form}) 


def cartc(request):
    if not request.user.is_authenticated:
        return redirect('loginc')  # Redirect if user is not logged in
    
    # Fetch only the cart items for the logged-in user
    cart_items = Cart.objects.filter(user=request.user)
    total_amount = Decimal('0.00')
    cart_data = []

    for item in cart_items:
        subtotal = item.product.price * item.quantity
        total_amount += subtotal

        cart_data.append({
            'item': item,
            'subtotal': subtotal,
        })

    return render(request, 'cartc.html', {
        'cart_data': cart_data,
        'total_amount': total_amount,
    })



@login_required
def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('loginc')  # Redirect if user is not logged in
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f"{product.name} added to cart!")
    return redirect('cartc')  # or redirect back to product page

def update_quantity(request, cart_item_id):
    if request.method == "POST":
        action = request.POST.get("action")
        cart_item = get_object_or_404(Cart, id=cart_item_id, user=request.user)

        if action == "increase":
            cart_item.quantity += 1
        elif action == "decrease" and cart_item.quantity > 1:
            cart_item.quantity -= 1

        cart_item.save()
        messages.success(request, "Quantity updated.")

    return redirect('cartc')


register = template.Library()

@register.filter
def multiply(price, quantity):
    return price * quantity

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    cart_item.delete()
    messages.success(request, "Item removed from cart.")
    return redirect('cartc')


@login_required
def place_order(request):
    cart_items = Cart.objects.filter(user=request.user)
    cart_items.delete()  # Clear cart after placing order
    messages.success(request, "Order placed successfully!")
    return redirect('homec')

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})


def aboutc(request):
    return render(request, 'aboutc.html')


'''def orderc(request):
    if not request.user.is_authenticated:
        return redirect('loginc')  # Redirect if user is not logged in
    
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orderc.html', {'orders': orders})'''


#order page views
@login_required
def orderc(request):
    if not request.user.is_authenticated:
        return redirect('loginc')  # Redirect if user is not logged in
    cart_items = Cart.objects.filter(user=request.user)
    total_amount = 0
    item_data = []

    for item in cart_items:
        subtotal = item.product.price * item.quantity
        item_data.append({
            'item': item,
            'subtotal': subtotal
        })
        total_amount += subtotal

    context = {
        'cart_items': item_data,
        'total_amount': total_amount
    }
    return render(request, 'orderc.html', context)


@login_required
def confirm_order(request):
    if request.method == 'POST':
        # place order logic here (save Order model, clear cart, etc.)
        messages.success(request, "Your order has been placed!")
        return redirect('homec')


@login_required

def deliveryc(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')

        if name and phone and address and pincode:
            DeliveryDetails.objects.create(
                user=request.user, 
                name=name,
                phone=phone,
                address=address,
                pincode=pincode
            )
            return redirect('paymentc')  # make sure 'paymentc' exists in your urls

    return render(request, 'deliveryc.html')


@login_required
def paymentc(request):
    return render(request, 'paymentc.html')


@login_required
def payment_confirm(request):
    if request.method == "POST":
        method = request.POST.get('payment_method')
        # Save payment method or process
        messages.success(request, f"Payment method '{method}' selected successfully.")
        return redirect('homec')  # or order confirmation page





def contactc(request):
    if request.method == 'POST':
        form = ContactQueryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact_success.html')
    else:
        form = ContactQueryForm()
    return render(request, 'contactc.html', {'form': form})