from rest_framework import serializers
from .models import Wallet, Transaction


class TransactionSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Транзакция
    """
    wallet = serializers.SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = Transaction
        fields = '__all__'


class TransactionCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Транзакция
    """

    class Meta:
        model = Transaction
        fields = '__all__'


class WalletSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Кошелек
    """
    transactions = TransactionSerializer(many=True)

    class Meta:
        model = Wallet
        fields = '__all__'


class WalletCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания нового объекта модели Кошелек
    """
    class Meta:
        model = Wallet
        fields = '__all__'


class WalletUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для изменения объекта модели Кошелек
    """
    class Meta:
        model = Wallet
        fields = ['title']
