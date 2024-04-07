from django.db import models


class Month(models.Model):
    MONTH_CHOICES = [
        (1, "Janeiro"),
        (2, "Fevereiro"),
        (3, "Março"),
        (4, "Abril"),
        (5, "Maio"),
        (6, "Junho"),
        (7, "Julho"),
        (8, "Agosto"),
        (9, "Setembro"),
        (10, "Outubro"),
        (11, "Novembro"),
        (12, "Dezembro"),
    ]

    month = models.IntegerField(choices=MONTH_CHOICES, unique=True)

    def __str__(self):
        return self.get_month_display()

    def total_expenses(self):
        # Calcula o total de gastos para este mês
        transactions = Transaction.objects.filter(month=self)
        total = sum(transaction.amount for transaction in transactions)
        return total

    def remaining_balance(self):
        # Calcula o saldo restante após os gastos para este mês
        earnings = Earning.objects.filter(month=self)
        total_earnings = sum(earning.amount for earning in earnings)
        total_expenses = self.total_expenses()
        remaining_balance = total_earnings - total_expenses
        return remaining_balance


class Label(models.Model):
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=50)
    color = models.CharField(max_length=7)  # Exemplo: "#RRGGBB"

    def __str__(self):
        return self.name


class Transaction(models.Model):
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class Earning(models.Model):
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.amount)
