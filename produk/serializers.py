from rest_framework import serializers
from .models import Kategori, Produk, Stok, Order

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = '__all__'

class StokSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stok
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    produk = ProdukSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


