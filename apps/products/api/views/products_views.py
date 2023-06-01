from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.product_serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = ProductSerializer.Meta.model.objects.filter(state=True)

    def post(self, request):
        product_serializer = self.get_serializer(data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response({'message': 'Producto creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(state=True)

    def patch(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product_serializer = self.serializer_class(product)
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'No hay un producto con ese id'})

    def put(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product_serializer = self.serializer_class(
                product, data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'No hay un producto con ese id'})

    def delete(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message': 'Producto eliminado correctamente'}, status=status.HTTP_200_OK)
        return Response({'message': 'No existe un producto con este id'})
