from django.db import models

class InterestRateSwapCalculation(models.Model):
    notional = models.FloatField()
    fixed_rate = models.FloatField()
    floating_rate = models.FloatField()
    term_years = models.FloatField()
    swap_value = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Swap Value: {self.swap_value}"