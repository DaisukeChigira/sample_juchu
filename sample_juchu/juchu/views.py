from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Order, Product

# Create your views here.
def index(request):
    latest_question_list = Product.objects.order_by('-name')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'juchu/index.html', context)
    
def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'juchu/detail.html', {'product': product})

def results(request, product_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % product_id)

def order(request, product_id):
    return HttpResponse("You're voting on question %s." % product_id)
