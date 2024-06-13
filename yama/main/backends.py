from datetime import datetime
from pathlib import PurePath

from django.conf import settings
from django.contrib.auth import get_user_model

from .models import Report

User = get_user_model()


def generate_report(user: User) -> Report:
    debts = user.debts.all()
    file_name = PurePath(f'report_{user.id}_{str(datetime.timestamp(datetime.now())).replace('.', '_')}.txt')

    report = f'### DEBTS REPORT FOR {user.username} ###\n' \
             f'# Date created: {datetime.now()}\n' \
             f'# Total debts: {len(debts)}\n' \
             f'# Total amount: {sum(debt.amount for debt in debts)}\n' \
             f'##########\n\n'

    if debts:
        report += f'## Debts ##\n\n'
        for debt in debts:
            report += f'# Creditor: {debt.creditor}\n' \
                      f'# Debtor: {debt.debtor}\n' \
                      f'# Amount: {debt.amount}\n' \
                      f'# Description: {debt.description}\n' \
                      f'# Date created: {debt.date_created}\n' \
                      f'# Date due: {debt.date_due}\n' \
                      f'# Interest rate: {debt.interest_rate}\n\n'
    else:
        report += f'## No debts ##\n'

    with open(settings.REPORTS_DIR / file_name, 'x') as file:
        file.write(report)

    return Report.objects.create(user=user, file_name=file_name)
