"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    houses = set()

    with open(filename, mode='rt', encoding='utf-8') as file:
      for line in file:
        house = line.strip().split('|')[2]
        if house:
          houses.add(house)

    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    students = []

    with open(filename, mode='rt', encoding='utf-8') as file:
      for line in file:
        line_arr = line.strip().split('|')
        name = ' '.join(line_arr[:2])
        student_cohort = line_arr[4]

        if cohort=='All' and student_cohort != 'I' and student_cohort != 'G':
          students.append(name)
        elif  student_cohort == cohort:
          students.append(name)

    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    with open(filename, mode='rt', encoding='utf-8') as file:
        for line in file:
            line_arr = line.strip().split('|')
            name = ' '.join(line_arr[:2])
            house = line_arr[2]
            cohort = line_arr[-1]

            if house == "Dumbledore's Army":
                dumbledores_army.append(name)
            elif house == "Gryffindor":
                gryffindor.append(name)
            elif house == "Hufflepuff":
                hufflepuff.append(name)
            elif house == "Ravenclaw":
                ravenclaw.append(name)
            elif house == "Slytherin":
                slytherin.append(name)
            elif cohort == "G":
                ghosts.append(name)
            elif cohort == "I":
                instructors.append(name)

    return [sorted(dumbledores_army), sorted(gryffindor), sorted(hufflepuff), sorted(ravenclaw), sorted(slytherin), sorted(ghosts), sorted(instructors)]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    with open(filename, mode='rt', encoding='utf-8') as file:
        for line in file:
            line_arr = line.strip().split('|')
            name = ' '.join(line_arr[:2])
            house = line_arr[2]
            head_of_house = line_arr[3]
            cohort = line_arr[4]
            person_tuple = (name, house, head_of_house, cohort)
            all_data.append(person_tuple)

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Someone else')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """
    cohort = None
    with open(filename, mode='rt', encoding='utf-8') as file:
        for line in file:
            line_arr = line.strip().split('|')
            entry_name = ' '.join(line_arr[:2])
            
            if entry_name == name:
                cohort = line_arr[4]
    
    return cohort


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    all_last_names = []
    duped_last_names = set()

    with open(filename, mode='rt', encoding='utf-8') as file:

        for line in file:
            line_arr = line.strip().split('|')
            last_name = line_arr[1]

            if last_name in all_last_names:
                duped_last_names.add(last_name)
            
            all_last_names.append(last_name)

    return duped_last_names


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    housemates = set()

    with open(filename, mode='rt', encoding='utf-8') as file:

        for line in file:
            line_arr = line.strip().split('|')
            entry_name = ' '.join(line_arr[:2])

            if entry_name == name:
                house = line_arr[2]
                cohort = line_arr[4]


    with open(filename, mode='rt', encoding='utf-8') as file:

        for line in file:
            line_arr = line.strip().split('|')
            student_house = line_arr[2]
            student_cohort = line_arr[4]
            student_name = ' '.join(line_arr[:2])

            
            if student_house == house and student_cohort == cohort and student_name != name:
                housemates.add(student_name)

    return housemates


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')

