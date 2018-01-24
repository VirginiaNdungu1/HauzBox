from .models import *
from django.forms import ModelForm

class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ['tenant_name', 'month', 'transaction_id', 'amount', 'property_id']
