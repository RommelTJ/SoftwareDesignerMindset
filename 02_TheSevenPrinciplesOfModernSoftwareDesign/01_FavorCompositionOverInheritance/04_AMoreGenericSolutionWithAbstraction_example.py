from dataclasses import dataclass, field
from typing import Protocol, List


class PaymentSource(Protocol):

    def compute_pay(self) -> int:
        ...


@dataclass()
class HourlyContract:
    hourly_rate: int
    hours_worked: float
    employer_cost: int = 100000

    def compute_pay(self):
        return int(self.hourly_rate * self.hours_worked + self.employer_cost)


@dataclass()
class SalariedContract:
    monthly_salary: int
    percentage: float = 1

    def compute_pay(self):
        return int(self.monthly_salary * self.percentage)


@dataclass()
class DealBasedCommission:
    commission: int = 10000
    deals_landed: float = 0

    def compute_pay(self) -> int:
        return int(self.commission * self.deals_landed)


@dataclass()
class Employee:
    name: str
    id: int
    payment_sources: List[PaymentSource] = field(default_factory=list)

    def add_payment_source(self, payment_source: PaymentSource):
        self.payment_sources.append(payment_source)

    def compute_pay(self) -> int:
        return sum(source.compute_pay() for source in self.payment_sources)


def main():
    henry = Employee(name="Henry", id=123456)
    henry.add_payment_source(HourlyContract(hourly_rate=5000, hours_worked=100))
    print(f"{henry.name} earned ${(henry.compute_pay() / 100):.2f}.")
    sarah = Employee(name="Sarah", id=47832)
    sarah.add_payment_source(SalariedContract(monthly_salary=500000))
    sarah.add_payment_source(DealBasedCommission(deals_landed=10))
    print(f"{sarah.name} earned ${(sarah.compute_pay() / 100):.2f}.")


if __name__ == "__main__":
    main()
