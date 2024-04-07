from rest_framework import serializers
from .models import Month, Label, Transaction, Earning


class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Month
        fields = "__all__"


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


class EarningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Earning
        fields = "__all__"
