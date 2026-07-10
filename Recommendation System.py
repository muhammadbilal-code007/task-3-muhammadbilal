library = {
    "movies": {
        "action": ["John Wick", "Mad Max: Fury Road", "Die Hard"],
        "comedy": ["The Hangover", "Superbad", "Step Brothers"],
        "horror": ["The Conjuring", "Get Out", "A Quiet Place"],
    },
    "books": {
        "fiction": ["1984", "To Kill a Mockingbird", "The Great Gatsby"],
        "non-fiction": ["Sapiens", "Educated", "The Immortal Life of Henrietta Lacks"],
    },
    "games": {
        "action": ["Call of Duty", "Assassin's Creed", "Gears of War"],
        "strategy": ["Civilization VI", "StarCraft II", "Age of Empires II"],
    },
}


def show_recommendations(category):
    print(f"\nAvailable Genres in {category.title()}:")

    for genre in library[category]:
        print("-", genre.title())

    user_genre = input("\nEnter Genre: ").lower()

    if user_genre in library[category]:
        print(f"\nRecommended {category.title()}:\n")

        for index, item in enumerate(library[category][user_genre], start=1):
            print(f"{index}. {item}")

    else:
        print("\nGenre not found.")


while True:

    print("\n==============================")
    print(" Recommendation System")
    print("==============================")
    print("1. Movies")
    print("2. Books")
    print("3. Games")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        show_recommendations("movies")

    elif choice == "2":
        show_recommendations("books")

    elif choice == "3":
        show_recommendations("games")

    elif choice == "4":
        print("\nThank you for using the Recommendation System!")
        break

    else:
        print("\nInvalid Choice. Please try again.")
