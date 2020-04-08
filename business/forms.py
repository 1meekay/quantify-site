from django import forms
from .models import BusinessInfo

class BusinessForm(forms.ModelForm):
    class Meta:
        model = BusinessInfo
        fields = ['businessName', 'location', 'industry', 'totalRevenue', 'totalRevenue', 'priorRevenue', 'costOfGoodsSold', 'operatingExpenses', 'cashBalance', 'currentAssets', 'currentLiabilities', 'longTermLiabilities', 'ownerSatisfaction', 'employeeSatisfaction', 'newCustomers', 'startCustomers', 'endCustomers', 'rewardsProgram', 'totalInventory', 'deadInventory', 'expansion']
        widgets = {
            'ownerSatisfaction': forms.TextInput(
                attrs={'placeholder': '1 to 11'}
            ),
            'employeeSatisfaction': forms.TextInput(
                attrs={'placeholder': '1 to 11'}
            ),
        }