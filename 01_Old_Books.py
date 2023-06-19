search_book = input()
books_checked = 0
book_found = False

while True:
    book = input()
    books_checked += 1

    if book == "No More Books":
        break

    if book == search_book:
        book_found = True
        break

if book_found:
    print(f"You checked {books_checked - 1} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {books_checked - 1} books.")
