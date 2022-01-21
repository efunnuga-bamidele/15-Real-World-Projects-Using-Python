from PyDictionary import PyDictionary

dict = PyDictionary()

print("Welcome to my Pocket Dictionary")

query = input("What do you want to Search: ")
print(f'The result for meaning search of "{query}" is : {dict.meaning(query)}')