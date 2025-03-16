# Task 4

# 1. Program to create a list for all the even numbers and another list for all the odd numbers from
# the given set of numbers

numlist = [10,501,22,37,100,999,87,351]

even = list(filter(lambda num: num % 2 == 0, numlist))
print(f"Even numbers are:",(even))

odd = list(filter(lambda num: num % 2 == 1, numlist))
print(f"Odd numbers are:",(odd))

# 2. Program to create a list for all the Prime numbers from the set of numbers given

mylist=[10,501,22,37,100,999,87,351]
prime_no=[]
for i in mylist :
    c=0
    for j in range(1,i):
        if i%j==0:
            c+=1
    if c==1:
        prime_no.append(i)
print(f"Prime numbers from the given list:",(prime_no))

# 4. Python program to add the first and the last digit of an integer

number = 3101

number = str(number)
first_digit = int(number[0])
last_digit = int(number[-1])
sum = first_digit + last_digit

print(f"Sum of the first and last digit of the number {number} is", sum)

#6. To find the duplicates from the given lists
# Defining three lists of numbers

list1 = [11, 12, 13, 14, 15, 16, 17]
list2 = [14, 15, 16, 17, 18]
list3 = [11,13,15,17,19]

common = list(set(list1) & set(list2) & set(list3))
print(f"The duplicates in the given three list are", common)

# 8. Program to find the minimum element of the sorted and rated list from the numbers that are displayed below:
list1 = [18,84,6,89,99]

list1.sort()

print("The minimum element of the sorted list is:", list1[0])

# 9. Program to find the triplet in list whose sum is equal to 59

from itertools import combinations

def findTriplets(num_list, key):

    def valid(val):
        return sum(val) == key

    return list(filter(valid, list(combinations(num_list, 3))))

num_list = [10,20,30,9]
print(findTriplets(num_list, 59))

# 10. Program to find if there is a sublist with sum equal to zero
def subArrayExists(arr, n):
    n_sum = 0
    s = set()
    for i in range(n):
        n_sum += arr[i]
        if n_sum == 0 or n_sum in s:
            return True
        s.add(n_sum)
    return False
arr = [4, 2, -3, 1, 6]
n = len(arr)
if subArrayExists(arr, n) == True:
    print("Found a subarray with sum as 0")
else:
    print("No such sub array exits!")