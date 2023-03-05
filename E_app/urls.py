from django.urls import path
from . import views


urlpatterns = [
    path("", views.ProductView.as_view(), name = 'home'),
    # path("about/", views.about, name = 'about'),
    path("signup_page/", views.signup_page, name = "signup_page"),
    path('signin_page/',views.signin_page,name = "signin_page"),
    path('signout_page/', views.signout_page, name = "signout_page"),


    path("profile_page/", views.profile_page, name = "profile_page"),
    path('profile_update/', views.profile_update, name = "profile_update"),


    path('signup/', views.signup, name = "signup"),
    path('signin/', views.signin, name = "signin"),


    path('product_item/<int:pk>', views.ProductItemView.as_view(), name = "product_item"),
    path('product_list/', views.product_list, name = "product_list"),

    path('product_list/<slug:data>', views.ProductListView.as_view(), name= 'product_list'),

    path('otp_page/', views.otp_page, name = "otp_page"),
    path('verify_otp/', views.verify_otp, name = "verify_otp"),

    
    path('add_to_cart/', views.CustomerCartProduct.as_view(), name='add_to_cart'),

    path('show_cart', views.show_cart, name = 'show_cart'),

    path('checkout', views.checkout, name = "checkout"),

]