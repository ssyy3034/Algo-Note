A = 300
B = 60
C = 10
A_num = 0
B_num = 0
C_num = 0
N = int(input())
click_num = 0
A_num += N // A
N = N%A
B_num += N // B
N = N%B
C_num += N // C
N = N % 10
if N != 0:
    print(-1)
else:
    print(A_num, B_num, C_num)
