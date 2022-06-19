from dataclasses import dataclass


@dataclass
class HourlyEmployee:
    name: str
    id: int
    pay_rate: int = 0
    hours_worked: float = 0
    employer_cost: int = 100000

    def compute_pay(self) -> int:
        return int(self.pay_rate * self.hours_worked + self.employer_cost)


@dataclass()
class HourlyEmployeeWithCommission(HourlyEmployee):
    commission: int = 10000
    deals_landed: float = 0

    def compute_pay(self) -> int:
        return super().compute_pay() + int(self.commission * self.deals_landed)


@dataclass
class SalariedEmployee:
    name: str
    id: int
    monthly_salary: int = 0
    percentage: float = 1

    def compute_pay(self) -> int:
        return int(self.monthly_salary * self.percentage)


@dataclass()
class SalariedEmployeeWithCommission(SalariedEmployee):
    commission: int = 10000
    deals_landed: float = 0

    def compute_pay(self) -> int:
        return super().compute_pay() + int(self.commission * self.deals_landed)


@dataclass
class Freelancer:
    name: str
    id: int
    pay_rate: int = 0
    hours_worked: float = 0
    vat_number: str = ""

    def compute_pay(self) -> int:
        return int(self.pay_rate * self.hours_worked)


@dataclass()
class FreelancerWithCommission(Freelancer):
    commission: int = 10000
    deals_landed: float = 0

    def compute_pay(self) -> int:
        return super().compute_pay() + int(self.commission * self.deals_landed)


def main():
    henry = HourlyEmployee(name="Henry", id=123456, pay_rate=5000, hours_worked=100)
    print(f"{henry.name} earned ${(henry.compute_pay() / 100):.2f}.")
    sarah = SalariedEmployeeWithCommission(name="Sarah", id=47832, monthly_salary=500000, deals_landed=10)
    print(f"{sarah.name} earned ${(sarah.compute_pay() / 100):.2f}.")


if __name__ == "__main__":
    main()
