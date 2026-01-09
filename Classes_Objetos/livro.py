class Book:
    def __init__(self, title, pages):
       self.title = title
       self.pages = pages
    
    
    def __len__(self):
        return self.pages
    
    def __str__(self):
        return f"{self.title} has {self.pages}" 
    
    def __eq__(self, other):
        return self.pages == other.pages 
       

book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)

# Não funcionam direito até chamar os métodos especiais como __str__

print(len(book1)) # TypeError: object of type 'Book' has no len()
print(str(book1)) # <__main__.Book object at 0x102ed2900>
print(book1 == book2) # False mesmo que tenham mesmo número de páginas

print(len(book1)) # 420
print(len(book2)) # 420
print(str(book1)) # 'Built Wealth Like a Boss' has 420 pages
print(str(book2)) # 'Be Your Own Start' has 420 pages
print(book1 == book2) # True