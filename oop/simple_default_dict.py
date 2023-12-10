from collections import defaultdict


def group_books_by_year(books):

    # Используем defaultdict для автоматического создания пустого списка для каждого года:
    books_by_year = defaultdict(list)

    # Сортируем книги по годам:
    sorted_books = sorted(books, key=lambda x: x["title"])

    #  Итерируемся по отсортированным книгам и вставляем в список по году (ключ) нужную книгу:
    for book in sorted_books:
        books_by_year[book["year"]].append(book)

    return dict(books_by_year)


books_data = [
    {"title": "book_1", "year": "1996"},
    {"title": "book_2", "year": "1998"},
    {"title": "book_3", "year": "1992"},
    {"title": "book_4", "year": "1996"},
]

res = group_books_by_year(books_data)
print(res)
