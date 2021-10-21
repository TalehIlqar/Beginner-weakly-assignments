import requests
import sys
a = sys.argv

try:
    if a[1] == "moviesearch":
        word = input("get input: ")
        x = requests.get(f'http://www.omdbapi.com/?t={word}&apikey=208436f5')
        # print(x)
        y = x.json()
        # print(x.json())
        print(f'Ad: {y["Title"]} \nIl: {y["Year"]} \nReleased: {y["Released"]} \nGenre: {y["Genre"]}  \nDirector: {y["Director"]}')
    else:
        print("Girdi")

except:
    raise
    print("Girmedi")
# the matrix

