from django.urls import path
from .views import WalletViewSet, TransactionViewSet


urlpatterns = [
    path('api/wallet', WalletViewSet.as_view({'get': 'list'}), name='Wallets-list'),
    path('api/wallet/create', WalletViewSet.as_view({'post': 'create'}), name='Wallet-create'),
    path('api/wallet/<int:pk>/update', WalletViewSet.as_view({'post': 'update'}), name='Wallet-update'),
    path('api/wallet/<int:pk>/delete', WalletViewSet.as_view({'delete': 'destroy'}), name='Wallet-delete'),
    path('api/wallet/<int:pk>', WalletViewSet.as_view({'get': 'retrieve'}), name='Wallet-item'),
    path('api/wallet/transaction', TransactionViewSet.as_view({'get': 'list'}), name='Transactions-list'),
    path('api/wallet/transaction/<int:pk>', TransactionViewSet.as_view({'get': 'retrieve'}), name='Transaction-item'),
    path('api/wallet/transaction/create', TransactionViewSet.as_view({'post': 'create'}), name='Transaction-create'),
    path('api/wallet/transaction/<int:pk>/delete', TransactionViewSet.as_view({'delete': 'destroy'}), name='Transaction-delete'),
]
