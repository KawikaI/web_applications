from django.urls import path

from .views import ProductsPageView, home_page_view, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', home_page_view, name='home'),
    path('products/', ProductsPageView.as_view(), name='products'),
]