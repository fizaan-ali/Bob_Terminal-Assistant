from groq import Groq
from dotenv import load_dotenv  # for security purposes
import os

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=API_KEY)


def main():

    print(ask_ai("What is an API key? How to use them can i share my api key public?"))


def ask_ai(question):
    """
    Function to generate answer from GROQ AI via api key and
    return that response
    """
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant", messages=[{"role": "user", "content": question}]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    main()
