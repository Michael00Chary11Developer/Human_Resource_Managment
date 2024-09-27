from decimal import Decimal


def calculate_gross_salary(base_salary, housing_allowance, child_allowance, food_allowance, number_of_child, marital_status):

    if marital_status == 'single' or (marital_status == 'married' and number_of_child in [0, None]):
        return base_salary + housing_allowance + food_allowance

    return base_salary + housing_allowance + (number_of_child*child_allowance) + food_allowance


def calculate_net_salary(gross_salary, tax_rate=Decimal('0.1')):

    return gross_salary * (Decimal(1) - tax_rate)
