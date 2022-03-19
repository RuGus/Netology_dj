from django.shortcuts import render, redirect
from phones.models import Phone



def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get("sort")
    if not sort:
        phone_objects = Phone.objects.all()
    elif sort == "name":
        phone_objects = Phone.objects.order_by("name")
    elif sort == "min_price":
        phone_objects = Phone.objects.order_by("price")
    elif sort == "max_price":
        phone_objects = Phone.objects.order_by("-price")
    
    context = {"phones":phone_objects}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.get(slug = slug)
    context = {"phone":phone_object}
    return render(request, template, context)
