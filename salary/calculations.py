from decimal import Decimal


def calculate_gross_salary(base_salary, housing_allowance, child_allowance, food_allowance, number_of_child):

    return base_salary + housing_allowance + (number_of_child*child_allowance) + food_allowance


def calculate_net_salary(gross_salary, tax_rate=Decimal('0.1')):

    return gross_salary * (Decimal(1) - tax_rate)
