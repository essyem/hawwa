from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    TagViewSet,
    AttachmentViewSet,
    ExpenseViewSet,
    RevenueViewSet,
    BudgetViewSet,
    FinancialReportViewSet,  # Add this import
    financial_dashboard,
)

# Create a router for API endpoints
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'attachments', AttachmentViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'revenues', RevenueViewSet)
router.register(r'budgets', BudgetViewSet)
router.register(r'financial-reports', FinancialReportViewSet)  # Add this line

urlpatterns = [
    path('', include(router.urls)),  # API endpoints
    path('dashboard/', financial_dashboard, name='financial_dashboard'),  # Dashboard route
]
