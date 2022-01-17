import pyshorteners

print("Welcome to my URL Shortener App")

getUrl = input("Enter the url you want to shorten: ")

print("Youe short url is: ",pyshorteners.Shortener().tinyurl.short(getUrl))