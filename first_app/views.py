from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
from .models import Product
from .forms import ProductForm
 #Create your views here.



def index(request):
	return HttpResponse("hello world")


#dynamic URLS
def dynamic_lookup_view(request,my_id):
	#obj= Product.objects.get(id = my_id)
	obj = get_object_or_404(Product,id=my_id)
	context={
		"object":obj
	}
	return render(request, "first_app/first_app_details.html",context)


def product_list_view(request):
	queryset = Product.objects.all()
	context={
	'object_list' : queryset
	}
	return render(request,"first_app/first_app_list.html",context)






def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()
	context={
		'form':form
	}
	return render(request,"first_app/first_app_create.html",context)


def product_detail_view(request):
	obj = Product.objects.get(id=1)
	context = {
		"title":obj.title,
		"description":obj.description,
		"price":obj.price
	}
	context={
		'object':obj
	}
	return render(request,"first_app/first_app_details.html",context)