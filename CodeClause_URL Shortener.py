import pyshorteners

#Defining the function
def shorten_url(url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    return short_url

#Get the URL from the user
user_url = input("Enter the URL to shorten: ")

#Shorten the URL
shortened_url = shorten_url(user_url)

#Display the shortened URL
print("Shortened URL:", shortened_url)