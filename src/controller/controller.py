from pip._vendor.distlib.compat import raw_input

from src.model.model import Person
from src.view import view


def showAll():
    # gets list of all Person objects
    people_in_db = Person.getAll()
    # calls view
    return view.showAllView(people_in_db)


def start():
    view.startView()
    userInput = raw_input()
    if userInput == 'y':
        return showAll()
    else:
        return view.endView()


if __name__ == "__main__":
    # running controller function
    start()
