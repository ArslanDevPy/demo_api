from django.db.models import Count
from rest_framework import generics, response
from django_filters.rest_framework import DjangoFilterBackend
from api import serializers, models
from core.mixins import pagination_mixins, email


class SupplierListAPIView(generics.ListAPIView):
    queryset = models.SupplierModel.objects.all()
    serializer_class = serializers.SupplierSerializers
    filter_backends = [DjangoFilterBackend]
    pagination_class = pagination_mixins.CustomPaginationBY3
    filterset_fields = ['name', 'shop__name', 'shop__id', 'address']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.annotate(num_shop=Count('shop')).order_by('-num_shop')


class ReportsOfSupplierAPIView(generics.GenericAPIView):
    http_method_names = ['post']
    serializer_class = serializers.ReportsOfSupplierSerializers

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            context = {
                'title': "Supplier Report",
                'object_list': models.SupplierModel.objects.annotate(num_shop=Count('shop')).order_by('-num_shop')
            }
            email.Email(title="Supplier Report", template_name="api/supplier_info.html",
                        email=serializer.validated_data['email'], _dict=context).start()
            return response.Response("Email send successfully.")
        return response.Response("Error")
