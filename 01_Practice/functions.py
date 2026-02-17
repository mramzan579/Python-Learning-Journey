#calculating average of three numbers
def nums_avg(num_1,num_2,num_3):
    nums=[num_1,num_2,num_3]
    avg=sum(nums)/len(nums)
    print(f"Average: {avg:.2f}")
    return avg

print(nums_avg(2,598,3))

#calculating power from current and voltage by user
def calc_power(v, i):
    power=v*i
    return power
result=calc_power(12,2)
print(f"Power: {result}")

#Checking the number if it is even or odd
def even_odd_check(a):
    if a%2==0:
        print(f"{a} is even number")
    else:
        print(f"{a} is odd number.")
    
even_odd_check(5)

#WAF to find the length of list in argument
def len_calc(nums=[]):
    return len(nums)
length=len_calc([1,2,3,2,3,4,5,4,3,6,4,5])
print(length)

#WAF to print elements of  alist in single line
cities=["Lahore","Karachi","Attock"]
def element_in_line(cities):
    for city in cities:
        print(city,end=" ")
element_in_line(cities)

#WAF to find the factorial of n
def fact_calc(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
print(f"The factorial is : {fact_calc(8)}")

#WAF to convert USD to PKR
def currency_converter(USD):
    USD_1=281.94
    PKR=USD*USD_1
    return PKR
print(f"The converted amount in rupees is : {currency_converter(9):.2f}")
