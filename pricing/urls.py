from django.contrib import admin
from django.urls import path
from pricing import views

urlpatterns = [
    path("", views.index, name='index'),
    path("home", views.index, name='index'),
    path('about/', views.about, name='about'),
    path('pricing-structure/', views.pricing_structure, name='pricing_structure'),
    path('api/organizations/', views.get_organizations, name='api_organizations'),
    path('api/item-types/', views.get_item_types, name='get_item_types'),
]