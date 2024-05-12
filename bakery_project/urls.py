"""
URL configuration for bakery_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path
from bakery.views import (
    IngredientListView, BakeryItemListView, BakeryItemDetailView,
    OrderListView, UserCreateView, ObtainTokenView
)

urlpatterns = [
    path('ingredients/', IngredientListView.as_view(), name='ingredient-list'),
    path('bakeryitems/', BakeryItemListView.as_view(), name='bakeryitem-list'),
    path('bakeryitems/<int:pk>/', BakeryItemDetailView.as_view(), name='bakeryitem-detail'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('register/', UserCreateView.as_view(), name='user-create'),
    path('token/', ObtainTokenView.as_view(), name='token-obtain'),
]
