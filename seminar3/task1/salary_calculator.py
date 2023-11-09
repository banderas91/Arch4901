class SalaryCalculator:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def calculate_net_salary(self):
        tax = int(self.base_salary * 0.25)  # рассчитать налог другим способом
        return self.base_salary - tax
