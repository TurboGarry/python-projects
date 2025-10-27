import pyshorteners 

url = input("Enter Url: \n")

print("Shorten Url: ", pyshorteners.Shortener(timeout=10).tinyurl.short(url))