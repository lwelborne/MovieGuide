# Lenora Welborne
# Movie Guide Part 1
def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    print()
def list_movies(movies):
    if not movies:
        print("There are no movies in the list.")
    else:
        for i, movie in enumerate(movies, start=1):
            print(f"{i}. {movie}")
    print()
def add_movie(movies):
    name = input("Name: ")
    movies.append(name)
    print(f"{name} was added.")
    print()
def delete_movie(movies):
    try:
        number = int(input("Number: "))
        if 1 <= number <= len(movies): 
            removed = movies.pop( number - 1)
            print(f"{removed} was deleted.")
        else:
            print("Invalid movie number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    print()
def main():
    movies = ["Monty Python and the Holy Grail", "On the waterfront", "Cat on a Hot Tin Roof"]
    display_menu()
    while True:
        command = input("Command: ").lower()
        if command == "list":
            list_movies(movies)
        elif command == "add":
            add_movie(movies)
        elif command == "del":
            delete_movie(movies)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")
        print()
if __name__ == "__main__":
    main()
            
