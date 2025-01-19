def listallbooks():
    with open("books.txt", "r") as books:
        return books.read()


def list_checked_book():
    with open("books.txt", "r") as file:
        lines = file.readline()
        while lines != "":
            aim_line = lines.split(",")
            if aim_line[3] == "T\n":
                print(','.join(aim_line), end="")
            lines = file.readline()


def add_new_book(book):
    with open("books.txt", "a") as books:
        book = book.split(",")
        book.append("F")
        book = ",".join(book)
        books.write(book + "\n")
    print("Your book has been added.Thank you for your support.\n")


def delete_book(name):
    data = ""
    with open("books.txt", "r") as file:
        lines = file.readline()
        while lines != "":
            lines = lines.split(",")
            if name.lower() == lines[1].lower():
                if lines[3] == "T\n":
                    print("This book is checked out, you can not delete it.")
                    new_line = ",".join(lines)
                    data = data + new_line
                    lines = file.readline()

                else:
                    lines = file.readline()
            else:
                new_line = ",".join(lines)
                data = data + new_line
                lines = file.readline()

    with open("books.txt", "w") as file:
        file.write(data)


def search_book_ISBN(number):
    with open("books.txt", "r") as file:
        lines = file.readline()
        while lines != "":
            aim_line = lines.split(",")
            if aim_line[0] == number:
                aim_book = ','.join(aim_line)
                print(f"This is the book: {aim_book}")
            lines = file.readline()


def search_book_byname(name):
    with open("books.txt", "r") as file:
        lines = file.readline()
        while lines != "":
            aim_line = lines.split(",")
            if aim_line[1].lower() == name.lower():
                aim_book = ','.join(aim_line)
                print(f"This is the book that you want to find: {aim_book}")
                lines = file.readline()
            else:
                lines = file.readline()


def check_out_book(student_id, isbn):
    with open("books.txt", "r", encoding="utf-8") as book_file:
        book_lines = book_file.readlines()

    book_found = False
    updated_books = []

    book_name = ""
    for line in book_lines:
        book_info = line.strip().split(',')
        if book_info[0] == isbn:
            book_found = True
            if book_info[3] == 'T':
                print("Sorry, this book is already checked out.")
                return
            else:
                book_info[3] = 'T'
                book_name = book_info[1]
        updated_books.append(','.join(book_info))

    with open("books.txt", "w", encoding="utf-8") as book_file:
        book_file.write('\n'.join(updated_books))

    with open("student.txt", "r", encoding="utf-8") as student_file:
        student_lines = student_file.readlines()

    updated_students = []
    for student_line in student_lines:
        student_info = student_line.strip().split(' ')
        if student_info[0] == student_id:
            student_info.append(book_name)
        updated_students.append(''.join(student_info))

    with open("students.txt", "w", encoding="utf-8") as student_file:
        student_file.write('\n'.join(updated_students))


def list_all_student():
    with open("student.txt", "r", encoding="utf-8") as students:
        return students.read()


number = 1
while number != 9:
    number = int(input("#### Welcome to Mugla Sıtkı Kocman University Library System ####\n"
                       "1-List all the book\n"
                       "2-List all the books that are checked out\n"
                       "3-Add a new book\n"
                       "4-Delete a book\n"
                       "5-Search a book by ISBN number\n"
                       "6-Search a book by name\n"
                       "7-Check out a book\n"
                       "8-List all the students\n"
                       "9-Exit\n"
                       "Enter what do you want to do:"))
    if number < 1 or number > 9:
        print("You entered wrong number,you are being redirected to the main menu...")
    else:
        if number == 1:
            print(listallbooks())
        elif number == 2:
            print(list_checked_book())
        elif number == 3:
            book = input(
                "Please enter book's information with this order; ISBN number,book name,writer name seperated by comma:")
            add_new_book(book)
        elif number == 4:
            name = input("Enter a name that you want to delete:")
            delete_book(name)
        elif number == 5:
            number = input("enter a ISBN to search for a book:")
            search_book_ISBN(number)
        elif number == 6:
            name = input("enter a name to search a book:")
            search_book_byname(name)
        elif number == 7:
            student_id = input("please enter your ID:")
            isbn = input("please enter ISBN number for book:")
            check_out_book(student_id, isbn)
        elif number == 8:
            print(list_all_student())












