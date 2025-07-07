"""
This Python code calculates the theoretical fair price of a US Treasury bond future. It uses a standard financial model called the **cost-of-carry model**, based on the principle of **no-arbitrage**. Essentially, it determines what the future price *should* be today so that no one can make a risk-free profit by buying the bond now and selling the future, or vice versa. It accounts for the cost of holding the bond until the future delivery date (the "carry cost") and the specific characteristics of the bond deliverable into the future contract.

### Parameters Explained

The function `calculate_bond_future_price` takes the following inputs:

*   **`clean_price`**: This is the market price of the underlying bond *excluding* any accrued interest. It's the most commonly quoted price for bonds.
*   **`conversion_factor`**: US Treasury bond futures contracts allow the seller to deliver any of several eligible bonds. Each eligible bond has a unique "conversion factor" provided by the exchange. This factor adjusts the invoice price to make different deliverable bonds roughly equivalent in value, reducing the delivery option's value to the seller.
*   **`accrued_interest_start`**: This is the amount of interest that has accumulated on the bond since the last coupon payment date up to the *start date* (time 0) of our calculation. This is added to the clean price to get the total cash needed to buy the bond today.
*   **`risk_free_rate`**: The annualized interest rate used to calculate the cost of financing or the return from investing the money required to hold the bond until the future's delivery date. It's typically based on Treasury bill rates or repo rates for the relevant time period. It's provided as a decimal (e.g., 5% is 0.05).
*   **`time_to_delivery`**: The time period, in years, from the start date of the calculation to the delivery date of the futures contract. This is used to compound the cost of holding the bond.
*   **`accrued_interest_delivery`**: The amount of interest that is expected to accumulate on the bond from the last coupon payment date up to the *delivery date* of the futures contract. This is subtracted from the theoretical invoice price to arrive at the quoted (clean) price.

### Calculation Logic Detailed

The function performs the calculation in three main steps:

1.  **Calculate the Full Price at the Start:**
    ```python
    full_price = clean_price + accrued_interest_start
    ```
    The `clean_price` is what's typically quoted, but when you actually buy a bond, you have to pay the clean price *plus* any interest that has accrued since the last coupon payment. This `full_price` (also known as the "dirty price" or "cash price") represents the actual amount of money needed to purchase the bond *today*.

2.  **Calculate the Theoretical Futures Invoice Price:**
    ```python
    futures_invoice_price = full_price * math.exp(risk_free_rate * time_to_delivery)
    ```
    This step calculates the *future value* of the initial investment (`full_price`) assuming it's held (and financed) at the `risk_free_rate` until the delivery date. The `math.exp()` function is used for **continuous compounding**, a common assumption in financial models for simplicity. This `futures_invoice_price` represents the theoretical total amount that should be paid at the delivery date for the specific bond being considered. It's derived from the no-arbitrage principle: the future price must equal the cost of buying the asset today and holding it until the future date. This is the **cost-of-carry** component – specifically, the cost of financing the initial purchase. (A more complete model would also subtract the future value of any coupons received between the start and delivery dates, but this simplified code omits that).

3.  **Derive the Quoted Futures Price:**
    ```python
    quoted_futures_price = (futures_invoice_price - accrued_interest_delivery) / conversion_factor
    ```
    The price of a bond future is always quoted in terms of a standardized contract, not the specific dirty price of the deliverable bond.
    *   First, we subtract the `accrued_interest_delivery` from the `futures_invoice_price`. The invoice price calculated in step 2 is a "dirty price" at the future date. Bond futures are quoted on a "clean" price basis. So, subtracting the accrued interest at delivery gives us the theoretical *clean* price of the deliverable bond at the delivery date.
    *   Second, we divide this theoretical clean price by the bond's `conversion_factor`. The futures contract specifies that the final invoice amount paid by the buyer (and received by the seller) will be `Quoted Futures Price * Conversion Factor + Accrued Interest at Delivery`. By rearranging this formula, we get the `quoted_futures_price` based on the calculated theoretical invoice price. This division adjusts the price of the *specific* deliverable bond to the standardized price used for trading the future.

The function then returns this `quoted_futures_price`.

### Connecting to Financial Concepts

*   **No-Arbitrage:** The core principle behind this calculation. The formula ensures that the theoretical future price is set such that there is no way to make a risk-free profit by combining a position in the spot bond and a position in the future. If the market price deviates significantly from this theoretical price, arbitrage opportunities would arise, and trading by sophisticated participants would quickly push the market price back towards the theoretical value.
*   **Cost of Carry:** This is the net cost (or benefit) of holding an asset over a period of time. For a bond, the main components are the financing cost (the interest paid to borrow the money to buy the bond) and the income received (the coupon payments). This simplified code primarily focuses on the financing cost component, represented by compounding the initial full price at the risk-free rate. A more detailed cost-of-carry model would also factor in the future value of any coupon payments received between the start and delivery dates, which would *reduce* the theoretical futures price. The `futures_invoice_price` calculation effectively represents the initial cost plus the net cost of carry (financing cost minus any benefit like coupons).

This model provides a fundamental benchmark for evaluating whether a bond future is potentially over- or under-priced in the market, ignoring complexities like the cheapest-to-deliver option and market liquidity.
"""
import math

def calculate_bond_future(
    clean_price: float,
    risk_free_rate: float,
    time_to_delivery: float,
    accrued_interest_start: float = 0,
    conversion_factor: float = 1,
    accrued_interest_delivery: float = 0
) -> float:
    """
    Calculates the theoretical price of a US Treasury Bond Future using a
    no-arbitrage cost-of-carry model with continuous compounding.

    Args:
        clean_price: The clean price of the cheapest-to-deliver (CTD) bond.
        conversion_factor: The conversion factor of the CTD bond.
        accrued_interest_start: Accrued interest at the start (time 0).
        risk_free_rate: The annualized risk-free interest rate (as a decimal).
        time_to_delivery: Time to delivery of the futures contract in years.
        accrued_interest_delivery: Accrued interest at the delivery date.

    Returns:
        The theoretical quoted futures price.
    """
    # 1. Calculate the full price (dirty price) of the bond at the start.
    full_price = clean_price + accrued_interest_start

    # 2. Calculate the futures invoice price by finding the future value of the
    #    full price, compounded at the risk-free rate.
    interest_rate = risk_free_rate / 100
    futures_invoice_price = full_price * math.exp(interest_rate * time_to_delivery)

    # 3. Derive the quoted futures price from the invoice price.
    quoted_futures_price = (futures_invoice_price - accrued_interest_delivery) / conversion_factor

    return quoted_futures_price


def calculate_bond_future_no_acc(bond_price, interest_rate, maturity_years):
    # Using the formula: F = P * e^(r * T)
    r = interest_rate / 100  # convert percentage to decimal
    F = bond_price * math.exp(r * maturity_years)
    return round(F, 2)


