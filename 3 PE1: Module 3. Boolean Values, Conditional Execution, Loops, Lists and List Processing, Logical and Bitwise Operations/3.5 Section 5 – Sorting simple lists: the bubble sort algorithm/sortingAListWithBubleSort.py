my_list = [8, 10, 6, 2, 4]  # list to sort


def sortTheList(listToSort):
    swap = True

    while swap:
        swap = False
        for num in range(len(listToSort) - 1):
            if listToSort[num] > listToSort[num + 1]:
                swap = True
                listToSort[num], listToSort[num + 1] = listToSort[num + 1], listToSort[num]

    return listToSort


res = sortTheList(my_list)
print(res)


# If you want Python to sort your list, you can do it like this:


# my_list = [8, 10, 6, 2, 4]
# my_list.sort()
# print(my_list)
