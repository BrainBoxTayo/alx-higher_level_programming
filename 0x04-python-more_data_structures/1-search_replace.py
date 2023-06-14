#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''search and replace in a list'''
    new_list = my_list.copy()
    for i in new_list:
        if search == my_list[my_list.index(i)]:
            j = new_list.index(search)
            new_list[j] = replace
    return new_list
