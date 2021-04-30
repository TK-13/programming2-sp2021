import nltk
import random
import time

from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download([
    "vader_lexicon",
])

JOKES = [
    ("What gets wetter the more it dries?", "a towel"),
    ("Why was the broom late?", "It overswept!"),
    ("What goes up and down, but does not move?", "stairs")
]


def greet(name, greeting="", message="Good morning!"):
    if greeting:  # did the user override the greeting variable?
        print("{0} {1}, {2}".format(greeting, name, message))
    else:
        print("{0}, {1}".format(name, message))


def get_sentiment(text, key=None):
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(text)
    if not key:
        return scores.get("compound")
    return scores.get(key)


# with inspiration from TK's labs
def validate_input(valid_options, question=None):
    lowercase_options = [option.lower() for option in valid_options]
    if not question:  # default behavior
        question = "Please enter a valid response ({0}): ".format(", ".join(lowercase_options))
    else:
        question += "\nPlease enter a valid response ({0}): ".format(", ".join(lowercase_options))
    while True:
        user_entry = input(question).lower()
        if user_entry in lowercase_options:
            return user_entry


def tell_a_joke():
    joke, answer = random.choice(JOKES)
    print(joke)
    time.sleep(2)
    print("...")
    time.sleep(2)
    print(answer)
    print()


def main():
    name = input("What is your name: ")
    greet(name)
    feelings = input("How are you feeling today?\n")
    sentiment = get_sentiment(feelings)
    if sentiment > 0:
        print("I'm glad you're having a good day!")
    else:
        greet(name, message="I'm sorry...")
        while True:
            print("Can I tell you a joke?")
            answer = validate_input(["yes", "no"])
            if answer == "no":
                print("Hope you feel better soon!")
                break
            tell_a_joke()

    print("Talk to you later :)")


# If the program is run (instead of imported), run the game:
if __name__ == "__main__":
    main()

# TAKEAWAYS
# have a main function, and call everything from there!!
# only use variables that were passed into your function, or are constants
# make good use of default parameters
# with default parameters, the non-optional ones have to come first!
# when you're calling a function with default parameters, it's good practice to name the default variables you are using
# define your functions in a logical order
# add comments
# descriptive variable and function names
