'''总结：

	•	浅拷贝传参：对于嵌套的可变对象，子对象仍然是引用传递，修改子对象会影响外部对象。
	•	深拷贝传参：完全独立的对象，即使嵌套对象也不会影响外部对象。
	•	不可变对象传参：不可变对象在函数内部修改不会影响外部对象，无论是否使用拷贝。
'''
import copy


def modify_list(lst):
    lst_copy = copy.copy(lst)  # 创建浅拷贝
    lst_copy[0] = 'modified'
    print("Inside function:", lst_copy)


my_list = [1, 2, 3]
modify_list(my_list)
print("Outside function:", my_list)

'''Inside function: ['modified', 2, 3]
Outside function: [1, 2, 3]'''


# import copy


# def modify_nested_list(lst):
#     lst_copy = copy.copy(lst)  # 浅拷贝
#     lst_copy[0][0] = 'modified'
#     print("Inside function:", lst_copy)


# my_list = [[1, 2], [3, 4]]
# modify_nested_list(my_list)
# print("Outside function:", my_list)

'''Inside function: [['modified', 2], [3, 4]]
Outside function: [['modified', 2], [3, 4]]'''


# import copy
# def modify_deep_list(lst):
#     lst_copy = copy.deepcopy(lst)  # 创建深拷贝
#     lst_copy[0][0] = 'modified'
#     print("Inside function:", lst_copy)


# my_list = [[1, 2], [3, 4]]
# modify_deep_list(my_list)
# print("Outside function:", my_list)

'''Inside function: [['modified', 2], [3, 4]]
Outside function: [[1, 2], [3, 4]]'''

# 传递不可变对象
# 当传递不可变对象（如整数、字符串、元组等）时，无论是浅拷贝还是深拷贝都无效，因为这些对象无法在函数内部修改。

# def modify_value(x):
#     x = 10
#     print("Inside function:", x)


# y = 5
# modify_value(y)
# print("Outside function:", y)
