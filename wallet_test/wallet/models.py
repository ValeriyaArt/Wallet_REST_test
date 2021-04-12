from django.db import models


class Wallet(models.Model):
    """
    Модель для кошелька
    """
    title = models.CharField(max_length=150, verbose_name='Название кошелька')
    balance = models.FloatField(verbose_name='Текущий баланс в рублях')

    class Meta:
        verbose_name = 'Кошелек'
        verbose_name_plural = 'Кошельки'

    def __str__(self):
        return self.title


class Transaction(models.Model):
    """
    Модель для транзакции
    """
    wallet = models.ForeignKey('Wallet', on_delete=models.CASCADE, verbose_name='Кошелек', related_name='transactions')
    amount = models.FloatField(verbose_name='Сумма транзакции')
    TransactionChoices = [
        ('-', 'Списание'),
        ('+', 'Пополнение')
    ]
    type = models.CharField(max_length=10, choices=TransactionChoices, verbose_name='Тип транзакции',)
    date = models.DateField(verbose_name='Дата проведения транзакции')
    comment = models.TextField(verbose_name='Комментарий пользователя')

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
