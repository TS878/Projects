import re
points = 0
def strength_checker(text, points):
    uppercase = re.compile('[A-Z]')
    lowercase = re.compile('[a-z]')
    numbers = re.compile('[1-9]')
    special = re.compile('[!|@#$%^&*()_+=-{}/]')
    list = [uppercase, lowercase, numbers, special]

    if len(text) >= 12:
        points += 2
        print('Length: Passed')
    elif len(text) >= 8:
        points += 1
        print('Length: Failed')
    else:
        print('Length: Failed')

        for i in list:
            if i.search(text) != None:
                points += 1
    return points


password = input('What is your current password?\n')
points = strength_checker(password, points)
if points == 6:
    print('You have a strong password')
elif points in range(4,6):
    print('You have a good password, but there is room for improvment.')
elif points in range(1,4):
    print('You have a weak password')
