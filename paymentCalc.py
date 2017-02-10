balance = float(raw_input("Enter the credit card balance"))
originalBalance = balance
annualInterestRate = float(raw_input("Enter the annual interest rate"))
months_to_repay = int(raw_input("How many months should it take to pay off the balance?"))
monthlyInterestRate = annualInterestRate / 12.0
hi = (originalBalance * (1+monthlyInterestRate) ** 12)/months_to_repay
lo = originalBalance / months_to_repay
foundAnswer = False
while not foundAnswer:
    payment = (hi+lo)/2
    for n in range(months_to_repay):
        balance -= payment
        balance += (balance * monthlyInterestRate)
    if balance < 0 and balance > -.25:
        foundAnswer = True
    elif balance < 0:
        hi = payment
    else:
        lo = payment
    balance = originalBalance
print ("Lowest Payment: " + str(round(payment,2)))
