import re
import sys
from rich.console import Console

console = Console()


def main():

    while True:
        understand_input(get_input())


def get_input():
    """
    Function to get the input from user strip and lowercase it
    and return the result
    """
    console.print(":> ", style="bold cyan", end="")
    query = input().strip().lower()
    return query


def understand_input(query):
    """
    Function to understand what our input means
    -> it helps us which function to call
    """
    if re.search(r"^quit$", query):
        console.print("Good Bye", style="red")
        sys.exit()

    elif match := re.search(r"^open\s+(.+)$", query):
        app = match.group(1)
        # print("Open triggered!", app)
        return ("open", app)

    elif match := re.search(r"^search\s+(.+)$", query):
        search = match.group(1)
        # print("Search triggered!", search)
        return ("search", search)

    elif match := re.search(r"^ask\s+(.+)$", query):
        ask = match.group(1)
        # print("Ask triggered!", ask)
        return ("ask", ask)

    elif re.search(r"^joke$", query):
        # print("Joke triggered!")
        return ("joke", None)

    else:
        # print("Invalid input.. Please follow Bob instructions!!")
        return ("invalid", None)


if __name__ == "__main__":
    main()
