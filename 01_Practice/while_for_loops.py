count=10
while count>=5:
    print(count)
    count-=1

num=0
while num<=10:
    print(num)
    num+=1
#print numbers from 1 to 100
i=1
while i<=100:
    print(i)
    i+=1
#print numbers from 100 to 1
i=100
while i>=1:
    print(i)
    i-=1
#print multiplication table of number n
num=int(input("Enter the number: "))
i=1
while i<=10:
    print(num*i)
    i+=1
#print elements of a list using loop
a=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<=len(a)-1:
    print(a[i])
    i+=1
#finidng number from list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 7, 5, 87, 56, 54, 54]
i = 0
x = 9
found = False

while i < len(nums):
    if nums[i] == x:
        found = True
        break  # Exit loop immediately once found
    i += 1

if found:
    print(f"{x} exists in the list")
else:
    print(f"{x} was not found")