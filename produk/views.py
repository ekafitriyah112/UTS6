from rest_framework import viewsets
from .models import Kategori, Produk, Stok, Order
from .serializers import KategoriSerializer, ProdukSerializer, StokSerializer, OrderSerializer

class KategoriViewSet(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer

class ProdukViewSet(viewsets.ModelViewSet):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer

class StokViewSet(viewsets.ModelViewSet):
    queryset = Stok.objects.all()
    serializer_class = StokSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


