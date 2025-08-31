import json

# File name where books will be stored
FILE_NAME = "library.json"

# Function to load books from JSON file
def load_books():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # if file not found, return empty list
    except json.JSONDecodeError:
        return []  # if file is empty/corrupted, return empty list

# Function to save books to JSON file
def save_books(books):
    with open(FILE_NAME, "w") as f:
        json.dump(books, f, indent=4)

# Function to add a new book
def add_book():
    books = load_books()
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    quantity = int(input("Enter Quantity: "))

    # create dictionary for book
    new_book = {"BookID": book_id, "Title": title, "Author": author, "Quantity": quantity}
    books.append(new_book)
    save_books(books)
    print("✅ Book added successfully!\n")

# Function to view all books
def view_books():
    books = load_books()
    if not books:
        print("⚠️ No books available.\n")
        return
    
    print("\n📚 Available Books:")
    print("="*60)
    print(f"{'Book ID':<10}{'Title':<20}{'Author':<15}{'Qty':<5}")
    print("-"*60)
    for book in books:
        print(f"{book['BookID']:<10}{book['Title']:<20}{book['Author']:<15}{book['Quantity']:<5}")
    print("="*60 + "\n")

# Function to borrow a book
def borrow_book():
    books = load_books()
    book_id = input("Enter Book ID to borrow: ")
    for book in books:
        if book["BookID"] == book_id:
            if book["Quantity"] > 0:
                book["Quantity"] -= 1
                save_books(books)
                print(f"✅ You borrowed '{book['Title']}' successfully!\n")
                return
            else:
                print("❌ Sorry, this book is not available right now.\n")
                return
    print("❌ Book not found.\n")

# Function to return a book
def return_book():
    books = load_books()
    book_id = input("Enter Book ID to return: ")
    for book in books:
        if book["BookID"] == book_id:
            book["Quantity"] += 1
            save_books(books)
            print(f"✅ You returned '{book['Title']}' successfully!\n")
            return
    print("❌ Book not found.\n")

# Main menu
while True:
    print("===== 📖 Mini Library Management System =====")
    print("1. ➕ Add Book")
    print("2. 📚 View All Books")
    print("3. 📕 Borrow Book")
    print("4. 📗 Return Book")
    print("5. ❌ Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        borrow_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        print("👋 Exiting program. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice, please try again.\n")
