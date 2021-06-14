#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: June 2021
# This program combines two lists and alternates them


def merge_list(first_list, second_list):
    final_list = []

    first_length = len(first_list)
    second_length = len(second_list)

    loop_counter = 0
    while first_length > loop_counter and second_length > loop_counter:
        final_list.append(first_list[loop_counter])
        final_list.append(second_list[loop_counter])
        loop_counter = loop_counter + 1

    # https://stackoverflow.com/questions/19252301/creating-a-new-list-with-subset-of-list-using-index-in-python
    if first_length < second_length:
        final_list = final_list + (second_list[loop_counter:])

    elif second_length < first_length:
        final_list = final_list + (first_list[loop_counter:])

    return final_list


def main():
    # comment

    entered_number = None
    second_number = None
    first_list = []
    second_list = []

    # input
    print("Enter -1 to end.")
    try:
        while entered_number != -1:
            entered_number = int(input("Enter a number for the first list: "))
            first_list.append(entered_number)
        first_list.pop()

        while second_number != -1:
            second_number = int(input("Enter a number for the second list: "))
            second_list.append(second_number)
        second_list.pop()

        m_list = merge_list(first_list, second_list)

        print("{0}".format(m_list))
    except Exception:
        print("That was not a number please try again")


if __name__ == "__main__":
    main()
