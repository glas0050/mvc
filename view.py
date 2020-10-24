from model import Person


def showAllView(recordList):
    print('In our db we have %i users. Here they are:' % len(recordList))
    for item in recordList:
        print(item.name())


def startView():
    print('MVC - the simplest example')
    print('Do you want to see everyone in my db?[y/n]')


def endView():
    print('Goodbye!')
