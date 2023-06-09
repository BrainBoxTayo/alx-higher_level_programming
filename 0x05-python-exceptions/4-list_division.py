#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            new_list += [my_list_1[i] / my_list_2[i]]
        except ZeroDivisionError:
            new_list += [0]
            print("division by 0")
        except (TypeError, ValueError):
            new_list += [0]
            print("wrong type")
        except IndexError:
            new_list += [0]
            print("out of range")
        finally:
            pass
    return new_list
