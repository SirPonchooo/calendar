import ui
import storage


def schedule_new(meetings):
    '''
    prompts user for input and uses input to append data file
    the input should be as follows:
    1. name of the meeting, which will be stored as a string
    2. duration of the meeting, 1 or 2 (hours). int
    3. time of meeting (between 8 and 18). int
    if a wrong type of data is passed, exception should be raised and handled
    '''

    new_meeting = []
    print('Schedule a new meeting.')
    title = get_title()
    clock = get_numerals()
    duration = clock[0]
    time = clock[1]
    new_meeting.append(time)
    new_meeting.append(time + duration)
    new_meeting.append(title)
    print('Schedule updated.\n\n')
    return new_meeting


def get_title():  # done
    try:
        title = str(ui.get_input('Enter meeting title'))
        return title
    except ValueError:
        print('try again...')


def get_numerals():

    things_to_munch = [
        ['duration', 1, 3, 'Enter duration in hours (1 or 2)',
         'you can set only 1, or 2h long meetings'],

        ['time',  8, 19, 'Enter start time',
         'seems like you typed time that\'s off your working hours']
    ]

    things_to_return = []

    for thing in things_to_munch:
        item_to_return = thing[0]
        time1 = thing[1]
        time2 = thing[2]
        input_message = thing[3]
        error_message = thing[4]
        iterator = 1

        while iterator == 1:  # for iterator in range 2
            try:
                item_to_return = int(ui.get_input(input_message))
                iterator = 2
            except (ValueError, TypeError):
                print('how about you type in a NUMBER?')

            if iterator == 2:
                if item_to_return in range(time1, time2):
                    things_to_return.append(item_to_return)
                    iterator = 0
                else:
                    print(error_message)
                    iterator = 1

    return things_to_return


def cancel_meeting(meetings_list):
    '''
    asks user for the hour of the already existing meeting,
    then, based on that number, finds the meeting and deletes it
    '''
    print('Cancel an existing meeting.')
    hour_to_free = int(ui.get_input('Enter the start time'))
    print(meetings_list)
    for lst in meetings_list:
        print(lst)
        if hour_to_free == lst[0]:
            meetings_list.remove(lst)
            print('deleted\n\n')
            return meetings_list
        else:
            print('not scheduled anything on this time\n\n')


def user_choice(meetings, switch):

    new_data = []  # here all the data from this function is complied, so it can be used in other functions
    choice = ui.get_input('Your choice')  # just a friendly shortcut for input function from outside the module

    if choice == 's':
        meetings.append(schedule_new(new_data))

    elif choice == 'c':
        meetings = cancel_meeting(meetings)

    elif choice == 'q':
        switch = False
        return switch


# def switch():


def main():
    running = True
    meetings = []
    while running:
        ui.schedule_info(meetings)
        ui.print_menu()
        running = user_choice(meetings, running)  # to zwróci meetings, ale samo nie przypisze running
        # ponieważ funkcje potrafią zwracać przedmioty modyfikowalne, ale nie booleanskie


if __name__ == '__main__':
    main()
