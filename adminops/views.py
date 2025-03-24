from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import render
from django.db.models import Sum
from .models import Expense, Revenue, Budget, Category, Tag, Attachment, FinancialReport
from .serializers import (
    ExpenseSerializer,
    RevenueSerializer,
    BudgetSerializer,
    CategorySerializer,
    TagSerializer,
    AttachmentSerializer,
    FinancialReportSerializer,
)
from .utils import generate_profit_loss_report


# ViewSets for API endpoints
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    @action(detail=False, methods=['get'])
    def total_expenses(self, request):
        total = self.queryset.aggregate(total=Sum('amount'))['total'] or 0
        return Response({'total_expenses': total})


class RevenueViewSet(viewsets.ModelViewSet):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializer

    @action(detail=False, methods=['get'])
    def total_revenue(self, request):
        total = self.queryset.aggregate(total=Sum('amount'))['total'] or 0
        return Response({'total_revenue': total})


class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    @action(detail=False, methods=['get'])
    def remaining_budgets(self, request):
        budgets = self.queryset.annotate(remaining_budget=Sum('amount') - Sum('spent_amount'))
        data = [{'department': budget.department, 'remaining_budget': budget.remaining_budget} for budget in budgets]
        return Response(data)


class FinancialReportViewSet(viewsets.ModelViewSet):
    queryset = FinancialReport.objects.all()
    serializer_class = FinancialReportSerializer


# Dashboard view
def financial_dashboard(request):
    # Calculate total revenue, expenses, and net profit
    total_revenue = Revenue.objects.aggregate(total=Sum('amount'))['total'] or 0
    total_expenses = Expense.objects.aggregate(total=Sum('amount'))['total'] or 0
    net_profit = total_revenue - total_expenses

    # Calculate remaining budgets for each department
    budgets = Budget.objects.annotate(remaining_budget=Sum('amount') - Sum('spent_amount'))

    # Prepare context data for the template
    context = {
        'total_revenue': total_revenue,
        'total_expenses': total_expenses,
        'net_profit': net_profit,
        'budgets': budgets,
    }

    # Render the dashboard template with the context data
    return render(request, 'adminops/dashboard.html', context)
