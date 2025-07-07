from django import forms

class BondFutureForm(forms.Form):
    bond_price = forms.FloatField(label='Bond Price')
    interest_rate = forms.FloatField(label='Interest Rate (%)')
    maturity_years = forms.FloatField(label='Maturity (Years)')
