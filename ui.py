import storage


def print_menu():
    '''
    Function prints out menus for user
    UZYJ TU LIST COMP.!!!!!!!
    '''

    print('Menu:')
    print('(s) schedule a new meeting')
    print('(c) cancel an existing meeting')
    print('(q) quit\n')


def schedule_info(schedule_4_the_day):
    '''
    function prints out the current schedule data, or
    "(empty)", if there's no schedule at all
    '''
    print('Your schedule for the day:')
    if schedule_4_the_day == []:
        print('(empty)\n')
    else:
        for lst in schedule_4_the_day:
            print("{} - {} {}".format(lst[0], lst[1], lst[2]))
        print('\n')
        # print(schedule_4_the_day, '\n')
    # if schedule_4_the_day is None:
    #     print('(empty)\n')
    # else:
    #     print(''.join(schedule_4_the_day),'\n')
    # '''parametr was schedule_4_the_day=None'''


def get_input(str):
    return input(str + ': ')


# print_menu()
