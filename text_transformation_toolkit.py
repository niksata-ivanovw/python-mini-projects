from collections import Counter
import string

#TODO Write the transformed text to a .txt file for saving results.
#TODO Use colorama to highlight results in color in the terminal.

print("🧠 Welcome to the Text Transformation Toolkit!")
print("Choose a transformation:")
print("1. Reverse Text")
print("2. Convert to Uppercase")
print("3. Convert to Lowercase")
print("4. Title Case")
print("5. Count Vowels")
print("6. Remove All Spaces")
print("7. Replace Vowels with '*'")
print("8. Check if Palindrome")
print("9. Word Frequency Counter")
print("10. Count consonants")
print("11. Sort the words in alphabetical order")
print("12. Search for a word")
print("13. Replace a word")
print("14. Exit the program")

while True:
    choice = int(input('\nEnter the number corresponding to your choice: '))
    if choice == 14:
        print("Bye!")
        break

    text = input("Enter the text: ")

    vowels = ['a', 'o', 'e', 'i', 'u', 'A', 'O', 'E', 'I', 'U']
    if choice == 1:
        text = text[::-1]
        print(f'The formatted text is: {text}')

    elif choice == 2:
        text = text.upper()
        print(f'The formatted text is: {text}')

    elif choice == 3:
        text = text.lower()
        print(f'The formatted text is: {text}')

    elif choice == 4:
        text = text.title()
        print(f'The formatted text is: {text}')

    elif choice == 5:
        vowels_count = 0
        for current_letter in text:
            if current_letter in vowels:
                vowels_count += 1

        print(f'The vowels in the text are exactly: {vowels_count}')

    elif choice == 6:
        text = text.replace(' ', '')
        print(f'The formatted text is: {text}')

    elif choice == 7:
        formatted_text = []
        for current_letter in text:
            if current_letter in vowels:
                formatted_text.append('*')
            else:
                formatted_text.append(current_letter)
        print(f'The formatted text is: {"".join(formatted_text)}')

    elif choice == 8:
        text = text.lower()
        if text == text[::-1]:
            print('The text is a palindrome')
        else:
            print('The text is not a palindrome')

    elif choice == 9:
        cleaned_text = text.lower().translate(str.maketrans('', '', string.punctuation))
        words = cleaned_text.split()
        word_counts = Counter(words)

        for word, count in word_counts.items():
            print(f'The word "{word}" is found {count} times.')

    elif choice == 10:
        cleaned_text = text.lower().translate(str.maketrans('', '', string.punctuation))
        consonants_count = 0
        for current_letter in cleaned_text:
            if current_letter not in vowels:
                consonants_count += 1

        print(f'There are a total of {consonants_count} consonants in the text.')

    elif choice == 11:
        cleaned_text = text.lower().translate(str.maketrans('', '', string.punctuation))
        text_list = cleaned_text.split()
        text_list = sorted(text_list)
        sorted_words = " ".join(text_list)
        print(f"These are the words in alphabetical order: {sorted_words}.")

    elif choice == 12:
        word_to_search = input()
        text = text.lower()
        if word_to_search in text:
            is_found = True
        else:
            is_found = False

        if is_found:
            print(f'The word {word_to_search} is in the text.')
        else:
            print(f'The word {word_to_search} is not in the text.')

    elif choice == 13:
        old_word = input("Which word do you want to replace? ")
        new_word = input("And with what word do you want to replace it? ")
        if old_word in text:
            text = text.replace(old_word, new_word)
            print(f"Here's the new text: {text}")
        else:
            print("The word which you want to replace is not in the text.")