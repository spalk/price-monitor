from django.urls import path
from .views import main
from .views import ProductView

urlpatterns = [
    path('test', main),
    path('products', ProductView.as_view()),
]