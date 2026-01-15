def calculate_average (num1:float, num2:float, num3:float) -> float:
    total_avg = (num1 + num2 + num3)/3
    return total_avg

def add_tax (bill_total: float) -> float:
    tax = bill_total * .10
    total_bill = bill_total + tax
    return total_bill

def greet_user (name: str) -> str:
    return f"Hello {name}"