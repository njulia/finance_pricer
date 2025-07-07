from math import exp

def calculate_interest_rate_swap(notional, fixed_rate, floating_rate, term_years):
    fixed = fixed_rate / 100
    floating = floating_rate / 100
    swap_value = notional * (fixed - floating) * term_years
    return round(swap_value, 2)
