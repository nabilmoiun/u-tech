from django.db import models


class Sale(models.Model):
    order_id = models.CharField(max_length=150)
    order_date = models.DateField()
    ship_date = models.DateField()
    ship_mode = models.CharField(max_length=50)
    customer_id = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=150)
    segment = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    region = models.CharField(max_length=50)
    product_id = models.CharField(max_length=50)
    category = models.CharField(max_length=150)
    sub_category = models.CharField(max_length=150)
    product_name = models.CharField(max_length=500)
    sales = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.order_id
