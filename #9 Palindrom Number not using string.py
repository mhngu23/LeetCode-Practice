'''Checking if n is a palindrome or not not using string function
take 121 % 10 => dig = 1
rev = 1
n = 121//10 = 12
take 12%10 => dig = 2
rev = 1*10+2 = 12
n = 12//10 = 1
take 1%10 dig = 1
rev = 12*10+1 = 121
n = 1//10 = 0
=> Check temp and rev
=> return value
'''
n = 121
temp = n
rev = 0
while (n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
if (temp == rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")