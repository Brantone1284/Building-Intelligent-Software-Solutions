#function that sort a list of dictionaries by a key
from operator import itemgetter
def sort_dicts_Manual(dict_list,key):
    """
        Sort a list of dictionaries by a specific key.
    Args:
        dict_list (list): List of dictionaries.
        key (str): Key to sort by.
    Returns:
        list: Sorted list of dictionaries.
    """
    return sorted(dict_list,key=itemgetter(key))

#manual execution
data = [
    {'name':'Emmah','age':21},
    {'name':'Ali','age':20},
    {'name':'John','age':19},
    {'name':'Effie','age':23},
    {'name':'Elis','age':15},
    {'name':'Eucabeth','age':31}
]
print(sort_dicts_Manual(data,'age'))

#write a function that sorts a list of dictionaries by a key in descending order
def sort_dicts_AI(dict_list, key):
    """
        Sort a list of dictionaries by a specific key in descending order.
    Args:
        dict_list (list): List of dictionaries.
        key (str): Key to sort by.
    Returns:
        list: Sorted list of dictionaries in descending order.
    """
    return sorted(dict_list, key=itemgetter(key))

print(sort_dicts_AI(data, 'age'))


#benchmark - using timeit module to measure execution time
import timeit

