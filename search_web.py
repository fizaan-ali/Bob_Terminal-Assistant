import webbrowser


def main():
    search_web("cs50")


def build_url(keyword):
    """
    Function to build url from keyword
    """
    return "https://www.google.com/search?q=" + keyword.replace(" ", "+")


def search_web(keyword):
    """
    Function to search url in your default browser
    """
    url = build_url(keyword)

    if webbrowser.open(url):
        print(f"Searching for {keyword}...")
    else:
        print("Could not open the page")


if __name__ == "__main__":
    main()
