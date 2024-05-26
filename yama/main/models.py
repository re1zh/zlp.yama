from django.db import models
from django.contrib.auth.models import User


class Debt(models.Model):
    creditor = models.CharField(max_length=100)
    debtor = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_due = models.DateTimeField()

    def __str__(self):
        return f'{self.debtor} owes {self.amount} to {self.creditor}'
