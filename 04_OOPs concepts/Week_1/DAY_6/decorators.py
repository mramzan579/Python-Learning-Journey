#first challnege on decorators
def uppercase(func):
    def inner_wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):#checks data type of result, if it is string then convert to uppercase
            return result.upper()
        return result
    return inner_wrapper
@uppercase
def greet(name):
    return f"Hello, {name}!"
print(greet("ali"))

#function time tracker decorator
import time
def time_tracker(func):
    def inner_wrapper(*args, **kwargs):
        start_time = time.time() #start time before function execution
        result = func(*args, **kwargs)
        end_time = time.time() #end time after function execution
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.12f} seconds")
        return result
    return inner_wrapper
@time_tracker
def compute_sum():
    #dont try to compute sum of numbers from 1 to 100 million on your local machine as it may take a long time and consume a lot of resources.
    sum1=sum(range(1, 100000000))#computes sum of numbers from 1 to 100 million
    return sum1
print(compute_sum())

#user role verification decorator
def check_user_status(func):
    def inner_wrapper(*args, **kwargs):
        # Checking ke kwargs mein 'role' hai ya args mein
        user_role = kwargs.get('role') if 'role' in kwargs else (args[1] if len(args) > 1 else None)

        if user_role == "admin":
            print("[STATUS]: Status verified!")
            return func(*args, **kwargs)
        else:
            print("[X] Access denied! You are not an admin.")
            
            
    return inner_wrapper
@check_user_status
def delete_user(user_id, role):
    print(f"User with ID {user_id} has been deleted.")
    return True
delete_user(123, role="admin")  # Should allow deletion
delete_user(456, role="user")   # Should deny access

#repeat/retry execution decorator
def repeat_execution(n):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            for i in range(n):
                print(f"Attempt {i + 1} of {n}")
                result = func(*args, **kwargs)
            return result
        return inner_wrapper
    return wrapper
@repeat_execution(n=5)
def greet_user(name):
    print(f"Hello, {name}!")
greet_user("Ali")  # This will greet the user 5 times