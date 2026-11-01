# 48. Compute simple interest from principal, rate, and time.

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time period in years: "))

if principal < 0 or rate < 0 or time < 0:
    print("Principal, interest rate, and time cannot be negative.")
else:
    simple_interest = (principal * rate * time) / 100

    print("The simple interest is:", simple_interest)
