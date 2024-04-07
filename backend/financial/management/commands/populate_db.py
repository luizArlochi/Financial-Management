from django.core.management.base import BaseCommand
from financial.models import Month


class Command(BaseCommand):
    help = "Populate the database with initial data"

    def handle(self, *args, **kwargs):
        # Coloque sua lógica de preenchimento do banco de dados aqui
        for month_number, month_name in Month.MONTH_CHOICES:
            Month.objects.get_or_create(month=month_number)
