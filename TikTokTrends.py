#Import the TikTok library that accesses the API
from TikTokApi import TikTokApi
verify_fp = "verify_xxx"
api = TikTokApi(custom_verify_fp=verify_fp)

def menu():
    option = input("\nPlease choose an option: \nT: Trending Users\nU: Search for a User\nQ: Quit")
    if option == "T" or option == "t":
        print("\nHere are some trending accounts right now:")
        for trends in api.trending.videos():
            print(trends.author.username)
        menu()
    elif option == "Q" or option == "q":
        print("\nGoodbye.")
        quit()
    elif option == "U" or option == "u":
        search = input("Search for a user: ")
        print("Showing results for \"", search, "\": ")
        for user in api.search.users(search):
            print(user.username)
        menu()
    else:
        print("\nInvalid option, try again!")
        menu()
menu()
