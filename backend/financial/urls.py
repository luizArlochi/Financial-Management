from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    # ExpenseViewSet,
    EarningViewSet,
    MonthViewSet,
    LabelViewSet,
    TransactionViewSet,
)

router = DefaultRouter()
# router.register(r"expenses", ExpenseViewSet, basename="expenses")
router.register(r"earnings", EarningViewSet, basename="earnings")
router.register(r"months", MonthViewSet, basename="months")
router.register(r"labels", LabelViewSet, basename="labels")
router.register(r"transactions", TransactionViewSet, basename="transactions")

urlpatterns = [
    path("", include(router.urls)),
]
