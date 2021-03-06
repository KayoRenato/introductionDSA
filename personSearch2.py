def main():

    people = ['Monteiro Lobato', 'Jose de Alencar',
              'Celilia Meireles', 'Carlos Drummond de Andrade',
              'Machado de Assis', 'Clarice Lispector',
              'Graciliano Ramos', 'Guimaraes Rosa', 'Ruth Rocha',
              'Luis Fernando Verissimo']

    print(people)
    print('')

    # Sort people list
    peopleSorded = sorted(people)

    # Search position of a person on list
    name = input('Name: ')

    # Function for define position of name

    def binarySearch(list, name):
        fistElement = 0
        lastElement = len(list)-1
        position = -1
        finded = False

        while not finded and fistElement <= lastElement:
            half = (fistElement + lastElement)//2

            if list[half] == name:
                finded = True
                position = half
            elif list[half] > name:
                lastElement = half - 1
            else:
                fistElement = half + 1

        return position

    # Call function
    position = binarySearch(peopleSorded, name)

    print("\nList Sorded")
    print(peopleSorded)

    if position == -1:
        print(f'\nIt\'s Name, {name}, not included in list.\n')
    else:
        print(
            f'\n{name} is included in list. Your position is {position} in list.\n')


main()
