testcase = int(input())
charges = [int(input()) for _ in range(testcase)]

for charge in charges:
    Q = charge // 25
    charge %= 25
    D = charge // 10
    charge %= 10
    N = charge // 5
    charge %= 5
    P = charge
    print(Q, D, N, P)

