from helpers import (
    exit_program,
    list_recipes,
    find_recipe_by_name,
    find_recipe_by_id,
    create_recipe,
    update_recipe,
    delete_recipe,
    search_recipes_by_ingredient
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_recipes()
        elif choice == "2":
            find_recipe_by_name()
        elif choice == "3":
            find_recipe_by_id()
        elif choice == "4":
            create_recipe()
        elif choice == "5":
            update_recipe()
        elif choice == "6":
            delete_recipe()
        elif choice == "7":
            search_recipes_by_ingredient()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all recipes")
    print("2. Find recipe by name")
    print("3. Find recipe by id")
    print("4. Create recipe")
    print("5. Update recipe")
    print("6. Delete recipe")
    print("7. Search recipes by ingredient")

if __name__ == "__main__":
    main()
