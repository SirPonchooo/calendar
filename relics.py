import ui

def get_duration():  # from calendar
    '''
    gets duration of the meeting, can only take values: 1 or 2
    '''

    try:
        duration = int(ui.get_input('Enter duration in hours (1 or 2)'))
    except ValueError:
        print('how about you type in a NUMBER?')
        get_duration()

    if duration in range(1, 3):
        return duration
    else:
        print('something went wrong, mate')
        get_duration()


def get_time():  # from calendar
    try:
        time = int(ui.get_input('Enter start time'))
        if time in range(8, 19):
            return time
        else:
            raise TypeError
    except (TypeError, ValueError):
        print('seems like you typed time that\'s off your working hours')
