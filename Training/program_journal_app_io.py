import journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print('________________________')
    print('      JOURNAL APP')
    print('________________________')


def run_event_loop():
    print('What do you want to do with your journal today? ')
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)
    while cmd != 'x' and cmd:
        cmd = input('[L]ist Entries, [A]dd an entry, e[X]it:  ')

        cmd = cmd.lower().strip()
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print('Sorry we do not understand "{}" '.format(cmd))

    print('See you next time. ')
    journal.save(journal_name, journal_data)


def list_entries(data):
    print('Your journal entries')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('{0}, {1}'.format(idx + 1, entry))


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)


if __name__ == '__main__':
    main()



