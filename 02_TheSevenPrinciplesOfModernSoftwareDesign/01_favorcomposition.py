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

    def compute_pay(self) -> int:
        return int(self.hourly_rate * self.hours_worked + self.employer_cost)


@dataclass()
class SalariedContract:
    monthly_salary: int
    percentage: float = 1

    def compute_pay(self) -> int:
        return int(self.monthly_salary * self.percentage)


@dataclass
class DealBasedCommission:
    commission: int = 10000
    deals_landed: float = 0

    def compute_pay(self) -> int:
        return int(self.commission * self.deals_landed)


@dataclass
class Employee:
    name: str
    id: int
    payment_sources: List[PaymentSource] = field(default_factory=list)

    def add_payment_source(self, payment_source: PaymentSource):
        self.payment_sources.append(payment_source)

    def compute_pay(self) -> int:
        return sum(source.compute_pay() for source in self.payment_sources)

# @dataclass
# class HourlyEmployee:
#     name: str
#     id: int
#     pay_rate: int = 0
#     hours_worked: float = 0
#     employer_cost: int = 100000
#     commission: Optional[DealBasedCommission] = None
#
#     def compute_pay(self) -> int:
#         total = int(self.pay_rate * self.hours_worked + self.employer_cost)
#         if self.commission:
#             total += self.commission.compute_pay()
#         return total

# Don't do this.
# @dataclass
# class HourlyEmployeeWithCommission(HourlyEmployee):
#     commission: int = 10000
#     deals_landed: float = 0
#
#     def compute_pay(self) -> int:
#         return super().compute_pay() + int(self.commission * self.deals_landed)


# @dataclass
# class SalariedEmployee:
#     name: str
#     id: int
#     monthly_salary: int = 0
#     percentage: float = 1
#     commission: Optional[DealBasedCommission] = None
#
#     def compute_pay(self) -> int:
#         total = int(self.monthly_salary * self.percentage)
#         if self.commission:
#             total += self.commission.compute_pay()
#         return total

# Don't do this.
# @dataclass
# class SalariedEmployeeWithCommission(SalariedEmployee):
#     commission: int = 10000
#     deals_landed: float = 0
#
#     def compute_pay(self) -> int:
#         return super().compute_pay() + int(self.commission * self.deals_landed)


# @dataclass
# class Freelancer:
#     name: str
#     id: int
#     pay_rate: int = 0
#     hours_worked: float = 0
#     vat_number: str = ""
#     commission: Optional[DealBasedCommission] = None
#
#     def compute_pay(self) -> int:
#         total = int(self.pay_rate * self.hours_worked)
#         if self.commission:
#             total += self.commission.compute_pay()
#         return total

# Don't do this.
# @dataclass
# class FreelancerWithCommission(Freelancer):
#     commission: int = 10000
#     deals_landed: float = 0
#
#     def compute_pay(self) -> int:
#         return super().compute_pay() + int(self.commission * self.deals_landed)


def main() -> None:
    # henry = HourlyEmployee(name="Henry", id=1223, pay_rate=5000, hours_worked=100, commission=DealBasedCommission())
    henry = Employee(name="Henry", id=1223)
    henry.add_payment_source(HourlyContract(5000, hours_worked=100))
    print(f"{henry.name} earned ${(henry.compute_pay() / 100):.2f}.")

    sarah_commission = DealBasedCommission(deals_landed=10)
    # sarah = SalariedEmployee(name="Sarah", id=434536, monthly_salary=500000, commission=sarah_commission)
    sarah = Employee(name="Sarah", id=434536)
    sarah.add_payment_source(SalariedContract(monthly_salary=500000))
    sarah.add_payment_source(sarah_commission)
    print(f"{sarah.name} earned ${(sarah.compute_pay() / 100):.2f}.")


if __name__ == "__main__":
    main()
