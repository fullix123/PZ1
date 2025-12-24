#1
n = int(input("Количество ступенек: "))

if n <= 1:
    print(1)
else:
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    print(b)



#2
nums = list(map(int, input("Введите числа через пробел: ").split()))

max_sum = nums[0]
current_sum = nums[0]

for num in nums[1:]:
    current_sum = max(num, current_sum + num)
    max_sum = max(max_sum, current_sum)

print("Максимальная сумма:", max_sum)


#3
n = int(input("Введите сумму: "))
coins = [1, 3, 4]

dp = [float('inf')] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i - coin] + 1)

print(f"Минимальное количество монет: {dp[n]}")


#4
s1 = input("Первая строка: ")
s2 = input("Вторая строка: ")

n = len(s1)
count = 0

for i in range(n):
    if s1[i] != s2[i]:
        count += 1

print(f"Редакционное расстояние:  {count}")

