"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from products import urls as urls_products
from products import urls as urls_users
from products import urls as urls_orders
from products import urls as urls_cart
from products.views import root_index


urlpatterns = [
    path('', root_index, name='root_index'),
    path('market/', include(urls_products)),
    path('users/', include(urls_users)),
    path('orders/', include(urls_orders)),
    path('cart/', include(urls_cart)),

]

