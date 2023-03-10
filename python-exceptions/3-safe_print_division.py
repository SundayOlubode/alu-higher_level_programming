#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        result = round((a / b),1)
    except:
        result = None
    finally:
        print('Inside result: {}'.format(result))
