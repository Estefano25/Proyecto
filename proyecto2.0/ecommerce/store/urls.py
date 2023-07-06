from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('ubication', views.Ubication, name='ubication'),
    path('Nosotros/', views.Nosotros, name='Nosotros'),
	path('login/', views.LoginPage, name='login'),
    path('logout/', views.logout_view, name='logout'),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path('signup1/', views.registerpage, name='signup1')

]