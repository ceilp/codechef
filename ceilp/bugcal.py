class Solver:
    @staticmethod
    def calculate(a, b):
        num = ((a % 10) + (b % 10)) % 10
        summ = (int(a / 10) + int(b / 10)) * 10 + num
        return summ


# t = int(input())
# for i in range(1, t + 1):
#     n, m = [int(s) for s in input().split(" ")]
#     print(Solver.calculate(n, m))

