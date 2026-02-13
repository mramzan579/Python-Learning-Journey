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

