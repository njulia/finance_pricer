from django import forms

class InterestRateSwapForm(forms.Form):
    notional = forms.FloatField(label='Notional Amount')
    fixed_rate = forms.FloatField(label='Fixed Rate (%)')
    floating_rate = forms.FloatField(label='Floating Rate (%)')
    term_years = forms.FloatField(label='Term (Years)')