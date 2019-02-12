'''
演算法 | 二進位搜尋演算法---使用Python3
https://hugheschung.blogspot.com/2019/01/python3.html
'''
def binary_search(list, item):
    low = 0
    high = len(list)-1  #len() 找出list中有多少個元素

    while low <= high:
        mid = round((low + high) / 2)   # 找出中位數，並用round()四捨五入
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1,3,5,7,9]
print(binary_search(my_list,3))   #印出在list中的位置
print(binary_search(my_list,9))   #印出在list中的位置
print(binary_search(my_list,2))   #印出在list中的位置
