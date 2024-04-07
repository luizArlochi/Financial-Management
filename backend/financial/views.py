from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import Month, Label, Transaction, Earning
from .serializers import (
    MonthSerializer,
    LabelSerializer,
    TransactionSerializer,
    EarningSerializer,
)


class MonthList(generics.ListCreateAPIView):
    queryset = Month.objects.all()
    serializer_class = MonthSerializer


class MonthViewSet(viewsets.ModelViewSet):
    queryset = Month.objects.all()
    serializer_class = MonthSerializer


class MonthDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Month.objects.all()
    serializer_class = MonthSerializer


class LabelList(generics.ListCreateAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class LabelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class EarningList(generics.ListCreateAPIView):
    queryset = Earning.objects.all()
    serializer_class = EarningSerializer


class EarningViewSet(viewsets.ModelViewSet):
    queryset = Earning.objects.all()
    serializer_class = EarningSerializer


class EarningDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Earning.objects.all()
    serializer_class = EarningSerializer


class MonthTotalExpenses(generics.RetrieveAPIView):
    queryset = Month.objects.all()
    serializer_class = MonthSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        total_expenses = instance.total_expenses()
        return Response({"total_expenses": total_expenses})


class MonthRemainingBalance(generics.RetrieveAPIView):
    queryset = Month.objects.all()
    serializer_class = MonthSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        remaining_balance = instance.remaining_balance()
        return Response({"remaining_balance": remaining_balance})
