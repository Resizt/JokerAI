import random

# List of jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why do we never tell secrets on a farm? Because the potatoes have eyes and the corn has ears!",
    "Why don't skeletons fight each other? They don't have the guts!",
    "Why don't some couples go to the gym? Because some relationships don't work out!",
    "I was going to tell a time traveling joke, but you guys didn't like it.",
    "Wanna see me run to that mountain? Wanna see me do it again?"
]


def tell_joke():
    return random.choice(jokes)

def main():
    print("JOKER.AI")
    while True:
        input("Press Enter to hear a joke. Press 'x' to quit.")
        user_input = input().lower()

        if user_input == 'x':
            print("Goodbye! Have a great day!")
            break

        joke = tell_joke()
        print(joke)

if __name__ == "__main__":
    main()
