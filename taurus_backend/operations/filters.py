from django_filters import rest_framework as filters

from operations.models import Order


class OrderFilter(filters.FilterSet):

    start_date = filters.DateFilter()
    end_date = filters.DateFilter()

    class Meta:
        model = Order
        fields = ( "delivery_date", )

