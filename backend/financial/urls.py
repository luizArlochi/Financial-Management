from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet
from .views import BulkDeleteExpenseView

router = DefaultRouter()
router.register(r"expenses", ExpenseViewSet, basename="expenses")
path(
    "expenses/bulk-delete/", BulkDeleteExpenseView.as_view(), name="bulk-delete-expense"
),

urlpatterns = [
    path("", include(router.urls)),
]
