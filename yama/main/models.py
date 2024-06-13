from django.contrib.auth.models import User
from django.db import models


class Debt(models.Model):
    creditor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='debts')
    debtor = models.TextField()
    is_confirmed = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_due = models.DateField()
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.debtor} owes {self.amount} to {self.creditor}'
