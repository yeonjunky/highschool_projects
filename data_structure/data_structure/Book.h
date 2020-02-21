#pragma once

#define MAX_TITLE_LEN 200
#define MAX_AUTHOR_LEN 20
typedef struct _Book Book;
struct _Book
{
	char title[MAX_TITLE_LEN + 1];
	char author[MAX_AUTHOR_LEN + 1];
	int num;
};

Book* New_Book(const char* title, const char* author, int num);
void Delete_Book(Book* book);
void Book_View(Book* book);
int Book_CompareTitle(Book* book, const char* author);
int Book_CompareNum(Book* book, int num);

#include <stdio.h>

#include <string.h>

#include <stdlib.h>

#include <time.h>
