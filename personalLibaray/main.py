import json
book_pick = ['title', 'author', 'publication', 'genre', 'Status']
file_name = "data.txt"


 # ----------------------------------1.add books------------------------------
def addBook() -> str:
    
    try:
        with open(file_name, "r") as f:
            book_save = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        book_save = []

    
    book_dic = {}
    for book_details in book_pick:
        book_input = input(f"Enter the {book_details}: \t")
        book_dic[book_details] = book_input

    
    book_save.append(book_dic)

   
    with open(file_name, "w") as f:
        json.dump(book_save, f, indent=4)

    print("Book added successfully.")       
                
                
   # addBook()  
     
    #  --------------------------2.Delete Book------------------------------ 
def delete_book() -> str:
  try:
    with open("data.txt", "r") as f:
        # lines = json.load(f)
          content = f.read().strip()
          if not content:
                lines = []
          else:
                lines = json.loads(content)
  except (FileNotFoundError, json.JSONDecodeError):
        lines = []

  if not lines:
        print("\n\n📂 No books found to delete.")
        return
  title_to_delete = input("\n\nEnter the title of the book to delete:\t")
  book_found = False

  books_save = []
    

    
 
  for line in lines:
            if title_to_delete.strip().lower() != line['title'].strip().lower():

                books_save.append(line)
  
            else:
                book_found = True  

  with open("data.txt", "w") as f:
                json.dump(books_save, f, indent=4) 
                
  if book_found:
         print(f"\n\nBook with title '{title_to_delete}' has been deleted.")
  else:
         print(f"\n\nBook with title '{title_to_delete}' not found.")
   
          
       
       
            
   # delete_book()          
            # ---------------3.Search Book--------------------------------  
def search_book():
    
    print("\n\n1. Title \n2. Author")
    select = int(input("Enter your choice: "))

   
    field = "title" if select == 1 else "author" if select == 2 else None
    
    
    if not field:
        print("\n\nInvalid choice.")
        return

    search_value = input(f"Enter the {field}: ").strip().lower()

    try:
        with open("data.txt", "r") as f:
            books = json.load(f) 

        found = False
        for book in books:
            if search_value in book[field].strip().lower():  
                print(f"\n\n{book['title']} by {book['author']} ({book['publication']}) - {book['genre']} - {book['Status']}")
                found = True
                

        if not found:
            print("\n\nBook not found.")

    except FileNotFoundError:
        print("\n\nLibrary is empty or file not found.")
    except json.JSONDecodeError:
        print("\n\nInvalid JSON format in file.")

# Run the search function
# search_book()  
  
                    # ------------------display books-----------------
def display_books():
    print("\n\nYour Library:")
    try:
        with open("data.txt", "r") as f:
            data = f.read().strip()
            if not data:
                print("\n\nNo books found.")
                return
            
            y = json.loads(data)

            

            for book in y:
                print(f"\n\n{book['title']} by {book['author']} ({book['publication']}) - {book['genre']} - {book['Status']}")
    except FileNotFoundError:
        print("\n\nLibrary file not found.")
    except json.JSONDecodeError:
        print("\n\nData format is invalid.")

# Example usage
# display_books()                
            
              #  --------------books Statics-------------------
def display_statics():
    with open("data.txt","r") as f:
        y = json.load(f)
        # print(y)
        total_books = 0
        total_percenage = 0
        for book in y:
            total_books+=1
            if book["Status"].lower() == "yes":
                total_percenage +=1
                
        if total_percenage > 0:
            read_percentage = (total_percenage / total_books) * 100
            print(f"\n\nPercentage read: {read_percentage:.2f}%")
        else:
            print("\n\nNo books found.")
        
        print(f"\nTotal books: {total_books}")       
                   
def exit():
  return 0   

def book_libaray()->str:
    while True:
    
        print(f"\n\n*****************************\n\n📚 Menu System: Implement a menu with the following options:\n\n1.Add a book\n2.Remove a book\n3.Search for a book\n4.Display all books\n5.Display statistics (total books, percentage read)\n6.Exit ")
  
        # menu = int(input(f"Enter your choice: "))
        user_input = input("Enter your choice (1-6): ").strip()

        if not user_input.isdigit():
            print("❌ Invalid input! Please enter a number between 1 and 6.\n")
            continue

        menu = int(user_input)
        match menu:
            case 1:
                addBook()
            case 2:
                delete_book()
            case 3:
                search_book()
            case 4:
                display_books()
            case 5:
                display_statics()
            case 6:
                exit()  
                break        
            case _:
                print("Invalid option. Please try again.")
book_libaray()     





 