import time
import random
import keyboard

def get_random_sentence():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "She sells seashells by the seashore.",
        "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
        "Peter Piper picked a peck of pickled peppers.",
        "I scream, you scream, we all scream for ice cream.",
        "The early bird catches the worm.",
        "A picture is worth a thousand words.",
        "Actions speak louder than words.",
        "You miss 100% of the shots you don't take.",
        "When life gives you lemons, make lemonade."
        
    ]
    return random.choice(sentences)

def speed_typing_test():
    while True:
        text = get_random_sentence()
        print("Type the following text:")
        print(text)
        print("Press Enter when ready.")
        input()

        print("Start typing...")
        start_time = time.time()
        user_text = input()
        end_time = time.time()

        time_taken = end_time - start_time
        words_typed = user_text.split()
        correct_words = text.split()
        mistakes = 0

        for i in range(len(words_typed)):
            if i >= len(correct_words):
                break
            if words_typed[i] != correct_words[i]:
                mistakes += 1

        speed = len(words_typed) / time_taken * 60

        accuracy = 0
        if len(words_typed) > 0:
            accuracy = ((len(words_typed) - mistakes) / len(words_typed)) * 100

        print("\nResults:")
        print(f"Time taken: {time_taken:.2f} seconds")
        print(f"Words typed: {len(words_typed)}")
        print(f"Typing speed: {speed:.2f} words per minute")
        print(f"Mistakes made: {mistakes}")
        print(f"Accuracy: {accuracy:.2f}%")

        print("\nPress 'Enter' to continue or 'Esc' to exit.")
        exit_key = keyboard.read_key()
        if exit_key.lower() == 'esc':
            break

        # Clear the console before starting the next typing test
        print("\n" * 50)

speed_typing_test()



