# multiples of 3 and 5
def check_multiple(number: int) -> bool:
    if number % 3 == 0 and number % 5 == 0:
        return True
    else:
        return False

# checking the password
def check_password(input_string: str) -> str:
    secret_password = "Python123"
    if input_string == secret_password:
        return "access granted"
    else:
        return "access denied"


# tax return
#  <= $11k: 10%, $11k - $44,725: 12%, 
#  $44,725 - $95,375: 22%, Over $95,375: 24%
def calculate_federal_tax(salary: int) -> int:
    if salary > 95375:
        tax_amount = salary * .24
        return tax_amount
    elif 44725 <= salary <= 95375:
        tax_amount = salary * .22
        return tax_amount
    elif 11000 <= salary <= 44725:
        tax_amount = salary * .12
        return tax_amount
    else:
        tax_amount = salary * .10
        return tax_amount
    