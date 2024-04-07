from django.contrib import admin
from .models import Month, Label, Transaction, Earning

admin.site.register(Month)
admin.site.register(Label)
admin.site.register(Transaction)
admin.site.register(Earning)
