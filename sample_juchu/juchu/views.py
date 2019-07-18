from django.shortcuts import render
from django.http import HttpResponse
from .models import Order, Product

# Create your views here.
def index(request):
    latest_question_list = Product.objects.order_by('-name')[:5]
    output = ', '.join([q.name for q in latest_question_list])
    return HttpResponse(output)
    
def detail(request, order_id):
    return HttpResponse("You're looking at question %s." % order_id)

def results(request, order_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % order_id)

def order(request, order_id):
    return HttpResponse("You're voting on question %s." % order_id)
