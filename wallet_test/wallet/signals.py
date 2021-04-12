from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Transaction


@receiver(post_save, sender=Transaction)
def update_balance(sender, instance, created, **kwargs):
    if created:
        if instance.type == '+':
            instance.wallet.balance += instance.amount
            instance.wallet.save()
        elif instance.type == '-':
            instance.wallet.balance -= instance.amount
            instance.wallet.save()
