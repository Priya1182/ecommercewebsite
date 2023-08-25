from django.shortcuts import render,redirect,get_object_or_404
from django.conf.urls import url
from django.contrib.auth.models import User,auth
from django.contrib import messages
from cart.models import Category,Product,contactIn,CartItem


# Create your views here.
def index(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {'category': category, 'categories': categories, 'products': products}

    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def userprofile(request):
    return render(request,'userprofile.html')

def cart(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    for item in cart_items:
        item.total_price = item.product.price * item.quantity
    total_cart_value = sum(item.product.price * item.quantity for item in cart_items)
    shipping_fee = 100
    final_cart_value =total_cart_value + shipping_fee   
    return render(request,'cart.html',{'cart_items': cart_items,'total_cart_value': total_cart_value,'final_cart_value':final_cart_value,'shipping_fee':shipping_fee})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email =request.POST['email']
        phone =request.POST['phone']
        subject =request.POST['subject']
        message =request.POST['message']
        contactfrom =contactIn(name=name,email=email,phone=phone,subject=subject,message=message)
        contactfrom.save()
        print("data saved")
        return redirect('/')
    return render(request,'contact.html')



def base(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request,'base.html',context)

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password) 

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            print("Invalid credentials")
            messages.info(request,"Invalid credentials")
            return redirect('login')

    else:
        return render(request,"login.html")
        
    

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        username = request.POST['mobile_number']
        email = request.POST['email']
       
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request,"Mobile number taken")
                    print('Username taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,email=email,first_name=first_name,password=password)
                    user.save()
                    messages.info(request,"User created")
                    print('User created')
                    return redirect('login')
        else:
            messages.info(request,"password not matching!!")
            return redirect('register')
        
    else:
        return render(request,"register.html")
    
def logout(request):
    auth.logout(request)
    return redirect('index')



def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    return render(request, 'single-product.html', context)


# cart/views.py


def add_to_cart(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        if request.user.is_authenticated:
            # Get or create a CartItem instance for the user and product
            cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
            if not created:
                cart_item.quantity += 1
                cart_item.save()
            return redirect('cart')
        else:
            # Redirect to the login page with a message
            messages.info(request, "You need to log in to add items to your cart.")
            return redirect('login')
        


def remove_from_cart(request, cart_item_id):
    # Fetch the cart item
    cart_item = get_object_or_404(CartItem, id=cart_item_id)

    # Check if the cart item belongs to the current user
    if cart_item.user == request.user:
        # Remove the cart item
        cart_item.delete()
    else:
        # Handle unauthorized access (optional)
        pass

    return redirect('cart')    





