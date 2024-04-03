from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import Expense
from .serializers import ExpenseSerializer


class ExpenseListCreate(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class BulkDeleteExpenseView(generics.GenericAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def delete(self, request, *args, **kwargs):
        ids = request.data.get("ids", [])
        if ids:
            self.queryset.filter(id__in=ids).delete()
            return Response(status=204)
        else:
            return Response({"detail": "No IDs provided for deletion."}, status=400)
