from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def home_page_view(request):
    context = {
        'inventory_list': ['Widget 1', 'Widget 2', 'Widget 3'],
        'greeting': 'THank you FOR visitING.'
    }
    return render(request, 'home.html', context)

class AboutPageView(TemplateView):
    template_name = 'about.html'

    def get_context_date(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_address'] = '123 Main Street'
        context['phone_number'] = '555-555-555'
        return context
    


#from django.views.generic import TemplateView

class ProductsPageView(TemplateView):
    template_name = 'products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = [
            {'name': 'Product 1', 'description': 'Description of product 1', 'price': 10.99},
            {'name': 'Product 2', 'description': 'Description of product 2', 'price': 12.99},
            {'name': 'Product 3', 'description': 'Description of product 3', 'price': 9.99},
            {'name': 'Product 4', 'description': 'Description of product 4', 'price': 15.99},
        ]
        return context