import csv

from django.core.management import BaseCommand

from sales.models import Sale


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Inserting data.....")
        file = open('sales/management/commands/xyz_sales_data.csv', 'r')
        columns = (
            "id",
            "order_id",
            "order_date",
            "ship_date",
            "ship_mode",
            "customer_id",
            "customer_name",
            "segment",
            "country",
            "city",
            "state",
            "postal_code",
            "region",
            "product_id",
            "category",
            "sub_category",
            "product_name",
            "sales"
        )
        data = csv.DictReader(file, fieldnames=columns)
        header = next(data)
        i = 0
        for row in data:
            Sale.objects.create(**row)
            i += 1
        print(f"Total {i} record inserted")

        

