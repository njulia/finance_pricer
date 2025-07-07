from django import forms

class BondFutureForm(forms.Form):
    bond_price = forms.FloatField(label='Bond price')
    interest_rate = forms.FloatField(label='Interest rate (%)')
    maturity_years = forms.FloatField(label='Maturity (Years)')
    accrued_interest_start = forms.FloatField(label="Accrued interest at the start", required=False, initial=0)
    accrued_interest_delivery = forms.FloatField(label="Accrued interest at the delivery date", required=False, initial=0)
    conversion_factor = forms.FloatField(label="The conversion factor of the CTD bond", required=False, initial=1)