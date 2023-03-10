#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    
    for i in range(len(list_length)):
        try:
            result = round((my_list_1[i] / my_list[i]), 1)
        except TypeError:
            print('wrong type')
        except ZeroDivisionError:
            print('division by 0')
        except IndexError:
            print('out of range')
        except:
            result = 0
        else:
            new_list.append(result)
        finally:
            return result