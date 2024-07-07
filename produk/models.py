from django.db import models

class Kategori(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Produk(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama

class Stok(models.Model):
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE)
    jumlah = models.IntegerField()

    def __str__(self):
        return f"Stok {self.produk.nama}"

class Order(models.Model):
    produk = models.ManyToManyField(Produk)
    total_harga = models.DecimalField(max_digits=10, decimal_places=2)
    waktu_pesan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pesanan #{self.id}"


