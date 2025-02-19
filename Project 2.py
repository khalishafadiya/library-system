library = {
    "books": [
        [1, "The Poppy War", "R. F. Kuang", 2018, True],
        [2, "Alone With You in the Ether", "Olivia Blake", 2020, True],
        [3, "The Ballad of Songbirds and Snakes", "Suzanne Collins", 2020, True],
        [4, "Babel", "R. F. Kuang", 2022, True],
        [5, "The Midnight Library", "Matt Haig", 2020, True],
        [6, "We'll Prescribe You a Cat", "Syou Ishida", 2024, True],
        [7, "Heartless", "Marissa Meyer", 2016, True],
        [8, "2025 K-Consumer Trend Insights", "Rando Kim", 2024, True],
        [9, "Quiet: The Power of Introverts in a World That Can't Stop Talking", "Susan Cain", 2012, True],
        [10, "Pale Blue Dot: A Vision of the Human Future in Space", "Carl Sagan", 1994, True],
    ],
    "borrowed": []
}

def create_book():
    book_id = len(library['books']) + 1
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = int(input("Enter year of publication: "))
    library['books'].append([book_id, title, author, year, True])
    print(f"Book '{title}' added successfully!")

def read_books():
    if not library['books']:
        print("No books available.")
    else:
        print("\nBook List:")
        for book in library['books']:
            status = "Available" if book[4] else "Borrowed"
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}, Status: {status}")

def update_book():
    book_id = int(input("Enter the ID of the book to update: "))
    for book in library['books']:
        if book[0] == book_id:
            book[1] = input("Enter new title: ") or book[1]
            book[2] = input("Enter new author: ") or book[2]
            try:
                book[3] = int(input("Enter new year of publication: ")) or book[3]
            except ValueError:
                pass
            print("Book updated successfully!")
            return
    print("Book not found.")

def delete_book():
    book_id = int(input("Enter the ID of the book to delete: "))
    for book in library['books']:
        if book[0] == book_id:
            library['books'].remove(book)
            print("Book deleted successfully!")
            return
    print("Book not found.")

def calculate_due_date(borrow_date):
    year, month, day = map(int, borrow_date.split('-'))
    day += 14
    while day > 30:
        day -= 30
        month += 1
        if month > 12:
            month = 1
            year += 1
    return f"{year:04d}-{month:02d}-{day:02d}"


def borrow_book():
    book_id = int(input("Enter the ID of the book to borrow: "))
    for book in library['books']:
        if book[0] == book_id and book[4]:
            book[4] = False
            borrower_name = input("Enter your name: ")
            borrow_date = input("Enter borrow date (YYYY-MM-DD): ")
            due_date = calculate_due_date(borrow_date)
            library['borrowed'].append([book_id, borrower_name, borrow_date, due_date])
            print(f"Book '{book[1]}' borrowed successfully! Due date: {due_date}")
            return
    print("Book not found or already borrowed.")

def return_book():
    book_id = int(input("Enter the ID of the book to return: "))
    for record in library['borrowed']:
        if record[0] == book_id:
            library['borrowed'].remove(record)
            for book in library['books']:
                if book[0] == book_id:
                    book[4] = True
                    print(f"Book '{book[1]}' returned successfully!")
                    return
    print("Borrow record not found.")

def search_books():
    query = input("Enter search term (title, author, or year): ").lower()
    results = []
    for book in library['books']:
        if query in str(book[1]).lower() or query in str(book[2]).lower() or query == str(book[3]):
            results.append(book)
    if results:
        print("\nSearch Results:")
        for book in results:
            status = "Available" if book[4] else "Borrowed"
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}, Status: {status}")
    else:
        print("No matching books found.")

def main_menu():
    while True:
        print("\nLibrary System Menu")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Search Books")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_book()
        elif choice == '2':
            read_books()
        elif choice == '3':
            update_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            borrow_book()
        elif choice == '6':
            return_book()
        elif choice == '7':
            search_books()
        elif choice == '8':
            print("Exiting Library System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
