from input import get_input, understand_input
from open_app import open_app
from search_web import search_web
from joke import joke
from ask_ai import ask_ai
from rich.console import Console
from rich.panel import Panel


def main():
    """
    Main function of the project. Calls our various imported functions of our
    project.
    """
    console = Console()
    console.print(Panel("WELCOME TO BOB", style="bold cyan"), justify="center")
    console.print(
        "You can ask one of the following things to Bob:",
        style="green",
        justify="center",
    )
    console.print(
        "* Open some app (i.e. open + ____)", style="yellow", justify="center"
    )
    console.print(
        "* Browse something (i.e. search + ____)", style="yellow", justify="center"
    )
    console.print(
        "* Ask AI some question (i.e. ask + ____)", style="yellow", justify="center"
    )
    console.print("* Listen a joke (i.e. joke)", style="yellow", justify="center")

    console.print("* Quit (i.e. quit)", style="yellow", justify="center")

    while True:
        query = get_input()
        action, value = understand_input(query)

        if action == "invalid":
            print("Invalid input. Please follow Bob instructions")
        elif action == "open":
            open_application(value)
        elif action == "search":
            search(value)
        elif action == "ask":
            print(ask(value))
        elif action == "joke":
            tell_joke()

        print()

def open_application(app):
    open_app(app)

def search(query):
    search_web(query)

def ask(question):
    return ask_ai(question)

def tell_joke():
    joke()

if __name__ == "__main__":
    main()


# all files are formatted with black
