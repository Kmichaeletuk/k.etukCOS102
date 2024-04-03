def annuity_payment(principal, annual_interest_rate, time_period):
    """
    Calculate the payment amount for an annuity plan.

    Args:
    principal (float): The principal amount.
    annual_interest_rate (float): The annual interest rate (in decimal).
    time_period (int): The time period (in years).

    Returns:
    float: The payment amount for the annuity plan.
    """
    r = annual_interest_rate / 12  # Monthly interest rate
    n = time_period * 12  # Number of payments
    payment = principal * (r * (1 + r)**n) / ((1 + r)**n - 1)
    return payment

# Example usage:
principal_amount = 100000  # Principal amount
annual_interest_rate = 0.06  # Annual interest rate (6%)
time_period_years = 20  # Time period in years

# Calculate annuity payment
payment_amount = annuity_payment(principal_amount, annual_interest_rate, time_period_years)
print("Annuity Payment Amount:", payment_amount)
