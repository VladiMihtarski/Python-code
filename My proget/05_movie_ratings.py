pcs_movies = int(input())

highest_star_movie = ""
highest_star = 0
lowest_star_movie = ""
lowest_star = 10
total_star = 0

for i in range(pcs_movies):
    movie_name = input()
    movie_star = float(input())

    if movie_star > highest_star:
        highest_star_movie = movie_name
        highest_star = movie_star

    if movie_star < lowest_star:
        lowest_star_movie = movie_name
        lowest_star = movie_star

    total_star += movie_star

average_star = total_star / pcs_movies

print(f"{highest_star_movie} is with highest rating: {highest_star:.1f}")
print(f"{lowest_star_movie} is with lowest rating: {lowest_star:.1f}")
print(f"Average rating: {average_star:.1f}")
