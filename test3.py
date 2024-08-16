

name_of_member = set()  # اضافه کردن اسم اعضا


def member_library():
    while True:
        name = input("enter name of new member(enter finish to finisg ) : ")
        if name == "finish":
            break
        name_of_member.add(name)


book = set()


def add_book():  # اضافه کردن اسم کتاب
    while True:
        name_book = input("enter name book pleas(enter finish to finisg ) : ")
        if name_book == "finish":
            break
        book.add(name_book)


def view_member():  # دیدن اعضای کتابخانه
    print(f"name of library member : {name_of_member}")


def view_book():  # دیدن لیست کتاب ها
    print(f"name of book in library:\n{book}")


def delet_book():  # حذف یک کتاب

    name_book = input(
        "please enter name of the book that you want to remove: ")
    if name_book in book:
        book.remove(name_book)
        print(book)
    else:
        print("this book was not find")


def delet_member():  # حذف یک عضو

    del_member = input(
        "pleas enter name of the member that you want to remove: ")
    if del_member in name_of_member:
        name_of_member.remove(del_member)
        print(name_of_member)
    else:
        print("this member not find")


debt = {}


def book_lone():  # ثبت گیرنده کتاب
    count = int(input("Enter the number of people you want to register : "))
    i = 0
    while i >= 0:
        key = input("name recever: ")
        value = input("book name : ")
        debt[key] = value
        i += 1
        if count == i:
            break


def show_lending():  # دیدن گیرنده کتاب
    for k in debt:
        print(f"recerver : {k}, book : {debt[k]}")


while True:
    application_ = int(input(""" enter number please!!!!!
                        1-add member :
                        2-add the name of the book :
                        3-view library member
                        4-view name of book: 
                        5-remove member from the library: 
                        6-remove a book from the library :
                        7-lending books : 
                        8-show who bought books:
                        9-exist :   """))
    if application_ == 1:
        member_library()
    if application_ == 2:
        add_book()
    if application_ == 3:
        view_member()
    if application_ == 4:
        view_book()
    if application_ == 5:
        delet_member()
    if application_ == 6:
        delet_book()
    if application_ == 7:
        book_lone()
    if application_ == 8:
        show_lending()
    if application_ == 9:
        break
