"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
def is_prime(int):
    if(int < 2):
        return False
    i = 2
    while i < int*0.5+1: 
        if int % i ==0:
            return False
        else:
            i += 1
    return True



def primes(number_of_primes):
    list = []
    num = 2 # first prime number 

    if number_of_primes <= 0:
        raise ValueError (f"Number should be a positive number")
    else:
        while len(list) < number_of_primes:
            if is_prime(num):
                list.append(num)
            num += 1
        return list
