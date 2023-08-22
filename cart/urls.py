from django.urls import path
from cart import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
path('',views.index,name='index'),
path('about',views.about,name='about'),
path('contact',views.contact,name='contact'),
path('register',views.register,name='register'),
path("login",views.login,name="login"),
path("logout",views.logout,name="logout"),
path("userprofile",views.userprofile,name="userprofile"),
path("cart",views.cart,name="cart"),
path("<int:id>",views.product_detail,name="product_detail"),
path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),


# path("createvchargingslot",views.createvchargingslot,name="createvchargingslot"),
# path("creatparkingslot",views.creatparkingslot,name="creatparkingslot"),
# path("evcharging",views.evcharging,name="evcharging"),
# path("parking",views.parking,name="parking"),
# path("checkout",views.checkout,name="checkout"),
# path("booking-success",views.bookingSuccess,name="bookingSuccess")

path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
 
path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
 
path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
 
path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)