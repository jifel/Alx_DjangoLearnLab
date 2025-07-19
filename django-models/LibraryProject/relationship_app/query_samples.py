from relationship_app.models import Author, Book, Library, Librarian 

#creating sample data for all models

a1 = Author.objects.create(name="Chinua Achebe")
a2 = Author.objects.create(name="TD Jakes")
a3 = Author.objects.create(name="Chimamanda Ngozie")
a4 = Author.objects.create(name ="Toyosi Etim-Effiong")

#adding books
book1 = Book.objects.create(title="Now You Know Me Better",author = a4)
book2 = Book.objects.create(title="Complexities",author = a4)
book3 = Book.objects.create(title="Things Fall Apart",author = a1)
book4 = Book.objects.create(title="The Ancestral Sacrifice",author = a2)
book5 = Book.objects.create(title="Nothing by Chance",author = a3)
book6 = Book.objects.create(title="Everything",author = a3)
book7 = Book.objects.create(title="Little Foxes",author = a1)
book8 = Book.objects.create(title="Possibilities",author = a2)



#adding libraries and their respective books
library1 = Library.objects.create(name="El's Safe Haven")
library1.books.add(book1,book2)
library2 = Library.objects.create(name="Reading Room")
library2.books.add(book4, book8)


#adding librarians
admin1 = Librarian.objects.create(name = "Phina Adams", library =library1)
admin2 = Librarian.objects.create(name = "Aseda Dellor", library =library2)



#Query all books by a specific author.
#checkerway
author_name = "Toyosi Etim-Effiong"
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)
print(books)

#my way
Toyo_books = Book.objects.filter(author__name ="Toyosi Etim-Effiong")
print(Toyo_books)

#Expected Outcome
# <QuerySet [<Book: Now You Know Me Better>, <Book: Complexities>]>


#List all books in a library.(one way to do it)
library_name = "El's Safe Heaven"
EL = Library.objects.get(name=library_name)
esh = EL.books.all()
print(esh)
#<QuerySet [<Book: Now You Know Me Better>, <Book: Complexities>]>


#my way of listing all books in a library
EL = Library.objects.get(name ="El's Safe Haven")
esh = EL.books.all()
print(esh)
#<QuerySet [<Book: Now You Know Me Better>, <Book: Complexities>]>

#get the Librarian of a library
EL = Library.objects.get(name ="El's Safe Haven")

lib = EL.librarian #librarian term here because i didnt not use related_name

print(lib.name)
#Phina Adams
