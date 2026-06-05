
def show_main_menu():

    ui_options = [
        """
        ------------=Main Menu=------------     
        1. Search films by keyword
        2. Search films by genre
        3. Search films by genre and year range
        4. View release year range
        5. Exit
        -----------------------------------
        Please select an option (1-5):  """
        ]
    print('='*100)
    print(ui_options[0])

def run_paginated_search(search_func, count_func, title, *args):
    limit = 10
    page = 1
    offset = 0

    total = count_func(*args)

    if total == 0:
        print("\nNo films found.")
        return
    
    total_pages = (total + limit - 1) // limit

    while True:
        films = search_func(*args, limit=limit, offset=offset)

        display_films(
            films=films,
            title=title,
            total=total,
            page=page,
            total_pages=total_pages,
            limit=limit
        )

        if total_pages <= 1:
            break

        print("\nNavigation:")
        print("n - next page")
        print("p - previous page")
        print("b - back to menu")

        choice = input("Choose option: ").strip().lower()

        if choice == "n":
            if page < total_pages:
                page += 1
                offset += limit
            else:
                print("You are already on the last page.")

        elif choice == "p":
            if page > 1:
                page -= 1
                offset -= limit
            else:
                print("You are already on the first page.")

        elif choice == "b":
            break

        else:
            print("Invalid option.")

def buttons_menu(main_db):
    running = True
    while running:
        show_main_menu()
        choice = input().strip()

        match choice:
            case '1':
                input_keyword = ask_keyword()

                run_paginated_search(
                        main_db.search_by_keyword,
                        main_db.count_by_keyword,
                        f"Keyword: {input_keyword}",
                        input_keyword
                    )

            case '2':
                genres = main_db.get_all_genres()
                display_genres(genres)

                genre = ask_genre()

                run_paginated_search(
                    main_db.search_by_genre,
                    main_db.count_by_genre,
                    f"Genre: {genre}",
                    genre
                )
            case '3':
                genres = main_db.get_all_genres()
                display_genres(genres)

                years_range = main_db.get_years_range()
                display_years_range(years_range)

                genre = ask_genre()
                start_year, end_year = ask_year_range()

                run_paginated_search(
                    main_db.search_by_genre_and_year,
                    main_db.count_by_genre_and_year,
                    f"Genre: {genre}, Years: {start_year}-{end_year}",
                    genre,
                    start_year,
                    end_year
                )

            case "4":
                years_range = main_db.get_years_range()
                display_years_range(years_range)
                print("Press Enter")
                input()
            case '5':
                print("Exiting the program. Goodbye!")
                running = False

            case _:
                print("Invalid option. Please try again.")

def ask_keyword():
    return input("Enter a film title to search for: ")

def ask_genre():
    return input("Enter a genre to filter by: ")

def ask_year_range():
    start_year = input("Enter the start year: ")
    end_year = input("Enter the end year: ")
    return start_year, end_year

def ask_next_page():
    return input("Do you want to see the next page of results? (y/n): ").lower() == 'y'

def display_genres(genres):
    if not genres:
        print("No genres found.")
    else:
        print("\nAvailable genres:")
        print("-" * 30)
        for genre in genres:
            print(f"- {genre['name']}")

def display_years_range(years_range):
    if not years_range:
        print("Could not get year range")
        return
    
    data = years_range[0]

    print("\nAvailable release year range:")
    print(f"From {data['min_year']} to {data['max_year']}")

def display_films(films, title, total, page, total_pages, limit):
    print("\n" + "=" * 100)
    print(f"Search: {title}")
    print(f"Total found: {total}")
    print(f"Page: {page}/{total_pages}")
    print(f"Showing: {len(films)} film(s) on this page")
    print("=" * 100)

    print(f"{'Title':<45} {'Year':<8} {'Rating':<10} {'Genre':<15}")
    print("-" * 100)

    for film in films:
        title_text = film["title"]

        if len(title_text) > 42:
            title_text = title_text[:39] + "..."

        print(
            f"{title_text:<45} "
            f"{film['release_year']:<8} "
            f"{film['rating']:<10} "
            f"{film['genre']:<15}"
        )

    print("-" * 100)