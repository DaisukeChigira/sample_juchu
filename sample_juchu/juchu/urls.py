from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:order_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:order_id>/results/', views.results, name='results'),
    # ex: /polls/5/order/
    path('<int:order_id>/order/', views.order, name='order'),
]
