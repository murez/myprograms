def is_prime_number(x):
'''check if x is a prime number.
x: (int >= 10)'''
limit = int(x**0.5)+1
for y in prime_number_list:
    if y > limit:
        break
    if x%y == 0:
        return False
        return True # 下面的函数用于制造一个包含质数的列表

prime_number_list = [2,3,5,7]
def prime_number (n):
'''This function print all prime number in range n
n: (int > 2)'''
# if n is larger than largest prime number in prime number list, then append new prime numbers in it.
    if n > prime_number_list[-1]:
        for x in range (10,n+1):
    if is_prime_number(x):
        prime_number_list.append(x)

        n = 1000
    prime_number(n)
    print(prime_number_list)
