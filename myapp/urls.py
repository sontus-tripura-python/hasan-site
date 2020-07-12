from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home_page, name='Home_page'),
    path('contact', views.contact, name='contact'),
     path('portfolio/<slug:category_slug>/', views.Home_page, name='portfolio_list_by_category'),
]
