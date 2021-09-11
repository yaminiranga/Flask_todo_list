from django.shortcuts import render
from .models import Destination


def index(request):
    # return HttpResponse("<h1>Hello World!!</h1>")

    # dest1 = Destination()
    # dest2 = Destination()
    # dest3 = Destination()
    #
    # dest1.name = 'Taiyaki'
    # dest1.sub_name = 'Vegan'
    # dest1.details = 'what a place to visit'
    # dest1.img = 'big_portfolio_item_1.png'
    # dest1.offer = True
    #
    # dest2.name = 'Taiyaki'
    # dest2.sub_name = 'Vegan'
    # dest2.details = 'what a place to visit'
    # dest2.img = 'big_portfolio_item_2.png'
    # dest2.offer = True
    #
    # dest3.name = 'Taiyaki'
    # dest3.sub_name = 'Vegan'
    # dest3.details = 'what a place to visit'
    # dest3.img = 'big_portfolio_item_3.png'
    # dest3.offer = False
    # dests = [dest1, dest2, dest3]
    dests = Destination.objects.all()

    return render(request, 'index.html', {'dests': dests})
