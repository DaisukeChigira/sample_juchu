from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:product_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:product_id>/results/', views.results, name='results'),
    # ex: /polls/5/order/
    path('<int:product_id>/product/', views.order, name='product'),
]
