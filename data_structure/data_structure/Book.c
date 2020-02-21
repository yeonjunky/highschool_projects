#include "Book.h"

void Book_Book(Book* book, const char* title, const char* author, int num);

Book* New_Book(const char* title, const char* author, int num) {
	Book* book = 0;
	book = (Book*)malloc(sizeof(Book));
	Book_Book(book, title, author, num);
	return book;
}

