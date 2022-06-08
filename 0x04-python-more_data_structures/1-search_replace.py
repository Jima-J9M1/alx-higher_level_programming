#!/usr/bin/python3
def search_replace(my_list, search, replace):
    idx = my_list.index(search)
    new_list = [x for x in my_list]
    new_list[idx] = replace
    return new_list
