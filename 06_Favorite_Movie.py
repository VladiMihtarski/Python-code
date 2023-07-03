MAX_MOVIES = 7
movieCount = 0
bestMovieSum = 0
bestMovieTitle = ""

while movieCount < MAX_MOVIES:
    movieTitle = input()

    if movieTitle == "STOP":
        break

    movieSum = 0
    titleLength = len(movieTitle)

    for c in movieTitle:
        if c.islower():
            movieSum += ord(c) - (2 * titleLength)
        elif c.isupper():
            movieSum += ord(c) - titleLength
        else:
            movieSum += ord(c)

    if movieSum > bestMovieSum:
        bestMovieSum = movieSum
        bestMovieTitle = movieTitle

    movieCount += 1

if movieCount == MAX_MOVIES:
    print("The limit is reached.")

print(f"The best movie for you is {bestMovieTitle} with {bestMovieSum} ASCII sum.")
