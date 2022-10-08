""""
author: Anishya Thinesh
file: prefix_search.py
description: this file searches through a text file either in a binary or
linear fashion and looks for a word that is given by the user.
"""



def linear_search(list, user_prefix):
    """ performs a linear search to find a word with matching prefix in a list
    :param list: (list) list that contains all words in a text file
    :param user_prefix: (String) a prefix that the user wants to look for.
    :return i: (int) returns index of matching prefix i if it exists
    :return -1: (int) returns -1 if no matching string is found.
    """
    if len(user_prefix) > 1:
        for i in range(len(list)):
            list_word = list[i]
            list_word = list_word[:len(user_prefix)]
            if list_word == user_prefix:
                return i
    elif len(user_prefix) == 1:
        for i in range(len(list)):
            list_word = list[i]
            if list_word[0] == user_prefix:
                return i
    return -1




def binary_search(list, user_prefix, start, end):
    """ performs a binary search to find a word with matching prefix in a list
    :param list: (list) list that contains all words in a text file
    :param user_prefix: (String) a prefix that the user wants to look for.
    :param start: (int) the changing start point of considered part of list
    :param end: (int) the changing end point of considered part of list
    :return mid_index: (int) returns index of matching prefix if it exists
    :return -1: (int) returns -1 if no matching string is found.
    """
    if len(user_prefix) > 1:
        mid_index = (start + end) // 2
        mid_value = list[mid_index]
        user_prefix_ascii = []
        list_value_ascii = []

        for ch in user_prefix:
            user_prefix_ascii.append(ord(ch))

        for i in range(len(user_prefix)):
            list_value_ascii.append(ord(mid_value[i]))

        if mid_index == len(list)-1 or mid_index == 0:
            if user_prefix_ascii == list_value_ascii:
                return mid_index
            else:
                return -1


        if user_prefix_ascii == list_value_ascii:
            return mid_index
        elif user_prefix_ascii < list_value_ascii:
            return binary_search(list, user_prefix, start, mid_index-1)
        elif user_prefix_ascii > list_value_ascii:
            return binary_search(list, user_prefix, mid_index+1, end)
        else:
            return -1

    elif len(user_prefix) == 1:
        mid_index = (start + end) // 2
        mid_value = list[mid_index]

        if ord(mid_value[0]) == ord(user_prefix):
            return mid_index
        elif mid_index == len(list)-1:
            if ord(mid_value[0]) == ord(user_prefix):
                return mid_index
            else:
                return -1
        elif ord(mid_value[0]) > ord(user_prefix):
            return binary_search(list, user_prefix, start, mid_index - 1)
        elif ord(mid_value[0]) < ord(user_prefix):
            return binary_search(list, user_prefix, mid_index + 1, end)
        else:
            return -1




def check_sorted(list):
    """ this function handles the case of the text file being not alphabetically sorted.
    :param list: (list) list that contains all words in a text file
    :return flag: (boolean) this value returns false if the list id not in alphabetical order
    """
    flag = True
    for i in range(len(list)-1):
        word1 = list[i]
        word2= list[i+1]
        if ord(word1[0]) > ord(word2[0]):
            flag = False
    return flag




def main():
    """ main function
    """
    file_name = input("Enter the name of a file to search through: ")
    list = []
    with open(file_name) as fd:
        for line in fd:
            line = line.strip()
            list.append(line.lower())

    if len(list) == 0:
        print("The text file is empty.")
        quit()

    if not check_sorted(list):
        print("The text file is not alphabetically sorted.")
        quit()

    type_of_search = input("Enter type of search [binary/linear]: ")

    if type_of_search == "Linear" or type_of_search == "linear":
        while True:
            user_prefix = input("Enter a prefix to search or a blank line to"
                                " quit: ")
            if user_prefix == "":
                print("Thanks for searching!")
                quit()
            elif linear_search(list, user_prefix) == -1:
                print("No word matching your prefix was found.")
            else:
                print(list[linear_search(list, user_prefix)])

    elif type_of_search == "Binary" or type_of_search == "binary":
        while True:
            user_prefix = input("Enter a prefix to search or a blank line to"
                                " quit: ")
            if user_prefix == "":
                print("Thanks for searching!")
                quit()
            elif binary_search(list, user_prefix, 0, len(list)) == -1:
                print("No word matching your prefix was found.")
            else:
                print(list[binary_search(list, user_prefix, 0, len(list)-1)])

    else:
        print("Your input was invalid.")



if __name__ == "__main__":
    main()
