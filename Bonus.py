movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

# Create a list to hold movies with an average rating of 6.0 or higher
filtered_movies = []

# Loop through each movie
for movie in movies:
    title = movie[0]          
    year = movie[1]            
    ratings = movie[2]         
    
    # Calculate the average rating
    avg_rating = sum(ratings) / len(ratings)
    
    # Check if the average rating is 6.0 or higher
    if avg_rating >= 6.0:
        # Add the movie details to the filtered list
        filtered_movies.append((title, year, avg_rating))

# Sort the filtered movies by average rating in descending order
filtered_movies.sort(key=lambda x: x[2], reverse=True)

# Display the results
for index, movie in enumerate(filtered_movies, start=1):
    title, year, avg_rating = movie  # Unpack the movie details
    # Print movie details with average rating rounded to 2 decimal places
    print(f"{index}. {title} ({year}) - Average rating: {avg_rating:.2f} ★")
