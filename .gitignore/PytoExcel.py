
#How to Connect Python to Excel - Read and Write Data (Try it!)
#In this tutorial, we would examine how to use Python to create an excel csv file, write data into it, read records from the file and delete records from it.
#To demonstrate how this works, we would build a book databases that would allow us to perform the following operations:

#1. SaveBook(book)
#This function takes a book record as parameter and writes the record into the file
# FUNCTION TO SAVE BOOK TO FILE

def SaveBook(book):
    f = open("BookData.csv","a+")
    f.write(book[0] + ',' + book[1] + ',' + book[2] + ',' + book[3] + '\n')
    f.close()


#2. GetRecord()
#This function accept id as parameter, then searches the database to retrieve the record with the given id
#  FUNCTION TO RETRIEVE A SINGLE BOOK RECORD FROM THE DATABASE

def GetRecord(input_id):
    with open("BookData.csv","r") as f:
         for line in f:
             line = line.rstrip()
             id,title,author,isbn = line.split(",")
             if (id == input_id):
                 return line

#3. AddBook()
#This function prompts the user for book details. Then it calls the SaveBook() function to save the book to file
#  FUNCTION TO ADD A BOOK TO THE DATABASE

def AddBook():
    Book = namedtuple("Book", "ID Title Author ISBN")
    id = input("Enter the ID: ")
    title = input("Enter title of book: ")
    author = input("Enter name of author: ")
    isbn = input("Enter ISBN: ")
    newBook = Book(id, title, author, isbn)
    SaveBook(newBook)
    print("Book was added successfullly")

#4. DisplayBook()
#This function prompts the user for an id, then it calls to the GetRecord() function to retrieve the book corresponding that id and then displays the book details
#  FUNCTION DISPLAY DETAILS OF A PARTICULAR BOOK

def DisplayBook():
    input_id = input("Enter the ID of book to display: ")
    id,title,author,isbn = GetRecord(input_id).split(",")
    if (id == input_id):
        print('{0: <5}'.format(id) + '\n{0: <35}'.format(title) + '\n{0: <25}'.format(author) + '\n{0: <15}'.format(isbn))


#5. DeleteBook()
#This function prompt the user for an id, then it deletes the record corresponding to that id from the file
# FUNCTION TO DELETE A BOOK FROM THE DATABASE

def DeleteBook():
    input_id = input("Enter the ID of the book to delete: ")
    f = open("BookData.csv","r+")
    d = f.readlines()
    f.seek(0)
    for line in d:
        record = line.rstrip()
        id,title,author,isbn = record.split(",")
        if id != input_id:
           f.write(line)
    f.truncate()
    f.close()
    print("Book was successfully deleted from the database!")

#6. ViewBooks()
#This function displays all the books in the database.
# FUNCTION TO VIEW ALL BOOKS IN THE DATABASE

def ViewBooks():
         with open("BookData.csv","r") as f:
             for line in f:
                 line = line.rstrip()
                 id,title,author,isbn = line.split(",")
                 if not line: continue
                 print('{0: <5}'.format(id) + '{0: <35}'.format(title) + '{0: <25}'.format(author) + '{0: <15}'.format(isbn))

#7. Search()
#This function prompts for a search criteria. It then searches through the all the records to find a record that matches with the given criteria.
#  FUNCTION TO SEARCH FOR A BOOK IN THE DATABASE

def Search():
    criteria = input("Enter a search criteria: ")
    with open("BookData.csv","r") as f:
         for line in f:
             line = line.rstrip()
             if line.upper().find(criteria.upper()) != -1:
                 id,title,author,isbn = line.split(",")
                 print('{0: <5}'.format(id) + '\n{0: <35}'.format(title) + '\n{0: <25}'.format(author) + '\n{0: <15}'.format(isbn))


#8. GetTotal()
#This function counts the total number of books in the database.
# GET THE TOTAL NUMBER OF BOOKS

def GetTotal():
        return sum(1 for line in open('BookData.csv'))

#9. DisplayMenu()
#This function displays the menu and allows user to make a choice of operations to perform.
#FUNCTION TO DISPLAY THE MENU

def DisplayMenu():
    print("CHOOSE AN OPERATION. ")
    print("1. ADD A BOOK")
    print("2. DISPLAY BOOK DETAILS")
    print("3. DELETE A BOOK")
    print("4. VIEW BOOKS")
    print("5. SEARCH FOR BOOK")
    print("6. GET TOTAL NUMBER")
    print("7. EXIT")

#The Complete Program
#After you have taken some time to understand the various functions in the program. Then go ahead to copy the complete program and paste in your python IDE and run.
#For any observation, you can leave a comment below. Since the next revision of  this program would be based on users' observations and recommendation, you can point out any areas you would like the program to be improved as well as any features you would like added. So we can work on the next update together.
#You can watch the video here.


import sys
from collections import namedtuple
#****************************************************************************************
#PROGRAM BY:    KINDSON THE GENIUS                                                      *
#SECTION:       PYTHON TUTORIALS                                                        *
#DATE:          1ST JANUARY 2018                                                        *
#Program No.    YOUR SECOND PROGRAM IN 2018                                             *
#****************************************************************************************

print('*' * 75)
print("\n**************** PROGRAM TO CREATE READ AND WRITE TO EXCEL ********************\n\n")
print('*' * 75)

# FUNCTION TO SAVE BOOK TO FILE
def SaveBook(book):
    f = open("BookData.csv","a+")
    f.write(book[0] + ',' + book[1] + ',' + book[2] + ',' + book[3] + '\n')
    f.close()


#  FUNCTION TO RETRIEVE A SINGLE BOOK RECORD FROM THE DATABASE
def GetRecord(input_id):
    with open("BookData.csv","r") as f:
         for line in f:
             line = line.rstrip()
             id,title,author,isbn = line.split(",")
             if (id == input_id):
                 return line


#  FUNCTION TO ADD A BOOK TO THE DATABASE
def AddBook():
    Book = namedtuple("Book", "ID Title Author ISBN")
    id = input("Enter the ID: ")
    title = input("Enter title of book: ")
    author = input("Enter name of author: ")
    isbn = input("Enter ISBN: ")
    newBook = Book(id, title, author, isbn)
    SaveBook(newBook)
    print("Book was added successfullly")


#  FUNCTION DISPLAY DETAILS OF A PARTICULAR BOOK
def DisplayBook():
    input_id = input("Enter the ID of book to display: ")
    id,title,author,isbn = GetRecord(input_id).split(",")
    if (id == input_id):
        print('{0: <5}'.format(id) + '\n{0: <35}'.format(title) + '\n{0: <25}'.format(author) + '\n{0: <15}'.format(isbn))



# FUNCTION TO DELETE A BOOK FROM THE DATABASE
def DeleteBook():
    input_id = input("Enter the ID of the book to delete: ")
    f = open("BookData.csv","r+")
    d = f.readlines()
    f.seek(0)
    for line in d:
        record = line.rstrip()
        id,title,author,isbn = record.split(",")
        if id != input_id:
           f.write(line)
    f.truncate()
    f.close()
    print("Book was successfully deleted from the database!")



# FUNCTION TO VIEW ALL BOOKS IN THE DATABASE
def ViewBooks():
         with open("BookData.csv","r") as f:
             for line in f:
                 line = line.rstrip()
                 id,title,author,isbn = line.split(",")
                 if not line: continue
                 print('{0: <5}'.format(id) + '{0: <35}'.format(title) + '{0: <25}'.format(author) + '{0: <15}'.format(isbn))


#  FUNCTION TO SEARCH FOR A BOOK IN THE DATABASE
def Search():
    criteria = input("Enter a search criteria: ")
    with open("BookData.csv","r") as f:
         for line in f:
             line = line.rstrip()
             if line.upper().find(criteria.upper()) != -1:
                 id,title,author,isbn = line.split(",")
                 print('{0: <5}'.format(id) + '\n{0: <35}'.format(title) + '\n{0: <25}'.format(author) + '\n{0: <15}'.format(isbn))


#FUNCTION TO DISPLAY THE MENU
def DisplayMenu():
    print("CHOOSE AN OPERATION. ")
    print("1. ADD A BOOK")
    print("2. DISPLAY BOOK DETAILS")
    print("3. DELETE A BOOK")
    print("4. VIEW BOOKS")
    print("5. SEARCH FOR BOOK")
    print("6. GET TOTAL NUMBER")
    print("7. EXIT")

# GET THE TOTAL NUMBER OF BOOKS
def GetTotal():
        return sum(1 for line in open('BookData.csv'))

#*********************** BEGINING OF MAIN PROGRAM *******************
DisplayMenu()

#GET USER CHOICE
choice = input("Select an operation (1,2,3,4,5,6,7): ")

#EXIT THE PROGRAM IF THE INPUT IS 7
if choice == '7':
   sys.exit()


if choice == 1:
    AddBook()

elif choice == 2:
    DisplayBook()

elif choice == 3:
    DeleteBook()

elif choice == 4:
    ViewBooks()

elif choice == 5:
    Search()

elif choice == 6:
    print(GetTotal())

else:
   print("Invalid input")
