#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divi = a / b
    except ZeroDivisionError:
        divi = None
    finally:
        print("Inside result: {}".format(divi))
    return divi
