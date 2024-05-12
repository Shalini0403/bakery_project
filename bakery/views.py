from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Ingredient, BakeryItem, Order, CustomUser
from .serializers import IngredientSerializer, BakeryItemSerializer, OrderSerializer, UserSerializer


class IngredientListView(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class BakeryItemListView(generics.ListCreateAPIView):
    queryset = BakeryItem.objects.all()
    serializer_class = BakeryItemSerializer


class BakeryItemDetailView(generics.RetrieveAPIView):
    queryset = BakeryItem.objects.all()
    serializer_class = BakeryItemSerializer


class OrderListView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class ObtainTokenView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
