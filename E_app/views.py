# from tempfile import TemporaryFile
from random import randint
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from django.views import View
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
default_data = {
    'hello': "World",
    }

# def index(request):
#     return render(request, 'index.html', default_data)

def signup_page(request):
    return render(request, 'signup_page.html')
 
def signin_page(request):
    return render(request, 'signin_page.html')

def otp_page(request):
    return render(request, 'otp_page.html')


# Profile management

def profile_page(request):
    if 'email' in request.session:
        profile_data(request)
        return render(request, 'profile_page.html', default_data)
    return redirect('signin_page')

def profile_data(request):
    master = Master.objects.get(Email=request.session['email'])
    profile = Profile.objects.get(Master = master)

    # sd  = serialize_data(profile)
    # print('serialize_data :' , sd)

    print(gender_choices)
    gender = []
    for gc in gender_choices:
        gender.append({
            'small_txt': gc[0],
            'txt': gc[1]
        })

    print(gender)

    default_data['profile_data'] = profile
    default_data['gender_choices'] = gender


def profile_update(request):
    master = Master.objects.get(Email = request.session['email'])
    profile = Profile.objects.get(Master = master)
     
    profile.Email = request.POST['email']
    profile.Fullname = request.POST['full_name']
    profile.Gender = request.POST['gender']
    profile.Mobile = request.POST['mobile']
    profile.State = request.POST['state']
    profile.City = request.POST['city']
    profile.Address = request.POST['address']

    profile.save()

    return redirect('profile_page')
    # profile_data(request)
    # return JsonResponse(default_data)


# def serialize_data(obj):
#     object = {}
#     source_dict = obj.__dict__
#     for o in source_dict:
#         if o.startswith('_') or o.endswith('_') or (o.startswith('_') and o.endswith('_')):
#             # object.pop(o) 
#             continue    
#         object.setdefault(o, source_dict[o])
#     # print(object)
#     return object



# OTP Verification

def create_otp(request):
    email_to_list = [request.session['reg_data'] ['email']]

    from_email = settings.EMAIL_HOST_USER
    otp = randint(1000, 9999)
    request.session['otp'] = otp

    subject = 'OTP VERIFICATION'
    message = f"Hey Sanket here! Your otp verification code is : {otp}"

    send_mail(subject,message, from_email, email_to_list)


def verify_otp(request):
    if request.method == 'POST':
        otp = int(request.POST['otp'])

        if otp == request.session['otp']:
            master = Master.objects.create(
                Email = request.session['reg_data']['email'],
                Password = request.session['reg_data']['password'],
                isActive = True
            )
            Profile.objects.create(Master = master)
            del request.session['otp']
            del request.session['reg_data']
            return redirect('signin_page')
        else:
            print('invalid otp')
            return redirect('otp_page')

    else:
        print('invalid method')
        return redirect('otp_page')

# Authentication Functionality

def signup(request):
    print("signup data", request.POST)
    request.session['reg_data'] = {
        'email': request.POST['email'],
        'password': request.POST['pwd'],
    }
    create_otp(request)
    return redirect('otp_page')


def signin(request):
    if request.method == 'POST':
        master = Master.objects.get(Email=request.POST['email'])

        if master.Password == request.POST['pwd']:
            request.session['email'] = master.Email
            # request.session['password'] = password
            return redirect('profile_page')
        else:
            print('incorrect password')
            return redirect('signin_page')
    else:
        return render(request, 'signin_page.html')
  

def signout_page(request):
    if 'email' in  request.session:
        del request.session['email']
    return redirect('signin_page')
    
    

# Category wise Distribution

class ProductView(View):
    def get(self, request):
        mobiles = Product.objects.filter(Category='M')
        laptops = Product.objects.filter(Category='L')
        headphones = Product.objects.filter(Category='Hp')
        keyboards = Product.objects.filter(Category='Kb')
        mouse = Product.objects.filter(Category = 'Mo')
        return render(request, 'index.html', {'mobiles': mobiles, 'laptops': laptops, 'headphones':  headphones, 'keyboards': keyboards, 'mouse':mouse})



class ProductItemView(View):
    def get(self, request ,pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'product_item.html', {'product': product})



def product_list(request):
    return render(request, 'product_list.html')

# Product listing view

class ProductListView(View):
    def get(self, request, data ):
        if data == 'all':
            all_prod = Product.objects.all()
        elif data == 'mobiles':
            all_prod = Product.objects.filter(Category = 'M')
        elif data == 'laptops':
            all_prod = Product.objects.filter(Category = 'L')
        elif data == 'headphones':  
            all_prod = Product.objects.filter(Category = 'Hp')
            
        return render(request, 'product_list.html', {'all_prod': all_prod})
        



# Add To cart
# class CartProductList:
#     def add_to_cart(request, pk):
#         master = Master.objects.get(Email= request.session['email'])
#         if master.IsActive():
#             prikey = Product.objects.get(pk = pk)

#         return render(request, 'cart.html',{'prikey' : prikey})



def add_to_cart(request):    

    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id = product_id)
    OrderItem( product =  product).save()
    print(product_id)
    return render(request, 'cart.html')
