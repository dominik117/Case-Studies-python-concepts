def filter_books(books, min_year, genres):
    """
    Filters a list of books based on the minimum publication year and a list of genres.
    
    :param books: List of dictionaries, where each dictionary represents a book.
    :param min_year: The minimum publication year for the books.
    :param genres: A list of genres to include in the filter.
    :return: Filtered list of books.
    """
    def book_filter(book):
        return book['year'] >= min_year and any(genre in book['genres'] for genre in genres)

    return list(filter(book_filter, books))

books = [
    {"title": "Book A", "author": "Author X", "year": 2001, "genres": ["Fiction", "Adventure"]},
    {"title": "Book B", "author": "Author Y", "year": 1995, "genres": ["Non-Fiction", "Science"]},
    {"title": "Book C", "author": "Author Z", "year": 2010, "genres": ["Fiction", "Thriller"]},
    # ... more books ...
]

filtered_books = filter_books(books, min_year=2000, genres=["Fiction", "Thriller"])
print(*filtered_books, sep='\n')