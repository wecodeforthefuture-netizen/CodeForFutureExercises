WIDTH = 60


def divider():
    print("=" * WIDTH)


def title(name):

    divider()

    print(name.center(WIDTH))

    divider()


def section(name):

    print()

    print("-" * WIDTH)

    print(name)

    print("-" * WIDTH)


def pause():

    input("\nPress ENTER to continue...")


def goodbye():

    divider()

    print("Thank you for playing!")

    print("God bless!")

    divider()


def error(message):

    print()

    print(f"ERROR: {message}")
