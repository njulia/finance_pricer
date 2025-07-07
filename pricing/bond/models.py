from django.db import models

class BondFutureCalculation(models.Model):
    bond_price = models.FloatField()
    interest_rate = models.FloatField()
    maturity_years = models.FloatField()
    accrued_interest_start = models.FloatField(default=0, null=True, blank=True)
    accrued_interest_delivery = models.FloatField(default=0, null=True, blank=True)
    conversion_factor = models.FloatField(default=1)
    future_price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Bond Future Price: {self.future_price}"
