#import module
from googlesearch import search

print('Welcome to Google Search Tool')
 
 #Take Query
 
query = input("What do you want to search on google ? : ")

for result in search(query, start=0, stop=10):
    print(result)
 