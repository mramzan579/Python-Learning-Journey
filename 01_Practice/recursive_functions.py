#Write a recursive function to calculate th esum of first n numbers
def sum_n_numbers(n):
    if n==0:
        return 0
    return sum_n_numbers(n-1)+n
print(sum_n_numbers(790))

#WARF to print elements of a list
cities=["lahore","Karachi","Islamabad"]
def element_printing(list):
    if len(list)==0:
        return
    print(list[0],end=" ")
    return element_printing(list[1:])
element_printing(cities)
print()

#WARF to print elements of a list using index
def print_list(list,idx=0):
    if len(list)==idx:
        return
    print(list[idx],end=" ")
    return print_list(list,idx+1)
countries=["Pakistan","India","Iran","Afghanistan","China"]
print_list(countries)