class ComplexNumber:
    def __init__(self, re: float, im: float):
        self.Realis = re
        self.Imaginaris = im

    def __add__(self, other: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber(self.Realis + other.Realis, self.Imaginaris + other.Imaginaris)

    def __sub__(self, other: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber(self.Realis - other.Realis, self.Imaginaris - other.Imaginaris)

    def __repr__(self) -> str:
        return f"{self.Realis}{'+' if self.Imaginaris >= 0 else ''}{self.Imaginaris}i"

a = ComplexNumber(7, 3)
b = ComplexNumber(2, -4)
print("a+b =", a + b)
print("a-b =", a - b)