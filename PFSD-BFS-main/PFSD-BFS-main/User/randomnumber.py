import random
import string

def passgen():
    result = ''.join(random.sample(string.ascii_lowercase, 6))
    return (result)
def usergen():
    result=''.join(random.sample(string.hexdigits,6))
    return (result)
def pingen():
    result=''.join(random.sample(string.digits,4))
    return (result)

def cvvgen():
    result=''.join(random.sample(string.digits,3))
    return (result)

def cardnumbergen():
    result=''.join(random.sample(string.digits,8))
    return (result)

def otpgen():
    result=''.join(random.sample(string.digits,6))
    return (result)

def loan_calculator(loan_amount,interest):
    return loan_amount + interest

def calculate_interest(category):
    if category == 'education':
        return 7
    elif category == 'home':
        return 6.5
    elif category == 'vehicle':
        return 8
    elif category == 'business':
        return 9
    elif category == 'personal':
        return 10


    