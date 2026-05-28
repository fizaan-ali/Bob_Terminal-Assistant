# Bob - Terminal Assistant
#### Video Demo: https://youtu.be/jfgsMc50I4I
#### Description:

## What is Bob?

Bob is a terminal-based personal assistant built entirely in Python. The idea is simple, instead of alt-tabbing between apps, opening a browser manually, or typing full commands, you just tell Bob what you want in plain English and it handles it. You can open applications, search Google, ask an AI a question, or listen to a joke, all without leaving your terminal.

I built Bob as my CS50P final project because I wanted to make something I would actually use. Early on I had bigger ideas, but I deliberately scoped it down to four features done well rather than ten done poorly.

## Project Structure

The project is split across multiple files, each with a single responsibility. Nothing is crammed into one big file.

**project.py**

This is the entry point. Running `python project.py` starts Bob. It prints the welcome screen using the `rich` library, then enters a loop that keeps asking for input until the user quits. Each iteration it calls `get_input()` to collect the user's query, passes it to `understand_input()` to figure out what was meant, and then calls the right feature function based on the result. The main file itself has almost no logic, it just coordinates between the other modules.

**input.py**

This file contains the brain of Bob. `get_input()` is straightforward — it takes input, strips whitespace, and converts to lowercase so the parser never has to worry about capitalization. `understand_input()` is where the real work happens. It uses Python's `re` module to match the user's input against patterns for each command. Each pattern uses a capture group to extract the useful part, for example `^open\s+(.+)$` matches anything starting with "open" and captures everything after it. The function returns a tuple like `("open", "chrome")` or `("search", "black holes")` so the caller knows both what to do and what to do it with. If nothing matches it returns `("invalid", None)`.

**open_app.py**

Contains a dictionary called `APPS` that maps app names to their executable paths or system command names. `open_app()` looks up the name and uses `subprocess.Popen()` to launch it. I chose `Popen` over `subprocess.run()` deliberately — `run()` blocks until the launched program closes, which would freeze Bob. `Popen` launches the app and returns immediately so Bob stays responsive.

**search_web.py**

Contains `build_url()` which takes a search query and builds a Google search URL by replacing spaces with `+` and appending to the base URL. Then `search_web()` calls `webbrowser.open()` with that URL. I split the URL building into its own function specifically so it could be unit tested without actually opening a browser.

**ask_ai.py**

Sets up the Groq API client using an API key loaded securely from a `.env` file. `ask_ai()` sends the user's question to the LLaMA model on Groq and returns the response as a string. It returns the text rather than printing it directly so the caller decides what to do with it — this matters because `joke.py` needs to both print and speak the response.

**joke.py**

Imports `ask_ai()` and calls it with a prompt asking for a short creative dev joke. It then uses `pyttsx3` to speak the joke out loud through the system speaker. I initialized the `pyttsx3` engine inside the function rather than at the module level because initializing it once at the top caused issues on repeated calls — the engine would not speak the second time.

**test_project.py**

Contains pytest tests for the pure logic functions. It tests `understand_input()` across all valid commands and invalid inputs, verifies that typing "quit" raises `SystemExit`, and tests `build_url()` with both single and multi-word queries. Functions with side effects like opening apps, calling the API, or speaking are not unit tested since they depend on external systems.

## Setup

Install dependencies:

```
pip install groq python-dotenv pyttsx3 rich
```
or 
```
pip install -r requirements.txt
```

Create a `.env` file in the project folder:

```
GROQ_API_KEY=your_key_here
```

Get a free API key from console.groq.com. Then run:

```
python project.py
```

## Design Decisions



**Separate files for each feature**

Keeping each feature in its own module means adding a new feature later is as simple as creating a new file and adding one elif in project.py. Nothing else changes. It also makes testing cleaner since each module can be imported and tested independently.

**Groq over other AI providers**

Groq provides a genuinely free API tier with no credit card required. For a student project this matters. The API is also compatible with the OpenAI interface format so switching providers later would require minimal changes to the code.

**API key security**

The API key is stored in a `.env` file and loaded using `python-dotenv`. It is never written directly in the source code. A `.gitignore` file ensures the `.env` file is never pushed to GitHub. A `.env.example` file is included in the repo so anyone who clones the project knows exactly what they need to set up.

## Known Limitations

The app dictionary is hardcoded. If an app is not in the list Bob cannot open it, but adding one is just adding a line to the dictionary. The regex parser requires a specific command format. Bob has no memory — each question is independent with no conversation history between turns.
