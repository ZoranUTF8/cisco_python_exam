# list_1 = [1,2,3,4,5]
# # my_list[start:end] OR my_list[:end]

# list_2 = list_1[0:2]
# list_1[0] = 2
# print(list_2)

# TODO Slices – negative indices
#
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:-1]
# print(new_list)
# #  [8, 6, 4]
#
#
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[:3]
# print(new_list)
# #  [10, 8, 6]

# TODO More about the del instruction
# The previously described del instruction is able to delete more
# than just a list's elements at once ‒ it can delete slices too:


# my_list = [10, 8, 6, 4, 2]
# del my_list[1:3]
# print(my_list)
# del my_list[:] delete all

#  TODO 3.6.4 The in and not in operators
# Python offers two very powerful operators, able to look through the list in order
# to check whether a specific value is stored inside the list or not.

# elem in my_list
# elem not in my_list
#
# my_list = [0, 3, 12, 8, 2]
#
# print(5 in my_list)
# print(5 not in my_list)
# print(12 in my_list)

# TODO 3.6.5 Lists – some simple programs

# The first of them tries to find the greater value in the list. Look at the code in the editor.
# def getGreatNum(ls):
#     grt = None
#
#     if len(ls) > 0:
#         grt = ls[0]
#
#         for num in range(len(ls)):
#             if ls[num] > grt:
#                 grt = ls[num]
#     else:
#         print("Your list is empty")
#
#     return grt
#
#
# my_list = [0, 3, 12, 8, 2]
#
# res = getGreatNum(my_list)
# print(res)

# Now let's find the location of a given element inside a list:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5


def findIfExistsInList(ls, to_find):
    if to_find in ls:
        return True
    else:
        return False


res = findIfExistsInList(my_list, to_find)
print(res)
