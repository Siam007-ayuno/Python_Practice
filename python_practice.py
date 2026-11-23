books = [
    {"name": "Animals", "price": 12.99, "royalty": 4.95},
    {"name": "Dinosaurs", "price": 14.99, "royalty": 4.51},
    {"name": "Christmas", "price": 16.99, "royalty": 4.01},
    {"name": "Vehicles", "price": 10.99, "royalty": 2.10},
]

def earnings(book, copies):
    return book["royalty"] * copies

def rate(book):
    r = book["royalty"]
    if r >= 4.50:
        return "Great"
    elif r >= 4.00:
        return "Good"
    else:
        return "Low"

def best_book(books):
    if not books:
        return None
    best = books[0]
    for book in books:
        if book["royalty"] > best["royalty"]:
            best = book
    return best

def report(books, copies):
    total = 0
    for book in books:
        print(book["name"], "-", rate(book), "- $", earnings(book, copies), "for", copies, "copies")
        total = total + earnings(book, copies)
    print("Total: $", total)

report(books, 100)
best = best_book(books)
print("Best book:", best["name"])
