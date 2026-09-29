# Simple Movie Recommendation System

# ---------- Movie data (parallel lists) ----------
names = ["Inception", "The Dark Knight", "Titanic", "The Notebook",
         "Avengers", "Interstellar", "Toy Story", "Finding Nemo",
         "The Conjuring", "Get Out", "Forrest Gump", "The Matrix",
         "Frozen", "Joker", "La La Land"]

genres = ["Sci-Fi", "Action", "Romance", "Romance",
          "Action", "Sci-Fi", "Animation", "Animation",
          "Horror", "Horror", "Drama", "Sci-Fi",
          "Animation", "Drama", "Romance"]

ratings = [8.8, 9.0, 7.9, 7.8,
           8.0, 8.7, 8.3, 8.2,
           7.5, 7.7, 8.8, 8.7,
           7.4, 8.4, 8.0]

genre_list = ["Sci-Fi", "Action", "Romance", "Animation", "Horror", "Drama"]


# ---------- Helper functions ----------
def show_all():
    print("\nAll movies:")
    print("-" * 45)
    i = 0
    while i < len(names):
        print(i + 1, ".", names[i], "|", genres[i], "|", ratings[i])
        i = i + 1


def by_genre():
    print("\nAvailable genres:")
    for g in genre_list:
        print("-", g)
    choice = input("Enter a genre: ")

    found = False
    print("\nMovies in", choice, ":")
    for i in range(len(names)):
        if genres[i].lower() == choice.lower():
            print(" *", names[i], "(", ratings[i], ")")
            found = True

    if found == False:
        print("Sorry, no movies found for that genre.")


def by_rating():
    limit = float(input("Enter minimum rating (0 to 10): "))
    if limit < 0 or limit > 10:
        print("Rating must be between 0 and 10.")
        return

    count = 0
    print("\nMovies with rating", limit, "or more:")
    for i in range(len(names)):
        if ratings[i] >= limit:
            print(" *", names[i], "(", ratings[i], ")")
            count = count + 1

    if count == 0:
        print("No movie matches this rating.")
    else:
        print("Total found:", count)


def top_movies():
    # copy the lists so the original order is not changed
    n = []
    r = []
    for i in range(len(names)):
        n.append(names[i])
        r.append(ratings[i])

    # bubble sort (highest rating first)
    for i in range(len(r) - 1):
        for j in range(len(r) - 1 - i):
            if r[j] < r[j + 1]:
                temp = r[j]
                r[j] = r[j + 1]
                r[j + 1] = temp
                temp2 = n[j]
                n[j] = n[j + 1]
                n[j + 1] = temp2

    print("\nTop 5 movies:")
    for i in range(5):
        print(i + 1, ".", n[i], "-", r[i])


def personal_recommendation():
    print("\nRate these movies from 1 to 5 (enter 0 if you have not seen it).")
    picks = [0, 1, 2, 4, 6, 8, 10]      # movies we will ask about
    user_scores = []

    for p in picks:
        score = int(input(names[p] + " (" + genres[p] + "): "))
        while score < 0 or score > 5:
            print("Please enter a number from 0 to 5.")
            score = int(input(names[p] + " (" + genres[p] + "): "))
        user_scores.append(score)

    # add up the score for every genre
    genre_points = [0, 0, 0, 0, 0, 0]
    for k in range(len(picks)):
        g = genres[picks[k]]
        for x in range(len(genre_list)):
            if genre_list[x] == g:
                genre_points[x] = genre_points[x] + user_scores[k]

    # find the genre with the highest points
    best = 0
    for x in range(len(genre_points)):
        if genre_points[x] > genre_points[best]:
            best = x

    if genre_points[best] == 0:
        print("\nYou did not rate anything, so we cannot personalise yet.")
        return

    print("\nYour favourite genre looks like:", genre_list[best])
    print("Recommended for you (movies you have not rated):")

    shown = 0
    for i in range(len(names)):
        already_rated = False
        for k in range(len(picks)):
            if picks[k] == i and user_scores[k] > 0:
                already_rated = True

        if genres[i] == genre_list[best] and already_rated == False:
            print(" *", names[i], "(", ratings[i], ")")
            shown = shown + 1

    if shown == 0:
        print(" You have already seen everything in this genre!")


# ---------- Main menu ----------
print("=== Movie Recommendation System ===")
running = True

while running:
    print("\n1. Show all movies")
    print("2. Recommend by genre")
    print("3. Recommend by minimum rating")
    print("4. Show top 5 movies")
    print("5. Personal recommendation")
    print("6. Exit")

    option = input("Choose an option (1-6): ")

    if option == "1":
        show_all()
    elif option == "2":
        by_genre()
    elif option == "3":
        by_rating()
    elif option == "4":
        top_movies()
    elif option == "5":
        personal_recommendation()
    elif option == "6":
        print("Thank you for using the system. Goodbye!")
        running = False
    else:
        print("Invalid choice, please try again.")
