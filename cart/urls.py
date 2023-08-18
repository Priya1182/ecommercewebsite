from django.urls import path
from cart import views

urlpatterns = [
path('',views.index,name='index'),
path('about',views.about,name='about'),
path('contact',views.contact,name='contact'),
# path('register',views.register,name='register'),
# path("logout",views.logout,name="logout"),
# path("createvchargingslot",views.createvchargingslot,name="createvchargingslot"),
# path("creatparkingslot",views.creatparkingslot,name="creatparkingslot"),
# path("evcharging",views.evcharging,name="evcharging"),
# path("parking",views.parking,name="parking"),
# path("checkout",views.checkout,name="checkout"),
# path("booking-success",views.bookingSuccess,name="bookingSuccess")
]