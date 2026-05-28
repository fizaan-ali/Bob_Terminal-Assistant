from ask_ai import ask_ai
import pyttsx3


def main():
    joke()


def joke():
    """
    Function to make a joke from ask_ai and say it
    """
    engine = pyttsx3.init()
    response = ask_ai("Tell me a random dev joke in about one or two line. Be creative")
    engine.say(response)
    print(response)
    engine.runAndWait()


if __name__ == "__main__":
    main()
