from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Wallet, Transaction
from .serializers import TransactionSerializer, TransactionCreateSerializer, WalletSerializer, WalletCreateSerializer, \
    WalletUpdateSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    """
    Контроллер для модели Транзакция
    """
    queryset = Transaction.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['type', 'date', 'wallet__title']
    ordering_fields = ['wallet__title', 'amount']

    def get_serializer_class(self):
        if self.action == 'create':
            return TransactionCreateSerializer
        else:
            TransactionSerializer


class WalletViewSet(viewsets.ModelViewSet):
    """
    Контроллер для модели Кошелек
    """
    queryset = Wallet.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['title', 'balance']
    search_fields = ['title', 'balance']

    def get_serializer_class(self):
        if self.action == 'create':
            return WalletCreateSerializer
        elif self.action == 'update':
            return WalletUpdateSerializer
        else:
            return WalletSerializer

