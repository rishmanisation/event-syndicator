from django.shortcuts import render, render_to_response
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, FormView
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, get_user_model, login, logout

from .models import Product
from .forms import AddProductForm

# Create your views here.
class ProductFormView(View):
    
    form_class = AddProductForm
    template_name = 'event_synd/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {
            'form': form 
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            clean = form.cleaned_data
            prodname = clean['name']
            description = clean['description']
            price = clean['price']
            
            product_object, created = Product.objects.get_or_create(
                product_name = prodname,
                product_description = description,
                product_price = price,
            )

            if created:
                try:
                    product_object.save()
                except Exception as e:
                    return HttpResponseRedirect(reverse('index'))
            else:
                product_object.is_syndicated = False
                product_object.save()
            
            return HttpResponseRedirect(reverse('index'))

class ObjectsView(View):

    template_name = 'event_synd/objects.html'

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, self.template_name, context)

