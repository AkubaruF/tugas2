from django.shortcuts import render

# TODO: Create your views here.
from katalog.models import CatalogItem

def index(request):
    barang_katalog = CatalogItem.objects.all()
    response = {'barang_katalog' : barang_katalog}
    return render(request, 'katalog.html', response)