from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Product, Category
from .forms import RegistrationForm

# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'home.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in"))
            return redirect('home')
        else:
            messages.success(request, ("There is something wrong. Try again"))
            return redirect('login')
    else:
        context = {}
        return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, ("You are logged out"))
    return redirect('home')

def register_user(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}')
            return redirect('login')
        else:
            messages.success(request, ("There is something wrong"))
            return redirect('register')
    else:
        context = {
            'form': form
        }
        return render(request, 'register.html', context)
    
def product(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product
    }
    return render(request, 'product.html', context)

def category(request, foo):
    foo = foo.replace('-', ' ')
    
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return redirect(request, 'category.html', {'products': products, 'category': category})
    except:
        messages.success(request, ("Category does not exist"))
        return redirect('home')