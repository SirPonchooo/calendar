import ui


def import_data(filename='test.txt'):

    result = []
    with open(filename, 'r') as datafile:
        for line in datafile.readfile():
            result.append(line.strip().split(','))
    return result


def export_data(meetings, filename='test.txt', mode='w'):
    '''
    Export data from a list to file. If called with mode 'w' it should overwrite
    data in file. If called with mode 'a' it should append data at the end.

    :param list meetings:
    :param str filename: optional, default='test.txt, name of export file
    :param str mode: optional, default=write,
    '''

    if mode not in ['a', 'w']:
        raise ValueError('Wrong write mode')

    with open(filename, mode) as datafile:
        for meeting in meetings:
            datafile.write(','.join(meeting) + '\r\n')

# zamykanie plików!! zapytaj kogoś żeby Ci wytłumaczył dlaczego trzeba to robić, nie koniecznie jak
# (bo wywali błąd; jakieś szczegóły)
