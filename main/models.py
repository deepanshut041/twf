from django.db import models
from django.contrib.auth import get_user_model

class CenterModel(models.Model):
    name = models.CharField(max_length=50, null=False)
    details = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=130, null=True, blank=True)

    def __str__(self):
        return str(self.name)

class CenterDistanceModel(models.Model):
    center_1 = models.ForeignKey(CenterModel, on_delete=models.CASCADE, null=True, blank=True, related_name="c1")
    center_2 = models.ForeignKey(CenterModel, on_delete=models.CASCADE, null=True, blank=True, related_name="c2")
    distance = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.center_1) + " - " + str(self.center_2)

class ProductModel(models.Model):
    center = models.ForeignKey(CenterModel, on_delete=models.CASCADE, related_name="products", null=False)
    name = models.CharField(max_length=130, null=False)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.name)

class LoadModel(models.Model):
    name = models.CharField(max_length=130, null=True, blank=True)
    address = models.CharField(max_length=130, null=True, blank=True)

    def __str__(self):
        return str(self.name)

class LoadDistanceModel(models.Model):
    center = models.ForeignKey(CenterModel, on_delete=models.CASCADE, null=True, blank=True)
    load = models.ForeignKey(LoadModel, on_delete=models.CASCADE, null=True, blank=True)
    distance = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.center) + " - " + str(self.load)

class OrderModel(models.Model):
    load = models.ForeignKey(LoadModel, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(null=True, default=0)
    is_dilivered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.product) + " - " + str(self.load)