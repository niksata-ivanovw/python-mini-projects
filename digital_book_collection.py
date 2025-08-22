from operator import index

import random

titles = []      # List of book titles
authors = []     # List of book authors
statuses = []    # List of read statuses: "Read" or "Unread"

def add_book(title: str, author: str):
    if title not in titles:
        titles.append(title)
        authors.append(author)
        statuses.append('Unread')
        print(f'The book {title} was added succesfully.')
    else:
        print(f'The book {title} is already added.')

def mark_as_read(title: str):
    if title in titles:
        book_index = titles.index(title)
        if statuses[book_index] == 'Unread':
            statuses[book_index] = 'Read'
            print(f'The status of book {titles[book_index]} was succesfully changed to "Read"')
        else:
            print(f'This book is already read')
    else:
        print(f'The book {title} was not found.')

def mark_as_unread(title: str):
    if title in titles:
        book_index = titles.index(title)
        if statuses[book_index] == 'Read':
            statuses[book_index] = 'Unread'
            print(f'The status of book {titles[book_index]} was succesfully changed to "Unread"')
        else:
            print(f'This book still hasn\'t been read')
    else:
        print(f'The book {title} was not found.')

def search_book(keyword: str):
    for current_book in titles:
        if current_book == keyword:
            index = titles.index(current_book)
            print(f'Search succesful. Book: {current_book}, author: {authors[index]}, status: {statuses[index]}')
            return
    for current_author in authors:
        if current_author == keyword:
            index = authors.index(current_author)

#TODO list all the books of the author

            print(f'Search succesful. Author: {current_author}.')
            return
    print(f'No book or author found.')

def list_books():
    for current_book in titles:
        current_index = titles.index(current_book)
        print(f'Book: {current_book}, author: {authors[current_index]}, status: {statuses[current_index]}')

def suggest_book():
    unread_books = []
    for index, current_status in enumerate(statuses):
        if current_status == 'Unread':
            unread_books.append(titles[index])
    if unread_books:
        random_index = random.randint(0, len(unread_books) - 1)
        print(f'A good recomendation from your unread books would be {unread_books[random_index]}!')
    else:
        print('No unread books left.')

def delete_book(title: str):
    if title in titles:
        index = titles.index(title)
        del titles[index], authors[index], statuses[index]
        print('Book removed succesfully.')
    else:
        print('There isn\'t a book with that title in the collection.')

def sort_books():
    sorted_titles = sorted(titles)
    print('Here are the books in alphabetical order:')
    for title in sorted_titles:
        print(title)


def main():
    print("📚 Welcome to the Digital Book Collection Manager 📚\n")

    while True:
        print("\nPlease choose an option:")
        print("1. Add a new book")
        print("2. Mark a book as read")
        print("3. Mark a book as unread")
        print("4. Search for a book")
        print("5. List all books")
        print("6. Suggest a book to read")
        print("7. Delete a book")
        print("8. Sort the books alphabetically")
        print("9. Exit")

        choice = input("\nEnter your choice (1-8): ")

        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            add_book(title, author)

        elif choice == '2':
            title = input("Enter the title of the book to mark as read: ")
            mark_as_read(title)

        elif choice == '3':
            title = input("Enter the title of the book to mark as unread: ")
            mark_as_unread(title)

        elif choice == '4':
            keyword = input("Enter a keyword to search: ")
            search_book(keyword)

        elif choice == '5':
            list_books()

        elif choice == '6':
            suggest_book()

        elif choice == '7':
            title = input("Enter the title of the book to delete: ")
            delete_book(title)

        elif choice == '8':
            sort_books()

        elif choice == '9':
            print("Goodbye! Happy reading! 📖")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 8.")

if __name__ == "__main__":
    main()