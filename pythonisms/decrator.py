from genrator import GLinkedList
import time

def calculate_time(any_fun):
  def wrapper(*args,**kwargs):
    starting_time = time.time()
    result = any_fun(*args,**kwargs)
    ending_time = time.time()
    print (ending_time-starting_time)
    return result
  return wrapper

@calculate_time
def check_equality(linked_list1,linked_list2):
    return linked_list1 == linked_list2

def debug_code(any_fun):
  def wrapper(*arg, **kwargs):
    x = arg
    y = kwargs
    print(f'inputs are : {x}, {y}')
    output = any_fun(*arg, **kwargs)
    print(f'output is : {output}')
    return output

  return wrapper
@debug_code
def sumation(n):
    if n == 1:
        return 1
    else:
        return n+sumation(n-1)

def slow_down(func):
    def wrapper(*args,**kwargs):
        time.sleep(1)
        output = func(*args,**kwargs)
        return output
    return wrapper

@slow_down
def counter_down(n):
    print(n)
    if n != 0:
        counter_down(n-1) 

def convert_returned(func):
    def wrapper(*args,**kwargs):
        output = func(*args,**kwargs)
        return f"the returned value was {output}"
    return wrapper

@convert_returned
def add(x,y):
    return x+y

if __name__ == "__main__":
    ll1 = GLinkedList()
    ll1.insert(1)
    ll1.insert(2)
    ll1.insert(3)
    ll1.insert(4)
    ll1.insert(5)
    ll1.insert(6)
    ll2 = GLinkedList()
    ll2.insert(6)
    ll2.insert(5)
    ll2.insert(4)
    ll2.insert(3)
    ll2.insert(2)
    ll2.insert(1)
    check_equality(ll1,ll2)
   
    counter_down(7)
    print(add(14,6))

