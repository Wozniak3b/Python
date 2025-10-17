class FibonacciSeq:
    def __init__(self, steps: int):
        self.steps = steps
        self.counter = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.steps:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.counter += 1
        return value

for x in FibonacciSeq(20):
    print(x, end=" ")
