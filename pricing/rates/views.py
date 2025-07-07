from django.shortcuts import render
from .forms import InterestRateSwapForm
from .utils import calculate_interest_rate_swap

def interest_rate_swap_view(request):
    result = None
    if request.method == 'POST':
        form = InterestRateSwapForm(request.POST)
        if form.is_valid():
            notional = form.cleaned_data['notional']
            fixed_rate = form.cleaned_data['fixed_rate']
            floating_rate = form.cleaned_data['floating_rate']
            term_years = form.cleaned_data['term_years']
            result = calculate_interest_rate_swap(notional, fixed_rate, floating_rate, term_years)
    else:
        form = InterestRateSwapForm()
    return render(request, 'pricing/interest_rate_swap.html', {'form': form, 'result': result})