from dataclasses import dataclass
from typing import Optional


@dataclass
class DealBasedCommission:
    commission: int = 10000
    deals_landed: float = 0

    def compute_pay(self) -> int:
        return int(self.commission * self.deals_landed)


@dataclass
class HourlyEmployee:
    name: str
    id: int
    pay_rate: int = 0
    hours_worked: float = 0
    employer_cost: int = 100000
    commission: Optional[DealBasedCommission] = None

    def compute_pay(self) -> int:
        total = int(self.pay_rate * self.hours_worked + self.employer_cost)
        if self.commission:
            total += self.commission.compute_pay()
        return total


@dataclass
class SalariedEmployee:
    name: str
    id: int
    monthly_salary: int = 0
    percentage: float = 1
    commission: Optional[DealBasedCommission] = None

    def compute_pay(self) -> int:
        total = int(self.monthly_salary * self.percentage)
        if self.commission:
            total += self.commission.compute_pay()
        return total


@dataclass
class Freelancer:
    name: str
    id: int
    pay_rate: int = 0
    hours_worked: float = 0
    vat_number: str = ""
    commission: Optional[DealBasedCommission] = None

    def compute_pay(self) -> int:
        total = int(self.pay_rate * self.hours_worked)
        if self.commission:
            total += self.commission.compute_pay()
        return total


def main():
    henry = HourlyEmployee(name="Henry", id=123456, pay_rate=5000, hours_worked=100)
    print(f"{henry.name} earned ${(henry.compute_pay() / 100):.2f}.")
    sarah_commission = DealBasedCommission(deals_landed=10)
    sarah = SalariedEmployee(name="Sarah", id=47832, monthly_salary=500000, commission=sarah_commission)
    print(f"{sarah.name} earned ${(sarah.compute_pay() / 100):.2f}.")


if __name__ == "__main__":
    main()
