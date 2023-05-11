from django.db.models import Count, Sum

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Sale
from .utils import generate_pdf
from .serializers import SaleSerializer


class InsertSale(generics.CreateAPIView):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()


class RetriveUpdateDeleteSale(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()


class GenertePdfReport(APIView):
    permission_classes = ()

    def get(self, *args, **kwargs):
        customers = Sale.objects.values("customer_name").distinct()
        orders_count_per_year = Sale.objects.values("order_date__year").annotate(Count("id"))
        top_three_customers = Sale.objects.values("customer_name", "customer_id").annotate(Sum('sales')).order_by('-sales')[:3]
        sales_by_region = Sale.objects.values("region").annotate(Count("id"))
        sales_by_year = Sale.objects.values("order_date__year").annotate(Count("id"))
        customer_transactions_per_year = Sale.objects.values("order_date__year").annotate(Sum("sales"))
        context = {
            "orders_count_per_year": orders_count_per_year,
            "total_customers": customers.count(),
            "top_three_customers": top_three_customers,
            "customer_transactions_per_year": customer_transactions_per_year,
            "region_sales": sales_by_region,
            "year_sales": sales_by_year
        }
        pdf = generate_pdf(self.request, context)
        return pdf

    