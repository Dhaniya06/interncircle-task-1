from collections import Counter
import re

def word_counter():
    filename = input("Enter the text file name: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        words = re.findall(r"\b[\w']+\b", text.lower())

        print("\n=== Word Counter ===")
        print("Total words:", len(words))

        frequency = Counter(words)

        print("\nWord Frequency:")
        for word, count in frequency.most_common():
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("Error: File not found.")
        print("Please make sure the file exists in the same folder.")


word_counter()
