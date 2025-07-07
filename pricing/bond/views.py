from django.shortcuts import render
from .forms import BondFutureForm
from .utils import calculate_bond_future

def bond_future_view(request):
    result = None
    if request.method == 'POST':
        form = BondFutureForm(request.POST)
        if form.is_valid():
            bond_price = form.cleaned_data['bond_price']
            interest_rate = form.cleaned_data['interest_rate']
            maturity_years = form.cleaned_data['maturity_years']
            accrued_interest_start = form.cleaned_data['accrued_interest_start']
            accrued_interest_delivery = form.cleaned_data['accrued_interest_delivery']
            conversion_factor = form.cleaned_data['conversion_factor']
            result = calculate_bond_future(bond_price, interest_rate, maturity_years, accrued_interest_start,
                                           accrued_interest_delivery, conversion_factor)
    else:
        form = BondFutureForm()
    return render(request, 'pricing/bond_future.html', {'form': form, 'result': result})