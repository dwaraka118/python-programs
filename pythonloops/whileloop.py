# Program to add natural
# numbers upto
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

n = int(input("enter the range of numbers to be added : "))

# initialize sum and counter
sum = 0
i = 0

while i <= n:
    sum = sum + i
    i = i+1 # update counter
    print("sum for now is",sum)
    print("the next number to be added is:", i)


# print the sum
print("The total sum is", sum)