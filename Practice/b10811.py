n,m = map(int, input().split())

baskets = list(range(1, n + 1))

for _ in range(m):
    i,j = map(int, input().split())
    sliced_basket = baskets[i-1:j]
    sliced_basket.reverse()
    baskets = baskets[:i-1] + sliced_basket + baskets[j:]

print(" ".join(map(str, baskets)))

