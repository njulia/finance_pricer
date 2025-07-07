from django.db import models

class BondFutureCalculation(models.Model):
    bond_price = models.FloatField()
    interest_rate = models.FloatField()
    maturity_years = models.FloatField()
    future_price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Bond Future Price: {self.future_price}"
